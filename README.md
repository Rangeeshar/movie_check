# GROUP MOVIE NOTIFIER
A movie booking availability notification for your telegram group.
- Clone the repository , install the required modules using the following command:
   - `pip install .`
- Add whatever movie URL, in a text file.
- If you want to add it in your telegram group, Create a bot using bot father using following link:
   - https://core.telegram.org/bots
- After creating the bot make note of the bot key they give for your bot.
- Then run the movie_check.py using following parameters:
```
usage: movie_check.py [-h] [-BK BOT_KEY] [-MF MOVIE_FILE] [-ST SNOOZE_TIME]

Movie Availablity Check API.

optional arguments:
  -h, --help            show this help message and exit
  -BK BOT_KEY, --bot-key BOT_KEY
                        Attach bot_key.
  -MF MOVIE_FILE, --movie-file MOVIE_FILE
                        path of list of url of movies file.
  -ST SNOOZE_TIME, --snooze-time SNOOZE_TIME
                        time interval between notifications in seconds
```
- Add the telegram bot to your group by inviting the bot to the group using your bot name which you used while creating
    - For example `@movienotify_bot`
- An example would be `python3 movie_check.py -BK dsajdajd:dad8dsa7d -MF ~/home/rangeesh/movis_urls.txt -ST 700`
- Now if you run the script it will send you notification about your booking in a time interval you specified to the telegram group.
