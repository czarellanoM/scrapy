from googletrans import Translator

translator = Translator()

translated_text = translator.translate('Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"', dest='es')
print(translated_text.text)

