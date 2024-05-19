from transformers import MarianMTModel, MarianTokenizer
from PIL import Image
import pytesseract
from pathlib import Path

print("... loading the translation model")
model_name = "Helsinki-NLP/opus-mt-sv-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

print("... reading the contents")
# Open an image file
# image = Image.open(r'D:\\Chetan\\passion\\tesseract-poc\\images\\img3.png')

base_dir = Path(r'images')

# Open an image file
# image = Image.open(r'D:\\Chetan\\passion\\tesseract-poc\\images\\MicrosoftTeams-image (11).png')

for img_path in base_dir.glob('*.png'):
    # Use Tesseract to do OCR on the image
    img = Image.open(img_path)
    text = pytesseract.image_to_string(img, lang='swe')

    # Use Tesseract to do OCR on the image
    # text = pytesseract.image_to_string(image, lang='swe')
    print("swedish --> \n", text)

    print("... converting from swedish to english ")
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    print("english --> \n", [tokenizer.decode(t, skip_special_tokens=True) for t in translated])
