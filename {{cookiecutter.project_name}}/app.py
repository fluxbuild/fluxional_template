from fastapi import FastAPI
from fluxional import Fluxional


app = FastAPI()
fluxional = Fluxional("FluxionalStack")


handler = fluxional.handler()