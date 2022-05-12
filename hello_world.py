from bs4 import BeautifulSoup
import requests
from googletrans import Translator

# website = "https://subslikescript.com/movie/Titanic-120338"
website = 'https://subslikescript.com/movie/The_Godfather-68646'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content)


box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w', encoding="utf-8") as file:
    file.write(transcript)
    file.close()

translator = Translator()

tex_en = transcript.split()

tex_en_f = []
characters = 4900
tex_temp = ""
if len(tex_en) > characters:
    for world_en in tex_en:
        characters -= len(world_en)
        if characters > 0:
            tex_temp += world_en + " "
        else:
            tex_en_f.append(tex_temp)
            tex_temp = ""
            characters = 4900

    can_tex_en = len(tex_en)
    tex_es = ""
    for world in tex_en_f:
        translated_text = translator.translate(world, dest='es')
        tex_es += str(translated_text.text) + " "
        can_tex_en -= 1
        print((100/can_tex_en) * 100, "%")

else:

    tex_en_f = "".join(tex_en)
    translated_text = translator.translate(tex_en_f, dest='es')
    tex_es = str(translated_text.text)

# tex_en = ['meters', 'You']


with open(f'{title}_es.txt', 'w', encoding="utf-8") as file:
    file.write(tex_es)
    file.close()
