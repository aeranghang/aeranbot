import random

from rtmbot.core import Plugin, Job

from canned_reply import reply_to_pattern, random_texts


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
        reply = reply_to_pattern(data['text'])
        if reply:
            self.outputs.append([data['channel'], reply])
            return
        elif "<@UC3L7FQ7Q>" in data['text']:
            self.outputs.append([
                data['channel'],
                random.choice(random_texts)
            ])
        else:
            pass
