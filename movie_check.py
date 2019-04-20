import urllib3
import telegram
from bs4 import BeautifulSoup
import time
import requests
from lxml import html
import argparse

class Check_Movie:
    def __init__(self, bot_key, movie_file, snooze_time):
        self.movies,self.chat_id = [],0
        self.bot_key = bot_key
        self.movie_file = movie_file
        if not isinstance(snooze_time, int):
            self.snooze = int(snooze_time)
        else:
            self.snooze = snooze_time
        with open(movie_file, 'r') as f:
            for movie in f:
                self.movies.append(movie.strip())
        self.bot = telegram.Bot(token=self.bot_key)
        self._get_updates()
        self._make_request()

    def _do_request_bookmyshow(self, url):
        response = requests.get(url, headers={'User-Agent': "Magic Browser"})
        soup = BeautifulSoup(response.content, "lxml")
        data = soup.find_all(class_='showtimes btn _cuatro')
        if len(data) == 1:
            stri = ' Hurray ! Bookings open for movie you Wanted !\n \n'+ url
            self.send_message(self.bot, self.chat_id, stri)
            print(stri)
        else:
            stri = "Sorry bookings are not open for Movie you wanted, Don't worry i will be checking and will tell you once it is available."
            self.send_message(self.bot, self.chat_id, stri)
            print(stri)

    def send_message(self, bot, c_id, message):
        print('bot.send_message(c_id, message)')

    def _make_request(self):
        while True:
            for movie_url in self.movies:
                self._do_request_bookmyshow(movie_url)
            time.sleep(self.snooze)

    def _get_updates(self):
        updates = self.bot.get_updates()
        self.chat_id = updates[0].message.chat_id

class CheckService(Check_Movie):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Movie Availablity Check API.')
        parser.add_argument('-BK','--bot-key',type=str, help='Attach bot_key.')
        parser.add_argument('-MF','--movie-file',type=str, help='path of list of url of movies file.')
        parser.add_argument('-ST','--snooze-time',type=str, help='time interval between\
                notifications in seconds', default=600)
        args = parser.parse_args()
        super().__init__(args.bot_key, args.movie_file, args.snooze_time)

if __name__=='__main__':
    CheckService()
