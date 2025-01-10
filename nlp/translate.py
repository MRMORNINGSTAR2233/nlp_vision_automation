from translate import Translator

trans = Translator(to_lang='es')

text = "Waste of time"

fer = trans.translate(text)
print(fer)