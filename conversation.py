from typing import Dict, List
import logging
logging.basicConfig(level=logging.DEBUG)

class Conversation:

    def __init__(self, messages:List[Dict[str,str]]=[]) -> None:
        self.messages = messages

    def add_message(self, message:Dict[str,str], keep:bool=True):
        logging.debug("ADD MESSAGE" + str(message))
        self.messages.append(message)
        self.messages[-1]["keep"] = keep


    def clean(self):
        self.messages = [message for message in self.messages if message['keep']]        
        