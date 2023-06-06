from fastapi import FastAPI
from fluxional import Fluxional


app = FastAPI()
fluxional = Fluxional(
    api_app=app,
)


@app.get("/hello")
def say_hello():
    return {"message": "hello"}


@app.get("/run-task")
def run_task():
    fluxional.run_quick_task(function_name="some_task", payload={"x": "x"})
    return {"message": "Task ran."}


@fluxional.quick_task
def some_task(x: str):
    print(f"Task Ran. {x}")


handler = fluxional.handler()