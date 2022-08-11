import uvicorn
from fastapi import FastAPI

from api.v1 import translate
from core.config import settings
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

#Instantiate mode and tokenizer at start of the server 
tokenizer = AutoTokenizer.from_pretrained("t5-base", model_max_length=60)
model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")


def include_router(app):
    app.include_router(translate.router)


def start_application():
    app = FastAPI(title=settings.APP_TITLE)
    include_router(app)
    return app


if __name__ == "__main__":
    app = start_application()
    uvicorn.run(app, host=settings.APP_HOST)
    
