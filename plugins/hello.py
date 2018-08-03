import random
import re

from rtmbot.core import Plugin, Job


patterns = {
    r'(파이[썬선손쏜]|python)': [
        '파이썬요? 사랑입니다.',
    ]
}


random_texts = [
    '파이썬은 *사랑*입니다.',
    '웅앵웅 쵸키포키',
    '회고는 하셨나요?',
    '과제하기 좋은 날씨입니다.',
    '컴퓨터는 맥, 휴대폰은 아이폰, 시계는 애플와치입니다. 물론 에어팟도 사야해요.',
]


class InitiateChatJob(Job):
    def run(self, client):
        # return [
        #     ["DC3L7NF1C", 'Hello']
        # ]
        pass


class HelloPlugin(Plugin):
    def register_jobs(self):
        # self.jobs.append(InitiateChatJob(10))
        pass

    def process_message(self, data):
        for p, replies in patterns.items():
            if re.match(p, data['text']):
                self.outputs.append([
                    data['channel'],
                    random.choice(replies)
                ])
                return

        if "<@UC3L7FQ7Q>" in data['text']:
            self.outputs.append([
                data['channel'],
                random.choice(random_texts)
            ])
