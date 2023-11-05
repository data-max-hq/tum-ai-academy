import io
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from transformers import pipeline

app = FastAPI()
sentiment_pipeline = pipeline("sentiment-analysis")


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/analysis")
async def sentiment_analysis(query: str):
    return {"message": query}


@app.get("/generate")
async def generate_image(query: str):
    return {"message": query}
    # image = await _services.generate_image(imgPrompt=query)
    #
    # memory_stream = io.BytesIO()
    # image.save(memory_stream, format="PNG")
    # memory_stream.seek(0)
    # return StreamingResponse(memory_stream, media_type="image/png")


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
