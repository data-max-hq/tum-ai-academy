import uvicorn
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
sentiment_pipeline = pipeline("sentiment-analysis")


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/analysis")
async def sentiment_analysis(query: str):
    return {"message": query}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
