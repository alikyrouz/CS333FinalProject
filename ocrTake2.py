import pytesseract
from PIL import Image
import os, os.path

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


def main():
    ## input file
    path = "C:/Python/PycharmProjects/pythonProject/Visions of Cody"
    #path = "C:/Python/PycharmProjects/pythonProject/test_images"
    imgs = [] ## initialize image list and string list
    texts = []

    #output file
    fn=open("outputs.txt", 'w')

    ## iterate through images in given folder
    for f in os.listdir(path):
        img = Image.open(os.path.join(path,f))
        imgs.append(img)
        text = pytesseract.image_to_string(img)
        fn.writelines(text)

        # write text to output file
        texts.append(text)


    fn.close()

main()