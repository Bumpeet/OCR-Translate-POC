from transformers import MarianMTModel, MarianTokenizer
from PIL import Image
import pytesseract
from pathlib import Path

print("... loading the translation model...")
model_name = "Helsinki-NLP/opus-mt-sv-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

base_dir = Path(r'images')

for img_path in base_dir.glob('*.png'):
  
    print("... reading the contents ...")
    img = Image.open(img_path)
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img, lang='swe')
    print("swedish --> \n", text)

    print("... converting from swedish to english ")
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    print("english --> \n", [tokenizer.decode(t, skip_special_tokens=True) for t in translated])
