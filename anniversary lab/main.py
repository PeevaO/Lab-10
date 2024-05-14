from recognize import Recognizer
from voice import voice
from commands import Command
import time


NAME = 'зус'

recognition = Recognizer()
text_gen = recognition.listen()
voice.text_to_speech(f'Привет! Я {NAME}. Давай я расскажу тебе факт о числе.')
for text in text_gen:
    print(text)
    recognition.stream.stop_stream()
    Command(text)
    time.sleep(0.5)
    recognition.stream.start_stream()
