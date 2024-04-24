from random import randint
import logging
import requests
import json

logging.basicConfig(filename='analytics.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')


class Research():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.file_reader()
        self.calc = self.Analytics(self.data)

    def file_reader(self, has_header=True):
        logging.info('Starting file_reader')
        with open(self.file_path, 'r') as file:
            text = file.read()
        lines = text.split('\n')
        new_lines = [line for line in lines if line != '']
        if has_header and len(new_lines[0].split(',')) != 2:
            raise ValueError('Incorrect header')
        y = 0
        if has_header:
            y = 1
        if len(new_lines) == 0:
            raise ValueError('No lines')
        for i in range(y, len(new_lines)):
            if new_lines[i] not in ['1,0', '0,1']:
                raise ValueError('Incorrect line')
        return [[int(elem) for elem in new_lines[i].split(',')] for i in range(y, len(new_lines))]

    def send_telegram_message(self, message):
        bot_token = 'BOT_TOKEN'
        chat_id = 'CHANNEL_ID'
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        payload = {'chat_id': chat_id, 'text': message}
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            logging.info('Message sent successfully')
        else:
            logging.error(f'Failed to send message: {response.content}')

    class Calculations():
        def __init__(self, data):
            self.data = data

        def counts(self):
            logging.info('Starting counts')
            return " ".join([str(sum(elem)) for elem in zip(*self.data)])

        def fractions(self, count):
            logging.info('Starting fractions')
            count = list(map(int, count.split(' ')))
            return [(elem / sum(count) * 100) for elem in count]

    class Analytics(Calculations):
        def predict_random(self, num_steps):
            logging.info('Starting Analytics')
            dictionary = {0: [0, 1], 1: [1, 0]}
            return [dictionary[randint(0, 1)] for _ in range(num_steps)]

        def predict_last(self):
            logging.info('Starting predict_last')
            return self.data[-1]

        def save_file(self, data, filename, end='txt'):
            logging.info('Starting save_file')
            with open(f'{filename}.{end}', 'w') as file:
                file.write(data)
