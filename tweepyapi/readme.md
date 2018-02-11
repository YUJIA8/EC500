Readme file for this tweepy api
===============================
This python file can help you download 10 photos from the twitter, choose whatever account you want.
It can also convert these 10 pictures to a video, the frame of the video is 1 fps.
What's more excited is that it can request a picture label description from the google vision API, and write the descriptions 
to a txt file.

Instructions:
============
1, Register a twitter app account and create a new app and get the consumer key, consumer secret, access key and the access
secret, and type them in this python file.<br>
2, You can change to any twitter account you want, the example here is from Ibrahimovich.<br>
3, To activate your google vision API credential, following the https://cloud.google.com/vision/docs/quickstart , download the
credential-keys json file, and export it in your environment.<br>
4, Run the python file. You better put the python file in an empty folder. And change the path you download the photos to the
path you want. The photos will be downloaded and an output.mp4 and a labels.txt will be created, which has the descriptions of
the 10 photos you downloaded one by one.<br>

Note:
====
Sometimes when the height or the width of the photos cannot be divided by 2, it will come up with an error. To be faster to solve this problem, just try again and download another set of photos, until it works, thx.

