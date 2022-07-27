# host the main html with fastapi
from re import I
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from shutil import copy2
from matplotlib import image as mpimg
from numpy import floor

import generator_ai
# from generator_ai.code.predict import predict_one, merge_from_file_cfg, build_model
from generator_ai import predict_one, merge_from_file_cfg, build_model 

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

@app.get("/generate/{text}")
def render_generate(text: str, request: Request):
    path_to_cfg= "./generator_ai/code/cfg/flower_cpu.yml"
    merge_from_file_cfg(path_to_cfg)
    text_encoder, netG, dataset, device = build_model(gpu_id=-1, data_dir='', manualSeed=100)
    print('TEXT original: ', text)
    if text.isnumeric():
        text = int(text)
    else:
        raise HTTPException(status_code=400, detail="Bad request")
    img_path, gen_text, cls_name, img_name_org = predict_one(text, text_encoder, netG, dataset, device)
    # move image to the static folder as generated.png
    copy2(img_path, f"static/generated_{text}.png")
    # comput the color inverse of avegerage of colors of the image
    def complementary_color(img):
        return floor(255 - img.max(axis=(0,1))).astype(int) 
    img = mpimg.imread("static/generated.png")
    rgb_complement = tuple(complementary_color(img))
    hex_complement = '#%02X%02X%02X' % rgb_complement
    gen_text = " ".join(gen_text)
    print('current url: ', request.url)
    return {'img': f"static/generated_{text}.png", 
            "color": hex_complement,
            "name": cls_name,
            "description": gen_text 
            }
