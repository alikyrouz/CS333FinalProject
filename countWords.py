import regex

def totalWords(f):
    # approximate
    spaces = f.count(" ")
    return spaces

def countWords(file, word):
    words = file.count(word)
    return words

def printStats(tot, targetWord, targetCount):
    print(f'there are about {tot} total words in this document')
    print(f'out of these words, the word "{targetWord}" appears {targetCount} times')
    print(f'this means {(targetCount/tot)*100:.2f}% of the words in this document are "{targetWord}"')

def main():
   # fn = input("file path?")
    fn = "C:/Python/PycharmProjects/pythonProject/VC.txt"
    f = open(fn, 'r')
    file = f.read()
    tot = totalWords(file)

    targetWord = ("woman")
    targetCount = countWords(file, targetWord)

    f.close()

    printStats(tot, targetWord, targetCount)

main()
