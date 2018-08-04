from rtmbot.core import Plugin, Job

from canned_reply import reply_to_pattern, mentions, generals


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
        if "<@UC3L7FQ7Q>" in data['text']:
            reply = reply_to_pattern(data['text'], mentions)
        else:
            reply = reply_to_pattern(data['text'], generals)

        if reply:
            self.outputs.append([data['channel'], reply])
