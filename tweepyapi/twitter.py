import tweepy
from tweepy import OAuthHandler
import json
import wget
import os
import subprocess
import io
from google.cloud import vision
from google.cloud.vision import types
 
consumer_key = "l9ogUMvrMxBECaFqXvrlyWfX8"
consumer_secret = "YVILwNXqerV9ucUzprvfmSeNU6i89QnNRqYHhi2J4zA4AgKixB"
access_token = "920695657740013568-04EYTz7rqWRWRuSKy0jiSEZxS5fHuLV"
access_secret = "aHisrtBZFuqkCjB4z3i6L224de1GzcsKI8ZyVioe9AgoX"
 
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="@Ibra_official",
                           count=200, include_rts=False,
                           exclude_replies=True)
last_id = tweets[-1].id
 
while (True):
    more_tweets = api.user_timeline(screen_name="@Ibra_official",
                                count=200,
                                include_rts=False,
                                exclude_replies=True,
                                max_id=last_id-1)
# There are no more tweets
    if (len(more_tweets) == 0):
        break
    else:
        last_id = more_tweets[-1].id-1
        tweets = tweets + more_tweets

media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

count = 0

for media_file in media_files:
    if count >= 10:
        break
    count = count + 1

    try:
        wget.download(media_file)
    except:
        pass

point = 0
numlist = "0123456789"
for file in os.listdir('.'):
    if file.endswith('jpg') or file.endswith('png'):
        
        
        new_name = numlist[point]+'.jpg'
        print(new_name)
        os.rename(file, new_name)
        point = point+1

subprocess.call("ffmpeg -framerate 1 -i %d.jpg output.mp4",shell=True)

# Instantiates a client
client = vision.ImageAnnotatorClient()

pathDir =  os.listdir('/home/ec602/Desktop/twitter')

f = open('/home/ec602/Desktop/twitter/labels.txt','w+')

for file in pathDir:
    if file.endswith('jpg'):
        with io.open(file,'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations

        print('Labels:')
        f.write("Labels:"+"\n")



        for label in labels:
            print(label.description)

            f.write(label.description+"\n")
f.close()
