from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'
raw_data = pytesseract.image_to_string(Image.open('sample.jpeg'))
data = [i for i in raw_data.split('\n') if len(i) != 0 and i != '  ' and i != ' '][3:6]
print(data)