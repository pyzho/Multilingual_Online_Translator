import requests
import re
from bs4 import BeautifulSoup
import sys

def translate_word(lang_from, lang_to, word):
    file = open(word + '.txt', "a+")
    lang_lang = lang_from.lower() + "-" + lang_to.lower() + "/"
    url = 'https://context.reverso.net/translation/' + lang_lang + word
    headers = {
        'authority': 'context.reverso.net',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-gpc': '1',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'experiment_context_Et4k3pePD=1; didomi_token=eyJ1c2VyX2lkIjoiMTdhODYyNmMtYmEzMi02YzIzLThkZWEtYjBiMTg2MzZiYjMyIiwiY3JlYXRlZCI6IjIwMjEtMDctMDhUMTI6NDk6MjQuMTk4WiIsInVwZGF0ZWQiOiIyMDIxLTA3LTA4VDEyOjQ5OjI0LjE5OFoiLCJ2ZXJzaW9uIjoyLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpnb29nbGVhbmEtbTIyS1RwM1kiXX0sInZlbmRvcnNfbGkiOnsiZW5hYmxlZCI6WyJnb29nbGUiXX0sImFjIjoiQUZtQUNBRmsuQUFBQSJ9; euconsent-v2=CPJBYtKPJBYtKAHABBENBhCgAP_AAH_AAAAAIBtf_X__b3_j-_59f_t0eY1P9_7_v-0zjhfdt-8N2f_X_L8X42M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6okVrzPsbk2Mr7NKJ7PEmnMbe2dYGH9_n93TuZKY7__8___z__-v_v____f_r-3_3__59X---_e_V399zLv9_____9nN_4IAgEmGpfABdiWODJtGlUKIEYVhIdAKACigGFomsIGVwU7K4CPUELABCagIwIgQYgoxYBAAIBAEhEQEgB4IBEARAIAAQAqQEIACNgEFgBYGAQACgGhYgRQBCBIQZHBUcpgQESLRQT2VgCUXexphCGUWAFAo_oqMBEoQQLAyEhYOY4AgAAAA.f_gAD_gAAAAA; reverso.net.dapp-promo=0; CTXTNODEID=bstweb17; context.lastpair=en-fr; history_entry=cheese]#[hello; history_pair=en-fr]#[en-fr; reverso.net.dapp-promo-count=6; JSESSIONID=d67jwIaNloyJ_6dTRaDsFCSt.bstweb17; reverso.net.apps-promo=10',
    }

    try:
        requests.get(url, headers=headers)
    except ConnectionError:
        print("Something wrong with your internet connection")
    except requests.exceptions.ConnectionError:
        print("Something wrong with your internet connection")
    else:
        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.content, 'html.parser')
        translation_words = soup.find_all('a', {'class': 'translation'})
        print()
        if len(translation_words) > 1:
            pass
        else:
            raise Exception("Sorry, unable to find " + word)
            sys.exit()
        print(lang_to.capitalize() + ' Translations:')
        file.write(lang_to.capitalize() + ' Translations:\n')
        translations = []
        template = '\w.?'
        for i in translation_words:
            word = str(i.text)[re.search(template,i.text).start():]
            if word != '':
                translations.append(word)
        five_only = 0

        translations = translations[1:]
        print(translations[0])
        file.write(translations[0] + '\n')

        phrases = []
        examples = soup.find_all('div', {'class': 'src ltr'}) + soup.find_all('div', {'class': 'trg ltr'})
        templ_phrase = r'\b.+$'

        for j in examples:
            phrase = str(j.text)[re.search(templ_phrase,j.text).start():re.search(templ_phrase,j.text).end()]
            if phrase != '':
                phrases.append(phrase)

        amount = len(phrases)
        part_two = int(amount / 2)
        ended = []

        print()
        print(lang_to.capitalize() + ' Example:')
        file.write('\n' + lang_to.capitalize() + ' Example:\n')

        for i in range(part_two):
            ended.append(phrases[i])
            ended.append(phrases[i+part_two])
            if i == 0:
                print(phrases[i])
                file.write(phrases[i] + '\n')
                print(phrases[i+part_two])
                file.write(phrases[i+part_two] + '\n')
                print()


