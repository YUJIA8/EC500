# EC500
This repository is for EC500

## Code Review for tweepyapi
Yujia's program can achieve the main functions of this task. By running this program, it can download 10 photos from a specific twitter ID by tweepy API, then transform them into a video by FFMPEG API, and get the characteristics of those pictures by Google Vision API. The code is clear and easy to read. And Yujia use the ten numbers(from 0 to 9) to name the pictures downloaded from the twitter. But there are still some problems.

1. The video you produced with pictures, some pictures in your video cannot maintain their original length-width ratio, instead, some of the pictures has changed their shape.

2. It's if thoughtful of you that you used "X" to remind the user to change those "X" parts into their own consumer_key, consumer_secret, access_key and access_secret. But I think you should also change this part of your code:
   ###### f = open('/home/ec602/Desktop/twitter/labels.txt','w+')
to something like:
   ###### f = open('/your/folder/path/labels.txt','w+')
to remind the users to change this part of code to their own folder path.

3. In a specific twitter, if there are more than one photo, then this program can only download the first photo, other photos will not be downloaded in the folder or be included in the video.
So the main call is asynchronous.

4. If I run the program again for the same twitter ID in the same folder, the new-downloaded-picture will cover the old ones if there are more than five photo-containing-twitters in that twitter ID.

5. If the twitter ID that the user want to use to run this program has more than 10 photo-containing-twitters, then the program will report an error:
###### Traceback (most recent call last):
######   File "twitter.py", line 77, in <module>
######     new_name = numlist[point]+'.jpg'
###### IndexError: string index out of range
which means that this program can only deal with twitter ID who contain less than 10 photo-containing-twitters.

## Unittest

For the unittest part, I wrote 3 unittest programs to test Yujia's mini project. 
The first test program, whose name is "UnitTest1.py", is to test whether the program have successfully created the ".mp4" video file. 
The second test program, whose name is "UnitTest2.py", is to test whether the program have successfully created the ".txt" document file to record the labels of the pictures using Google Vision API. 
The third test program, whose name is "UnitTest3.py", is to test the running time of the program.

As the result shows, Yujia's program can creat the ".mp4" video file which contain at most first 10 pictures in a specific twitter account so it passed the first test; and the program can use Google Vision API and record the labels in a ".txt" file; but the program cannot pass the third test because it runs not fast enough.  

## Web Application
