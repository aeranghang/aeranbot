from rtmbot import RtmBot
from rtmbot.core import Plugin, Job
import secret
from canned_reply import reply_to_pattern, generals, mentions


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
        reply = reply_to_pattern(data['text'], generals)
        if reply is None and "<@UC3L7FQ7Q>" in data['text']:
            reply = reply_to_pattern(data['text'], mentions)
        if reply:
            self.outputs.append([data['channel'], reply])


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
