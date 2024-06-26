from voice import voice
import handlers

COMMANDS = [
    {'id': 0, 'text': 'спасибо', 'handler': handlers.thanks},
    {'id': 1, 'text': 'факт', 'handler': handlers.fact},
    {'id': 2, 'text': 'следующий', 'handler': handlers.fact},
    {'id': 3, 'text': 'прочитать', 'handler': handlers.read},
    {'id': 4, 'text': 'записать', 'handler': handlers.write},
    {'id': 5, 'text': 'удалить', 'handler': handlers.delete}
]

ACTIVATION = 'зус'


class Command:

    def __init__(self, text):
        self.text = text
        self.map()

    def map(self):
        if self.text.startswith(ACTIVATION):
            self.text = self.text.replace(ACTIVATION, '').strip()
            for cmd in COMMANDS:
                if self.text.startswith(cmd['text']):
                    self.run(cmd)
                    return True
            else:
                voice.text_to_speech('Я не знаю такой команды, попробуйте другую.')

    def run(self, cmd):
        handler = cmd['handler']
        text = self.text.replace(cmd['text'], '').strip()
        handler(text)
