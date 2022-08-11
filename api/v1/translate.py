from fastapi import APIRouter
from transformers import pipeline
import os
from pathlib import Path

main_directory = (Path(__file__) / ".." / "..").resolve()
main = os.path.join(main_directory, "main")

schema_directory = (Path(__file__) / ".." / "..").resolve()
schemas = os.path.join(schema_directory, "schemas")

core_directory = (Path(__file__) / ".." / "..").resolve()
core = os.path.join(core_directory, "core")

from schemas.translate import Translate
from core.config import settings


from main import model, tokenizer

router = APIRouter()
route_prefix = settings.ROUTER_PREFIX


@router.post(route_prefix+"translate")
def text_translation(req: Translate):

    # provide consumers with options of selecting initial and target languages
    # Easier to add additional languages
    source = req.source_language or "en"
    target = req.target_language or "fr"
    method = "translation_" + source + "_to_" + target
    # Init translator
    translator = pipeline(method, model=model, tokenizer=tokenizer)
    # Translate text
    text = req.text
    translation = translator(text)
    # retrieve translation from object
    output = translation[0]["translation_text"]
    # return Initial text together with the translated text
    return {"initital_text": text, "translated_text": output}
