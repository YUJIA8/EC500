# EC500
This repository is for EC500

# Code Review for tweepyapi
Yujia's program can achieve the main functions of this task. By running this program, it can download 10 photos from a specific twitter ID by tweepy API, then transform them into a video by FFMPEG API, and get the characteristics of those pictures by Google Vision API. The code is clear and easy to read. But there are still some problems.

1. The video you produced with pictures, some pictures in your video cannot maintain their original length-width ratio, instead, some of the pictures has changed their shape.

2. It's if thoughtful of you that you used "X" to remind the user to change those "X" parts into their own consumer_key, consumer_secret, access_key and access_secret. But I think you should also change this part of your code:
    f = open('/home/ec602/Desktop/twitter/labels.txt','w+')
to something like:
    f = open('/your/folder/path/labels.txt','w+')
to remind the users to change this part of code to their own folder path.

3. In a specific twitter, if there are more than one photos, then this program can only download the first photo, other photos will not be downloaded in the folder or be included in the video.
So the main call is asynchronous.
