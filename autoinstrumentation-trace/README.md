### ZeroCode Instrumentation:
Use below commands to bootstrap necessary packages require for python app autoinstrumentation.

> [!WARNING]
> you have to reinstall the auto instrumentation every time you run uv sync or update existing packages. It is therefore recommended to make the installation part of your build pipeline.

- install the appropriate packages:

```uv pip install opentelemetry-distro opentelemetry-exporter-otlp```

- install the auto instrumentation:

```uv run opentelemetry-bootstrap -a requirements | uv pip install --requirement -```

- run app with export using OTLP/grpc:

```uv run opentelemetry-instrument --traces_exporter otlp --metrics_exporter none --logs_exporter none --service_name <your_service_name> --exporter_otlp_protocol grpc --exporter_otlp_endpoint http://localhost:4317 python <app.py>```

- run app with export using OTLP/http:

```uv run opentelemetry-instrument --traces_exporter otlp --metrics_exporter none --logs_exporter none --service_name <your_service_name> --exporter_otlp_protocol http/protobuf  --exporter_otlp_endpoint http://localhost:4318 python <app.py>```

