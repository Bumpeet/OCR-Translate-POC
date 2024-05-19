# OCR-Translate-POC

Prerequisites:
    - Install the executable of tesseract OCR from this [link](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe)
    - Durning installation also include the swedish installation.
    - After installation add the path of executable to the environment variables, Path variable.

All the images are present in the images folder in the root directory. Just follow the below commands.

Python:
    - create a venv using `python -m venv ocr-translate`
    - activate the environment `~\ocr-translate\Scripts\activate`
    - then run this command `pip install -m requirements.exe`
    - run `python main.py`