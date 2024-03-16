import os
import re

from utils.lock import acquire_lock
from utils.logging import log
from constants import PDF_DIR


def main():
    # Define the local PDF file path
    pdf_file_path = "/Users/tarique/Downloads/LLM-main/data/book.pdf"

    # Call the read_from_local function
    result = read_from_local(pdf_file_path)

    # Check if the result is not empty
    if result:
        print("PDF file found at " + os.path.abspath(result))
    else:
        print("PDF file not found or invalid path")


def read_from_local(file_path: str) -> str:
    if not os.path.exists(file_path):
        print("PDF file does not exist at " + os.path.abspath(file_path))
        return ""

    return file_path


def normalize_filename(filename):
    # Replace any invalid characters with an underscore
    return re.sub(r"[^\w\-_. ]", "_", filename)


if __name__ == "__main__":
    main()
