#!python3
# -*- coding: cp1252 -*-

from twitter import *
import json
import re
import threading
from queue import Queue
import time

modi_text = []

def twitterauth():
    global t
    t= Twitter(
            auth=OAuth("Access Credentials Here All the secrets")
           )
    
    print("Object Initialized ",t)

def Stats():
    username = "krishnakalyan3"
    print(username, "User Stats")
    Following = t.friends.ids(screen_name = username)
    Count_Following=len(Following["ids"])
    print("Number of Following", )
    Followers = t.followers.ids(screen_name = username)
    Count_Followers=len(Followers["ids"])
    print("No of Followers",Count_Followers)

def trends():
    trends_india = t.trends.place(_id="2295420")
    for i in trends_india:
        for b in i['trends']:
            print(b['name'])

def search():
    global modi_text
##    modi = t.search.tweets(q="modi",result_type='recent',language='en')
    modi = t.search.tweets(q="modi",result_type='recent', count=100,language='en')
    for i in modi['statuses']:
        modi_text.append(i['text'])
    

def writetofile():
    text_file = open("C:\\Users\\saikrishnak\\Desktop\\write.txt", "a",encoding='utf-8')
    for tweets in modi_text:
        print(tweets)
        text_file.write(tweets)
        text_file.write('\n')
    text_file.close()
    print("# of Tweets Captured ",len(modi_text))

def Political_Search():
    Congress = t.search.tweets(q="congress",result_type='recent', count=1)
    for b in Congress['statuses']:
        print(b['text'])
    BJP = t.search.tweets(q="bjp",result_type='recent', count=1)
    for b in BJP['statuses']:
        print(b['text'])
    AAP = t.search.tweets(q="AAP",result_type='recent', count=1)
    for b in AAP['statuses']:
        print(b['text'])

if __name__ == '__main__':   
    twitterauth()
    search()
    writetofile()
##    Stats()
##    trends()
##    Political_Search()
    
    
    

