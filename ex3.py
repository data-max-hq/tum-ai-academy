import uvicorn
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
# https://huggingface.co/google/flan-t5-small
flan_t5 = pipeline("text2text-generation", model="google/flan-t5-small")


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/analysis")
async def sentiment_analysis(query: str):
    return {"message": query}


@app.get("/generate")
async def generate_image(prompt: str):
    result = flan_t5(prompt)
    return {"result": result}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
