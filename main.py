from datetime import datetime
from pathlib import Path

import os
import instaloader

L = instaloader.Instaloader()
user = input("Please enter your username: \n")
password = input("Please enter your password: \n")
page = input("Please enter the page you want to scrap for posts: \n")
L.login(user, password)
posts = instaloader.Profile.from_username(L.context, page).get_posts()

print("posts gotten")
# start_date_year = int(input("Please enter the year you want to start from: \n"))
# start_date_month = int(input("Please enter the month you want to start from: \n"))
# start_date_day = int(input("Please enter the day you want to start from: \n"))
# end_date_year = int(input("Please enter the year you want your posts to end at: \n"))
# end_date_month = int(input("Please enter the month you want your posts to end at: \n"))
# end_date_day = int(input("Please enter the day you want your posts to end at: \n"))
SINCE = datetime(2021, 1, 5)
UNTIL = datetime(2021, 1, 6)

count = 1
for post in posts:
    if post.date >= SINCE:
        if post.date <= UNTIL:
            print(post.date)
            # path = os.path.join("f.a.online", str(count))
            os.makedirs("{}/{}".format(page, count))
            path = Path("{}/{}".format(page, count))
            L.download_post(post, path)
            count += 1
