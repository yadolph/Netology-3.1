

import json
from pprint import pprint

def parse_all_list(all_list):

    word_list = []
    for item in all_list:
        for word in item:
            word_list.append(word.lower())

    word_list = [x for x in word_list if len(x) >= 6]

    word_list_unique = list(set(word_list))

    word_counts = {}

    for word in word_list_unique:
        word_counts[word] = word_list.count(word)

    list_of_word_counts = sorted(word_counts.items(), reverse=True, key=lambda item: item[1])

    for item in list_of_word_counts[:10]:
        print(f'{item[0]} - {item[1]}')


print('10 самых часто встречающихся слов из файла .json:')

with open('newsafr.json') as f:
    all_list = []

    json_data = json.load(f )
    for item in json_data['rss']['channel']['items']:
        all_list.append(item['description'].split(' '))

    parse_all_list(all_list)

print('\n 10 самых часто встречающихся слов из файла .xml:')

import xml.etree.ElementTree as ET

with open('newsafr.xml') as f:
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(f, parser=parser)
    root = tree.getroot()
    channel = root.find('channel')
    items = channel.findall('item')

    all_list = []

    for item in items:
        all_list.append(item.find('description').text.split(' '))

    parse_all_list(all_list)