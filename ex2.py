import uvicorn
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
# https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english
sentiment_pipeline = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    revision="4643665f84c6760e3cbf6adaace6c398592270af"
)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/analysis")
async def sentiment_analysis(query: str):
    result = sentiment_pipeline(query)
    return {"result": result}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
