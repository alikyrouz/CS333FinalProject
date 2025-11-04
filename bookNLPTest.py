from booknlp.booknlp import BookNLP
import spacy

import en_core_web_sm
nlp = en_core_web_sm.load()

spacy.load('en_core_web_sm')
model_params = {
    "pipeline": "entity,quote,supersense,event,coref",
    "model": "small"
}
booknlp = BookNLP("en", model_params)
def main():
    ## load document; literally try booknlp functions
    fName = "C:/Users/aliky/Downloads/DubiousOnTheRoadFile.txt"
    output = "C:/Users/aliky/Downloads"
    book_id = 'road'
    booknlp.process(fName, output, book_id)

main()