def translate_to_file(lang_from, lang_to, word, file):
    my_file = open(file, "a+")
    lang_lang = lang_from.lower() + "-" + lang_to.lower() + "/"

    url = 'https://context.reverso.net/translation/' + lang_lang + word

    headers = {
        'authority': 'context.reverso.net',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-gpc': '1',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'experiment_context_Et4k3pePD=1; didomi_token=eyJ1c2VyX2lkIjoiMTdhODYyNmMtYmEzMi02YzIzLThkZWEtYjBiMTg2MzZiYjMyIiwiY3JlYXRlZCI6IjIwMjEtMDctMDhUMTI6NDk6MjQuMTk4WiIsInVwZGF0ZWQiOiIyMDIxLTA3LTA4VDEyOjQ5OjI0LjE5OFoiLCJ2ZXJzaW9uIjoyLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpnb29nbGVhbmEtbTIyS1RwM1kiXX0sInZlbmRvcnNfbGkiOnsiZW5hYmxlZCI6WyJnb29nbGUiXX0sImFjIjoiQUZtQUNBRmsuQUFBQSJ9; euconsent-v2=CPJBYtKPJBYtKAHABBENBhCgAP_AAH_AAAAAIBtf_X__b3_j-_59f_t0eY1P9_7_v-0zjhfdt-8N2f_X_L8X42M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6okVrzPsbk2Mr7NKJ7PEmnMbe2dYGH9_n93TuZKY7__8___z__-v_v____f_r-3_3__59X---_e_V399zLv9_____9nN_4IAgEmGpfABdiWODJtGlUKIEYVhIdAKACigGFomsIGVwU7K4CPUELABCagIwIgQYgoxYBAAIBAEhEQEgB4IBEARAIAAQAqQEIACNgEFgBYGAQACgGhYgRQBCBIQZHBUcpgQESLRQT2VgCUXexphCGUWAFAo_oqMBEoQQLAyEhYOY4AgAAAA.f_gAD_gAAAAA; reverso.net.dapp-promo=0; CTXTNODEID=bstweb17; context.lastpair=en-fr; history_entry=cheese]#[hello; history_pair=en-fr]#[en-fr; reverso.net.dapp-promo-count=6; JSESSIONID=d67jwIaNloyJ_6dTRaDsFCSt.bstweb17; reverso.net.apps-promo=10',
    }
    try:
        requests.get(url, headers=headers)
    except ConnectionError:
        print("Something wrong with your internet connection")
    except requests.exceptions.ConnectionError:
        print("Something wrong with your internet connection")
    except UnboundLocalError:
        print("Something wrong with your internet connection")

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    translation_words = soup.find_all('a', {'class': 'translation'})
    try:
        result = translation_words[2]
    except IndexError:
        print("Sorry, unable to find " + word)
        sys.exit()
    my_file.write(lang_to.capitalize() + ' Translations:\n')
    translations = []
    template = '\w.?'
    for i in translation_words:
        word = str(i.text)[re.search(template,i.text).start():]
        if word != '':
            translations.append(word)

    translations = translations[1:]
    my_file.write(translations[0] + '\n')
    phrases = []
    examples = soup.find_all('div', {'class': 'src ltr'}) + soup.find_all('div', {'class': 'trg ltr'})
    templ_phrase = r'\b.+$'

    for j in examples:
        phrase = str(j.text)[re.search(templ_phrase,j.text).start():re.search(templ_phrase,j.text).end()]
        if phrase != '':
            phrases.append(phrase)

    amount = len(phrases)
    part_two = int(amount / 2)
    ended = []

    my_file.write('\n')
    my_file.write(lang_to.capitalize() + ' Example:\n')

    for i in range(part_two):
        ended.append(phrases[i])
        ended.append(phrases[i+part_two])
        if i == 0:
            my_file.write(phrases[i] + '\n')
            my_file.write(phrases[i+part_two] + '\n')
            my_file.write('\n')

    my_file.close()

args = sys.argv
if len(args) == 4:
    target_lang_in = args[1]
    target_lang_to = args[2]
    target_word = args[3]
else:
    args[1] = None
    args[2] = None
    args[3] = None
    target_lang_in = input()
    target_lang_to = input()
    target_word = input()
languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']

if target_lang_to != "all":
    try:
        languages.index(target_lang_to.capitalize())
    except ValueError:
        print("Sorry, the program doesn't support " + target_lang_to)
        sys.exit()
    translate_word(target_lang_in, target_lang_to, target_word)

else:
    name_file = target_word + '.txt'
    languages.pop(languages.index(target_lang_in.capitalize()))
    for language in languages:
        translate_to_file(target_lang_in, language, target_word, name_file)

    f = open(name_file,'r')
    print(f.read())
