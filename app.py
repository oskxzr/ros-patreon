import os, random
import time
from instagrapi import Client
InstagramClient = Client()
InstagramClient.login("ros_patreon", "redacted")
Files = os.listdir("images")
ChosenImage = None

#test

while True:
    try:
        ChosenImage = random.choice(Files)
        Path = "images/" + ChosenImage
        InstagramClient.photo_upload(Path, "ros posted " + ChosenImage)
        print("Posted")
        time.sleep(random.randint(2000,4000)/100)
    except Exception as e:
        print("Failed: " + ChosenImage)
        print(e)
