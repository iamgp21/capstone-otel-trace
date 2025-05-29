from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.sdk.resources import Resource

# Set up the resource attributes
resource = Resource(attributes={"service.name": "main", "os-version": "ubuntu-22.04 LTS", "environment": "wsl2"})

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("global.tracer")

@tracer.start_as_current_span("main")
def main():
    try:
        current_span = trace.get_current_span()
        print("Hello from capstone-otel-trace!")
    
    except Exception as e:
        # Record the exception in the current span
        current_span.record_exception(e)
        # Set the span status to error
        current_span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
        

if __name__ == "__main__":
    main()
