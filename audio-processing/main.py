import typer
import process
import logging

app = typer.Typer()
app.add_typer(process.app, name="process")

logger = logging.getLogger(__package__)


def run():
    try:
        app()
    except Exception as err:
        logger.error("error running audio-process application")
        raise


if __name__ == "__main__":
    app()
