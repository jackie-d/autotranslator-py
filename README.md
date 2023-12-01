# Autotranslator Py

## Translate the values of a key value Json file to a Json with updated values

Reads a Json file from the user locally which contains words or sentences of natural human language, translates it by Google services and it gives out a Json with same keys and updated values.

## Usage

#### Installing the required libraries

`pip install -r requirements.txt`

### Use this program

- Set in the `terms.json` file the key-values object you want to translate
- Run `py translate.py`
- Specify the original texts language on request
- Specify the destination texts language on request
- Get the resulting translated object string

#### Non-interactive

It's possible to run the command also as `py transalate.py it en` so it gets specified on prior which languages to translate from and to.

#### Save output to a file

If you run the script by `py translate.py > output.json` you can save the resulting Json object directly to a local file.

#### Codes for language

Codes of two letters are requested as language identifiers
[ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

## GitHub Repository

This is a software written in Python v.3 and it uses [googletrans](https://pypi.org/project/googletrans/) library

## Creator and contributors

Author Suns Deglinnocenti a.k.a. Jackie

Software under the MIT license