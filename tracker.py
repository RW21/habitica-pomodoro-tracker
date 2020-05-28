import requests
from pprint import pprint
from datetime import datetime, timedelta

from helper import create_bar_plot

settings = [line for line in open('config')]
user_id = settings[0]
token = settings[1]
pomodoro_task_id = settings[2]
request_url = 'https://habitica.com/api/v3/tasks/' + settings[3]
store_directory = settings[4]


def main(test=False):
    if test:
        test_date = datetime.fromisoformat('2020-05-25')

    headers = {"x-api-user": user_id, 'x-api-key': token,
               'x-client': 'aaf35791-babd-44ef-b102-2e6902684651-pomodoro-tracker'}
    r = requests.get(request_url, headers=headers)

    if r.status_code == 200:
        counter = r.json()['data']['counterUp']
        now = datetime.now()
        day = now.strftime("%A")

        # append to this weeks file
        last_monday = now.date() + timedelta(days=-now.date().weekday(), weeks=1)
        f = open(store_directory + str(last_monday), 'a+')
        f.write(str(counter))
        f.close()

        # Create last weeks plots
        if day == 'Monday':
            yesterday = now - timedelta(days=1)
            last_week_name = str((yesterday - timedelta(days=6)).date())
            f = open(store_directory + last_week_name)
            result = [int(line.strip()) for line in f]
            f.close()

            create_bar_plot(result, yesterday)
