import os
import typing

def write_file(path: str, content: typing.BinaryIO):
    with open(path, 'wb') as f:
        try:
            while content_bytes := content.read(1024*1024):
                f.write(content_bytes)
        except Exception:
            return {"message": f"error writing file to {path}"}


def delete_files(dir):
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")