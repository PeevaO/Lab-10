import json
import requests
from voice import voice


def thanks(text):
    voice.text_to_speech('Рад помочь!')


def fact(text):
    global data
    try:
        response = requests.get('http://numbersapi.com/random/math')
        data = response.json()
        voice.text_to_speech('Ищу новый факт')
        print(data)
    except Exception:
        voice.text_to_speech('Не удалось найти факт')


def read(text):
    voice.text_to_speech(data)


def write(text):
    with open('facts.txt', 'w') as file:
        file.write(data)
    voice.text_to_speech('Факт записан!')


def delete(text):
    with open('facts.txt', 'r') as file:
        row = file.readlines()

    row = row[:-1]

    with open('facts.txt', 'w') as file:
        file.write(row)

    voice.text_to_speech('Последний факт удалён')
