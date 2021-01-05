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
SINCE = datetime(2021, 1, 5)
UNTIL = datetime(2021, 1, 6)

count = 1
for post in posts:
    if post.date >= SINCE:
        if post.date <= UNTIL:
            print(post.date)
            # path = os.path.join("f.a.online", str(count))
            os.makedirs("f.a.online/{}".format(count))
            path = Path("f.a.online/{}".format(count))
            L.download_post(post, path)
            count += 1
