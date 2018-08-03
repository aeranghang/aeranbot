import random
import re

from rtmbot.core import Plugin, Job


patterns = {
    r'(파이[썬선손쏜]|[Pp]ython)': [
        '파이썬요? 사랑입니다.',
    ]
}


random_texts = [
    '과제하기 좋은 날씨입니다.',
    '수업 피드백을 꼭 남겨주세요.',
    '맥주는 몽크 IPA',
    '웅앵웅 쵸키포키',
    '지속하능하게 갈아넣으세요.',
    '질문을 많이 해주세요. 조금이라도 궁금하면 그냥 넘어가지 마세요.',
    '컴퓨터는 맥, 휴대폰은 아이폰, 시계는 애플와치입니다. 물론 에어팟도 사야해요.',
    '파이썬은 *사랑*입니다.',
    '한번에 하기 어려우면 더 작은 조각으로 나눠서 해보세요. 중간중간 더 자주 확인하며 진행하세요.',
    '회고는 하셨나요?',
    '훌륭해요 :)',
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
