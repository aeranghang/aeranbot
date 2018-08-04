import random
import re

patterns = {
    r'.*\b주사위.*': [
        lambda g: '주사위를 던졌습니다 => ' + str(random.randint(1, 6)),
    ],
    r'.*\b동전.*': [
        lambda g: '동전을 던졌습니다 => ' + random.choice(
            ['앞면', '뒷면'] * 5 + ['옆면!?', '사라졌다!']
        ),
    ],
    r'(.+?)(이?랑|하고|와|과|,)\s+(.+?)((가|이|이?랑|하고| 중).+)?\?$': [
        lambda g: random.choice([g[0], g[2], '글쎄?', '정말 이 중에서 골라야 하나요?'])
    ],
    r'.+(살|할|뭐|모|뭔|무엇인|무엇일|뭘|무얼)(가요?|까요?|지요?|죠)\?$': [
        '글쎄...',
        '좀 더 고민해봐.',
        '다른 분들은 어떻게 생각하세요?',
        '난 모르겠어.',
    ],
    r'(파이[썬선손쏜]|[Pp]ython)': [
        '파이썬요? 사랑입니다.',
    ],
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


def reply_to_pattern(text):
    for pattern, replies in patterns.items():
        m = re.match(pattern, text)
        if m:
            reply = random.choice(replies)
            if type(reply) == str:
                return reply
            else:
                return reply(m.groups())
    return None
