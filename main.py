from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_hello_world():
    return {'Hello': 'World'}
