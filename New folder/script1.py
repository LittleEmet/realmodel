from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()
funni: list[dict] = [
    {
        'id':'1',
        'name':'Land'
    },
    {
        'id':'2',
        'name':'Lord'}
]
@app.get("/", response_class=HTMLResponse)
def hehe():
    return '<h1>Salutation!!!!</h1>'
@app.get("/funni/kk")
def funni_kk():
    return funni