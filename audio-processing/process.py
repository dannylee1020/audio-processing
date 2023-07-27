from pydub import AudioSegment

import typer
import random

app = typer.Typer()


@app.command()
def insert_audio(audio: str, ads: str, start_time: int, end_time: int):
    base_path = "/Users/dannylee/Downloads/"
    main_audio = AudioSegment.from_file(base_path + audio)
    insert_ads = AudioSegment.from_file(base_path + ads)

    start_time = start_time * 1000
    end_time = end_time * 1000

    first_part = main_audio[:start_time]
    second_part = main_audio[end_time:]
    new_audio = first_part + insert_ads + second_part

    new_audio.export(
        base_path + f"new_audio_{random.randint(100,999)}.wav", format="wav"
    )
