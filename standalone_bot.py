import urllib3
import telegram
from bs4 import BeautifulSoup
import time
import requests
from lxml import html
import argparse
from urllib.parse import urlparse
import threading

DEFAULT = " Hello There, Welcome to movie_reminder_bot send me messages using the following format - MU:url1,url2"
class User:
    USER_MAPPING = {}
    def analyze_message(self, chat_id, message):
        if ":" not in message:
            return False
        url = message.split(':', 1)[1]
        if url:
            if self.USER_MAPPING.get(chat_id):
                self.USER_MAPPING[chat_id].append(url)
                return True
            else:
                self.USER_MAPPING[chat_id] = []
                self.USER_MAPPING[chat_id].append(url)
                return True
        else:
            return False

class Check_Movie(User):
    def __init__(self, bot_key):
        super().__init__()
        self.bot = telegram.Bot(token=bot_key)
        self.monitor()
        self.update_id = None
        self._start_message_processing()

    def _start_message_processing(self):
        while True:
            self.chat, self.msg = self._get_updates()
            if self.chat and self.msg:
                res = self.analyze_message(self.chat, self.msg)
                if res:
                    for chat_id, msg in self.USER_MAPPING.items():
                        self._make_request(chat_id, msg)
                        time.sleep(5)
                    else:
                        time.sleep(5)
                else:
                    self.send_message(self.bot, self.chat, DEFAULT)

    def _get_updates(self):
        try:
            updates = self.bot.get_updates(offset=self.update_id, timeout=5)
        except TimeoutError:
            pass
        if len(updates) == 0:
            print("No Messages yet ...")
            return None,None
        else:
            resp = updates.pop()
            chat_id = resp.message.chat_id
            msg = resp.message.text
            self.update_id = resp.update_id + 1
            return chat_id, msg

    def _make_request(self, chat_id, url):
        for movie_url in url:
            self._do_request_bookmyshow(chat_id, movie_url)

    def _do_request_bookmyshow(self, chat_id, url):

        response = requests.get(url, headers={'User-Agent': "Magic Browser"})
        soup = BeautifulSoup(response.content, "lxml")
        data = soup.find_all(class_='showtimes btn _cuatro')
        if len(data) == 1:
            stri = ' Hurray ! Bookings open for movie you Wanted !\n \n'+ url
            self.send_message(self.bot, chat_id, stri)
            print(stri)
        else:
            stri = "Sorry bookings are not open for Movie you wanted, Don't worry i will be checking and will tell you once it is available."
            self.send_message(self.bot, chat_id, stri)
            print(stri)

    def send_message(self, bot, c_id, message):
        print("sending message ...")
        bot.send_message(c_id, message)

    def requester(self):
        while True:
            if len(self.USER_MAPPING.keys())!=0:
                for chat_id, msg in self.USER_MAPPING.items():
                    self._make_request(chat_id, msg)
            time.sleep(5)


    def monitor(self):
        d = threading.Thread(name='requester', target=self.requester)
        d.setDaemon(True)
        d.start()

class CheckService(Check_Movie):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Movie Availablity Check API.')
        parser.add_argument('-BK','--bot-key',type=str, help='Attach bot_key.')
        args = parser.parse_args()
        super().__init__(args.bot_key)

if __name__=='__main__':
    CheckService()
