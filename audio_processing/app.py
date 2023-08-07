from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import random

import process
from utils import script

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck():
    return {"message": "OK"}

@app.post("/insert")
async def insert_audio(audio_sample: UploadFile, audio_ad: UploadFile):
    sample_path = f"./files/{audio_sample.filename}"
    ad_path = f"./files/{audio_ad.filename}"

    script.write_file(sample_path, audio_sample.file)
    script.write_file(ad_path, audio_ad.file)

    new_audio = process.insert_audio(sample_path, ad_path, 3)
    script.delete_files('./files')

    return {"message": "audio successfully inserted"}


@app.post("/replace")
async def replace_audio(audio_sample: UploadFile, audio_ad: UploadFile):
    sample_path = f"./files/{audio_sample.filename}"
    ad_path = f"./files/{audio_ad.filename}"

    script.write_file(sample_path, audio_sample.file)
    script.write_file(ad_path, audio_ad.file)

    new_audio = process.replace_audio(sample_path, ad_path, 3, 6)
    script.delete_files('./files')

    return {"message": "audio successfully replaced"}
