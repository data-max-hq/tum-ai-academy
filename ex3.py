import io
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from transformers import pipeline
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

app = FastAPI()
model_id = "CompVis/stable-diffusion-v1-1"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/analysis")
async def sentiment_analysis(query: str):
    return {"message": query}


@app.get("/generate")
async def generate_image(prompt: str):
    return {"prompt": prompt}
    # prompt = "a photo of an astronaut riding a horse on mars"
    # with autocast("cuda"):
    #     image = pipe(prompt)["sample"][0]
    #
    # image.save("astronaut_rides_horse.png")
    # image = await _services.generate_image(imgPrompt=query)
    #
    # memory_stream = io.BytesIO()
    # image.save(memory_stream, format="PNG")
    # memory_stream.seek(0)
    # return StreamingResponse(memory_stream, media_type="image/png")


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
