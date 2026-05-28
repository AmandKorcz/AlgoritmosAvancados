from typing import List, Optional

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

from app.services.dashboard_repository import dashboard_repository
from app.services.search_service import search_service

router = APIRouter(prefix="/api", tags=["Busca em Strings"])


class TextSearchRequest(BaseModel):
    text: str
    pattern: str
    algorithm: str
    include_steps: bool = False


async def _read_upload_files(files: Optional[List[UploadFile]]) -> list[tuple[str, str]]:
    contents: list[tuple[str, str]] = []

    if not files:
        return contents

    for file in files:
        raw = await file.read()
        text = raw.decode("utf-8", errors="ignore")
        contents.append((file.filename or "arquivo.txt", text))

    return contents


@router.get("/algorithms")
def list_algorithms():
    return {"algorithms": search_service.available_algorithms()}


@router.post("/search")
def search_text(payload: TextSearchRequest):
    try:
        result = search_service.execute(
            algorithm=payload.algorithm,
            text=payload.text,
            pattern=payload.pattern,
            include_steps=payload.include_steps,
        )
        return result.to_dict()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/search/files")
async def search_files(
    pattern: str = Form(...),
    algorithm: str = Form(...),
    include_steps: bool = Form(False),
    files: List[UploadFile] = File(...),
):
    uploaded_files = await _read_upload_files(files)

    if not uploaded_files:
        raise HTTPException(status_code=400, detail="Nenhum arquivo enviado.")

    results = []
    try:
        for file_name, text in uploaded_files:
            result = search_service.execute(
                algorithm=algorithm,
                text=text,
                pattern=pattern,
                file_name=file_name,
                include_steps=include_steps,
            )
            results.append(result.to_dict())
        return {"results": results}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/compare")
def compare_text(payload: TextSearchRequest):
    results = search_service.compare_all(text=payload.text, pattern=payload.pattern)
    return {"results": [result.to_dict() for result in results]}


@router.post("/compare/files")
async def compare_files(
    pattern: str = Form(...),
    files: List[UploadFile] = File(...),
):
    uploaded_files = await _read_upload_files(files)

    if not uploaded_files:
        raise HTTPException(status_code=400, detail="Nenhum arquivo enviado.")

    results = []
    for file_name, text in uploaded_files:
        for result in search_service.compare_all(text=text, pattern=pattern, file_name=file_name):
            results.append(result.to_dict())

    return {"results": results}


@router.get("/dashboard")
def dashboard():
    return dashboard_repository.summary()
