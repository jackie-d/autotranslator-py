from googletrans import Translator
import json, sys

termsFile = open('terms.json')
terms = json.load(termsFile)

src = sys.argv[1] if len(sys.argv) > 1 else None
if not bool(src):
    src = input('Which language would you like to translate your words from? (it) ') or 'it'

dest = sys.argv[2] if len(sys.argv) > 2 else None
if not bool(dest):
    dest = input('In which language would you like to translate to? (en) ') or 'en'

translator = Translator()
translations = dict()
for key, value in terms.items():
    translated = translator.translate(value, src=src, dest=dest)
    translations[key] = translated.text

print(json.dumps(translations))