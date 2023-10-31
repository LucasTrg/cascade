import openai

from link import Link
from conversation import Conversation

from typing import Dict, List
class Chain:

    def __init__(self, sys_message:str="You are a helpful assistant.", links:List[Link]=[]):
        self.links = links
        
    def add_link(self, link:Link):
        self.links.append(link)


    def execute(self):
        conversation = Conversation()
        conversation.add_message({"role":"system", "content":"You are a helpful assistant.", "keep":True})
        for link in self.links:
            conversation = link.execute(conversation)
        return conversation
    
