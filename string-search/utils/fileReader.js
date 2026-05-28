export async function readFiles(files) {
  const contents = [];

  for (const file of files) {
    const text = await file.text();
    contents.push({
      name: file.name,
      content: text
    });
  }

  return contents;
}