from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Set up the resource attributes
resource = Resource(attributes={"service.name": "computations", "os-version": "ubuntu-22.04 LTS", "environment": "wsl2"})

provider = TracerProvider(resource=resource)
#processor = BatchSpanProcessor(ConsoleSpanExporter())
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="localhost:4317", insecure=True))
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("computations.tracer")

@tracer.start_as_current_span("add")
def add(a, b):
    result = a + b
    return result

@tracer.start_as_current_span("multiply")
def multiply(a, b):
    result = a * b
    return result

def main():
    with tracer.start_as_current_span("computations"):
        x = 5
        y = 10
        sum_result = add(x, y)
        product_result = multiply(sum_result, 2)
        print(f"Final Result is: {product_result}")
    
if __name__ == "__main__":
    main()
