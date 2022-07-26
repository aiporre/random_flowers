# host the main html with fastapi
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def main():
    # return {"message": "Hello World"}
    return RedirectResponse(url="/render")

@app.get("/render", response_class=HTMLResponse)
def render_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
    # return request


@app.get("/about", response_class=HTMLResponse)
def render_about(request: Request):
    return templates.TemplateResponse("aboutbase.html", {"request": request})

@app.get("/generate")
def render_generate(request: Request):
    return {'img': "static/img/generate.png", "color": "#9BA0BC"}