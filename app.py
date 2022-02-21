import os, random
import time
from instagrapi import Client
InstagramClient = Client()
InstagramClient.login("ros_patreon", "redomellow")
Files = os.listdir("images")
ChosenImage = None

def RandomNumber():
    Str = ""
    for x in range(10):
        Str = Str + str(random.randint(0,9))
    return Str

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