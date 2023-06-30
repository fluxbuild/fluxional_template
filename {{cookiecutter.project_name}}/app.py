from fluxional import Fluxional

fluxional = Fluxional("FluxionalStack")

def app(event: dict, request: dict) -> dict:
    return {"statusCode": 200, "body": 'Hello World!'}

fluxional.add_api(app)

handler = fluxional.handler()