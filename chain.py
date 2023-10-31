from typing import List

import openai

from conversation import Conversation
from link import Link


class Chain:
    def __init__(
        self, sys_message: str = "You are a helpful assistant.", links: List[Link] = []
    ):
        self.links = links

    def add_link(self, link: Link):
        self.links.append(link)

    def execute(self):
        conversation = Conversation()
        conversation.add_message(
            {"role": "system", "content": "You are a helpful assistant.", "keep": True}
        )
        for link in self.links:
            conversation = link.execute(conversation)
        return conversation
