# aerangbot

Slack RTM API를 이용한 간단한 슬랙봇.

셋업:

    pipenv install

설정:

*   `secret.py.sample`을 복사하여 `secret.py` 파일을 만들고 슬랙에서 발급받은 토큰을 입력한다.

봇 실행하기:

    pipenv run python main.py

참고:

*   [Real time messaging API](https://api.slack.com/rtm)
*   [python-rtmbot](https://github.com/slackapi/python-rtmbot)
