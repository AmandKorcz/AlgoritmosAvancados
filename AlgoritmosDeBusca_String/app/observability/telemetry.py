from __future__ import annotations

import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

SERVICE_NAME = "string-search-n2"

_tracer: Optional[Any] = None
_meter: Optional[Any] = None
_metrics: dict[str, Any] = {}


class _NoopSpan:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def set_attribute(self, key: str, value: Any) -> None:
        pass


class _NoopTracer:
    def start_as_current_span(self, name: str):
        return _NoopSpan()


class _NoopMetric:
    def add(self, value: float, attributes: Optional[dict[str, Any]] = None) -> None:
        pass

    def record(self, value: float, attributes: Optional[dict[str, Any]] = None) -> None:
        pass


def setup_telemetry(app) -> None:
    """Inicializa OpenTelemetry para traces e métricas.

    A aplicação continua funcionando se as dependências de OpenTelemetry ainda não
    tiverem sido instaladas. Isso facilita a integração gradual no projeto antigo.
    """

    global _tracer, _meter, _metrics

    try:
        from opentelemetry import metrics, trace
        from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
        from opentelemetry.sdk.metrics import MeterProvider
        from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

        resource = Resource.create({"service.name": SERVICE_NAME})

        trace_provider = TracerProvider(resource=resource)
        trace_provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
        trace.set_tracer_provider(trace_provider)
        _tracer = trace.get_tracer(SERVICE_NAME)

        metric_reader = PeriodicExportingMetricReader(ConsoleMetricExporter(), export_interval_millis=5000)
        meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
        metrics.set_meter_provider(meter_provider)
        _meter = metrics.get_meter(SERVICE_NAME)

        _metrics = {
            "search_execution_total": _meter.create_counter(
                name="search_execution_total",
                description="Quantidade de execuções dos algoritmos de busca.",
                unit="1",
            ),
            "search_execution_time_ms": _meter.create_histogram(
                name="search_execution_time_ms",
                description="Tempo de execução dos algoritmos em milissegundos.",
                unit="ms",
            ),
            "search_comparisons_total": _meter.create_counter(
                name="search_comparisons_total",
                description="Quantidade total de comparações realizadas.",
                unit="1",
            ),
            "search_occurrences_total": _meter.create_counter(
                name="search_occurrences_total",
                description="Quantidade total de ocorrências encontradas.",
                unit="1",
            ),
        }

        FastAPIInstrumentor.instrument_app(app)
        logger.info("OpenTelemetry inicializado com exportação no console.")
    except Exception as exc:  # pragma: no cover - fallback depende do ambiente local
        _tracer = _NoopTracer()
        _metrics = {
            "search_execution_total": _NoopMetric(),
            "search_execution_time_ms": _NoopMetric(),
            "search_comparisons_total": _NoopMetric(),
            "search_occurrences_total": _NoopMetric(),
        }
        logger.warning("OpenTelemetry não foi inicializado. Motivo: %s", exc)


def get_tracer():
    return _tracer or _NoopTracer()


def get_metric(name: str):
    return _metrics.get(name, _NoopMetric())
