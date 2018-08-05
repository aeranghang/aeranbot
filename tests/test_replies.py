from canned_reply import reply_to_pattern as r, generals, mentions


def test_no_match():
    assert r('아무말', generals) is None


def test_simple_match():
    assert r('파이썬', generals) == '파이썬요? 사랑입니다.'


def test_coin_toss():
    expected = {
        '동전을 던졌습니다 => 앞면',
        '동전을 던졌습니다 => 뒷면',
        '동전을 던졌습니다 => 옆면!?',
        '동전을 던졌습니다 => 사라졌다!',
    }
    actual = {r('동전', generals) for _ in range(100)}
    assert actual == expected


def test_choice():
    expected = {'아이언맨', '슈퍼맨', '글쎄?', '정말 이 중에서 골라야 하나요?'}

    actual = {r('아이언맨이랑 슈퍼맨 중 누구?', generals) for _ in range(100)}
    assert actual == expected
    actual = {r('아이언맨과 슈퍼맨이 싸우면 누가 이겨?', generals) for _ in range(100)}
    assert actual == expected
    actual = {r('아이언맨하고 슈퍼맨하고 싸우면 누가 이겨?', generals) for _ in range(100)}
    assert actual == expected
    actual = {r('아이언맨, 슈퍼맨?', generals) for _ in range(100)}
    assert actual == expected


def test_vs():
    expected = {'아이언맨', '슈퍼맨', '둘 다 별로...'}

    actual = {r('아이언맨 vs. 슈퍼맨', generals) for _ in range(100)}
    assert actual == expected
    actual = {r('아이언맨 vs.슈퍼맨', generals) for _ in range(100)}
    assert actual == expected
    actual = {r('아이언맨 vs 슈퍼맨', generals) for _ in range(100)}
    assert actual == expected



def test_open_ended_questions():
    expected = {'글쎄...', '다른 분들은 어떻게 생각하세요?', '난 모르겠어.', '좀 더 고민해봐.'}

    actual = {r('이유가 무엇일까요?', generals) for _ in range(100)}
    assert actual == expected
    actual = {r('이유가 뭐지?', generals) for _ in range(100)}
    assert actual == expected
    actual = {r('맥 살까?', generals) for _ in range(100)}
    assert actual == expected


def test_ask_for_name():
    expected = {'내 이름은 애란봇이야. 사실은 시리보다 똑똑하지.', '애란봇입니다 :)'}

    actual = {r('이름이 뭐냐?', mentions) for _ in range(100)}
    assert actual == expected
    actual = {r('이름이 뭔가요?', mentions) for _ in range(100)}
    assert actual == expected


def test_statements():
    expected = {'왜 놀랬어요?', '어떻게 놀랬어요?', '놀랬어요?', '정말?', '그랬구나.', 'ㅇㅇ'}

    actual = {r('대박 놀랬어요.', mentions) for _ in range(100)}
    assert actual == expected
    actual = {r('놀랬어요!', mentions) for _ in range(100)}
    assert actual == expected
