import random


class UserAgentsMiddleware(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.user_agents = [
                line.strip()
                for line in f.readlines()
            ]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get(
                'USER_AGENTS_LIST_FILE',
                'user-agents.txt'
            ),
        )

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agents)
        request.headers.setdefault('User-Agent', user_agent)
