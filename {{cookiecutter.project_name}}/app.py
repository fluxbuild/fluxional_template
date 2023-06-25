from fluxional import Fluxional
from fluxional.infrastructure import InfraBuilder


def app(event: dict, request: dict) -> dict:
    return {"message": "Hello World!"}


fluxional = Fluxional("FluxionalStack", api_app=app)


handler = fluxional.handler()

stack = fluxional.generate_infrastructure(to_dict=True)

builder = InfraBuilder(stack)

builder.synth()
