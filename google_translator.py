import googletrans
from googletrans import Translator

translator=googletrans.Translator()

input_text=input("Enter the text:")
input_language=input("Enter the language:")
 
translate=translator.translate(text=input_text, dest=input_language)
print(translate.text)