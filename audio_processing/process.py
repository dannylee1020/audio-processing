from pydub import AudioSegment

import typer
import random
import io

app = typer.Typer()

BASE_PATH = '/Users/dannylee/Downloads/'

@app.command()
def insert_audio(audio_path: str, ad_path: str, start_time: int):
    main_audio = AudioSegment.from_file(audio_path)
    insert_ad = AudioSegment.from_file(ad_path)

    start_time = start_time * 1000

    first_part = main_audio[:start_time]
    second_part = main_audio[start_time:]
    new_audio = first_part + insert_ad + second_part

    new_audio.export(BASE_PATH + f"insert_audio_{random.randint(100,999)}.wav", format="wav")
    return new_audio

@app.command()
def replace_audio(audio_path: str, ad_path: str, start_time: int, end_time: int):
    main_audio = AudioSegment.from_file(audio_path)
    insert_ad = AudioSegment.from_file(ad_path)

    start_time = start_time * 1000
    end_time = end_time * 1000

    first_part = main_audio[:start_time]
    second_part = main_audio[end_time:]
    new_audio = first_part + insert_ad + second_part

    new_audio.export(BASE_PATH + f"replace_audio_{random.randint(100,999)}.wav", format="wav")