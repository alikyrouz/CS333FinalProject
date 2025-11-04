
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import sentencepiece
from transformers import TFXLNetModel, XLNetTokenizer
import os, os.path

def main():
    ## initialize processor (with text base?)
    processor = TrOCRProcessor.from_pretrained("microsoft/trocr-large-printed")
    model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-large-printed")

    #path = "C:/Python/PycharmProjects/New folder"
    path = "C:/Python/PycharmProjects/pythonProject/test"

    imgs = []
    for f in os.listdir(path):
        imgs.append(Image.open(os.path.join(path,f)))

    pixel_values = processor(imgs, return_tensors='pt').pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)

    # model
    fn = open("outputs.txt", 'w')
    for t in generated_text:
        fn.writelines(t)
    fn.close()
# output text
main()