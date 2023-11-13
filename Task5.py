import pytesseract
from PIL import Image
import sys

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python extract_text_from_image.py image_path")
    else:
        image_path = sys.argv[1]
        extracted_text = extract_text_from_image(image_path)
        print(extracted_text)
