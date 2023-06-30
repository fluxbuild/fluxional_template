from fluxional import Fluxional


def app(event: dict, request: dict) -> dict:
    return {"statusCode": 200, "body": 'Hello World!'}


fluxional = Fluxional("FluxionalStack", api=app)


handler = fluxional.handler()