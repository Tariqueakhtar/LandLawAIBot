import requests
import os
import re

from utils.lock import acquire_lock
from utils.logging import log
from constants import PDF_DIR


# Read a pdf file from a local path and return the path to the file
def download(file_path: str) -> str:
    if not os.path.exists(file_path):
        log("PDF file does not exist at " + os.path.abspath(file_path))
        return ""

    return file_path


def normalize_filename(filename):
    # Replace any invalid characters with an underscore
    return re.sub(r"[^\w\-_. ]", "_", filename)
