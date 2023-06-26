from fluxional import Fluxional


def app(event: dict, request: dict) -> dict:
    return {"message": "Hello World!"}


fluxional = Fluxional("FluxionalStack", api=app)


handler = fluxional.handler()