from canned_reply import reply_to_pattern as r


def test_no_match():
    assert r('아무말') is None


def test_simple_match():
    assert r('파이썬') == '파이썬요? 사랑입니다.'


def test_coin_toss():
    expected = {
        '동전을 던졌습니다 => 앞면',
        '동전을 던졌습니다 => 뒷면',
        '동전을 던졌습니다 => 옆면!?',
        '동전을 던졌습니다 => 사라졌다!',
    }
    actual = {r('동전') for _ in range(100)}
    assert actual == expected


def test_choice():
    expected = {'아이언맨', '슈퍼맨', '글쎄?', '정말 이 중에서 골라야 하나요?'}

    actual = {r('아이언맨이랑 슈퍼맨 중 누구?') for _ in range(100)}
    assert actual == expected
    actual = {r('아이언맨과 슈퍼맨이 싸우면 누가 이겨?') for _ in range(100)}
    assert actual == expected
    actual = {r('아이언맨하고 슈퍼맨하고 싸우면 누가 이겨?') for _ in range(100)}
    assert actual == expected
    actual = {r('아이언맨, 슈퍼맨?') for _ in range(100)}
    assert actual == expected


def test_open_ended_questions():
    expected = {'글쎄...', '다른 분들은 어떻게 생각하세요?', '난 모르겠어.', '좀 더 고민해봐.'}

    actual = {r('이유가 무엇일까요?') for _ in range(100)}
    assert actual == expected
    actual = {r('이유가 뭐지?') for _ in range(100)}
    assert actual == expected
