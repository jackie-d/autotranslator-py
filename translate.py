from googletrans import Translator
import json, sys, keyboard

# open input json file
termsFile = open('terms.json')
terms = json.load(termsFile)

# read which languages from input
src = sys.argv[1] if len(sys.argv) > 1 else None
if not bool(src):
    src = input('Which language would you like to translate your words from? (it) ') or 'it'

dest = sys.argv[2] if len(sys.argv) > 2 else None
if not bool(dest):
    dest = input('In which language would you like to translate to? (en) ') or 'en'

# prepare elaboration
translator = Translator()
translations = dict()
withErrors = 0
continueElaboration = True

# prepare quitting
def setQuitExecution():
    print('User interrupt', file=sys.stderr)
    global continueElaboration
    continueElaboration = False

keyboard.add_hotkey("ctrl+q", setQuitExecution)

# execute elaboration
for key, value in terms.items():
    if not continueElaboration:
        break
    try:
        translated = translator.translate(value, src=src, dest=dest)
    except Exception as e:
        print(e, file=sys.stderr)
        withErrors = 1
    translations[key] = translated.text
    print('Translating: ' + key, file=sys.stderr, end='\r')

#print result
print(json.dumps(translations))

#quit execution
sys.exit(withErrors)