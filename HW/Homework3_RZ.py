# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:53:04 2020

@author: rzava
"""
import time
import operator
import importlib
import sys
import tweepy
#header for tweepy w/ api keys
sys.path.insert(0, 'E:\Academic\Summer\Python')
twitter = importlib.import_module('Twitter_API')
api = twitter.client

#initialize wustl polisci user
wustlPS = api.get_user('WUSTLPoliSci')
#list of all followers' ids
wustl_Follows = wustlPS.followers_ids()
#number of followers
for_the_gram = len(wustl_Follows)





#######   Find most active follower   ##########
#setup empty dictionary for statuses
follow_Status = {}
#for loop to get status count for each user, then adding to dictionary
for i in range(0,for_the_gram):
    n = api.get_user(wustl_Follows[i]).statuses_count
    follow_Status[wustl_Follows[i]] = n

#get max statuses  
soMuchID = max(follow_Status.items(), key = operator.itemgetter(1))[0]
print("@" + str(api.get_user(soMuchID).screen_name) + " has " 
      + str(follow_Status[soMuchID]) + " statuses.") 
## Answer: @tubuann_only has 109,785 statuses## 





#######   Find most followed follower   #########
#empty dictionary for followers' followers
follow_Follow = {}
#for loop to get followers count for each user, then adding to dictionary
for i in range(0,for_the_gram):
    n = api.get_user(wustl_Follows[i]).followers_count
    follow_Follow[wustl_Follows[i]] = n
    
#get max followers
popID = max(follow_Follow.items(), key = operator.itemgetter(1))[0]
print("@" + str(api.get_user(popID).screen_name) + " has " 
      + str(follow_Follow[popID]) + " followers.")
##Answer: @BrendanNyhan has 81163 followers.##





###########     Active friends    ##############
#empty lists for indexing popularity
laymen_FriendsID = []
expert_FriendsID = []
celebrity_FriendsID = []
#list of wustl friends
wustl_Friends = []
#pulled from stack exchange.  Creating list of friends 
for page in tweepy.Cursor(api.friends_ids, screen_name='WUSTLPoliSci').pages():
    wustl_Friends.extend(page)
    time.sleep(10)

#binning each friend based on follower count
#(This hit the rate limit on the first go)
for i in range(0,len(wustl_Friends)):
    if api.get_user(wustl_Friends[i]).followers_count < 100:
        laymen_FriendsID.append(wustl_Friends[i])
    elif api.get_user(wustl_Friends[i]).followers_count in range (100,1001):
        expert_FriendsID.append(wustl_Friends[i])
    elif api.get_user(wustl_Friends[i]).followers_count > 1000:
        celebrity_FriendsID.append(wustl_Friends[i])





#######   Find most active lay friend   ##########
#setup empty dictionary for statuses
layfriend_Status = {}
#for loop to get status count for each user, then adding to dictionary
for i in range(0,len(laymen_FriendsID)):
    #get statuses count
    n = api.get_user(laymen_FriendsID[i]).statuses_count
    #update dictionary
    layfriend_Status[laymen_FriendsID[i]] = n

#get max status entry
layFriendID = max(layfriend_Status.items(), key = operator.itemgetter(1))[0]
print("@" + str(api.get_user(layFriendID).screen_name) + " has " 
      + str(layfriend_Status[layFriendID]) + " statuses.") 
##Answer: @usmanfalalu1 has 1,445 statuses.##
        




#######   Find most active expert friend   ##########
#setup empty dictionary for statuses
expertfriend_Status = {}
#for loop to get status count for each user, then adding to dictionary
for i in range(0,len(expert_FriendsID)):
    #get statuses count
    n = api.get_user(expert_FriendsID[i]).statuses_count
    #update dictionary
    expertfriend_Status[expert_FriendsID[i]] = n

#get max status entry
exFriendID = max(expertfriend_Status.items(), key = operator.itemgetter(1))[0]
print("@" + str(api.get_user(exFriendID).screen_name) + " has " 
      + str(expertfriend_Status[exFriendID]) + " statuses.") 
##Answer: @prof_nokken has 12576 statuses.##





#######   Find most active celebrity friend   ##########
#setup empty dictionary for statuses
celebfriend_Status = {}
#for loop to get status count for each user, then adding to dictionary
for i in range(0,len(celebrity_FriendsID)):
    #get statuses count
    n = api.get_user(celebrity_FriendsID[i]).statuses_count
    #update dictionary
    celebfriend_Status[celebrity_FriendsID[i]] = n

#get max status entry
celebFriendID = max(celebfriend_Status.items(), key = operator.itemgetter(1))[0]
print("@" + str(api.get_user(celebFriendID).screen_name) + " has " 
      + str(celebfriend_Status[celebFriendID]) + " statuses.") 
##Answer: @nytimes has 406822 statuses.##
        




#######   Find most followed friend   #########
#empty dictionary for friends' followers
follow_Friends = {}
#for loop to get followers count for each user, then adding to dictionary
for i in range(0,len(wustl_Friends)):
    n = api.get_user(wustl_Friends[i]).followers_count
    follow_Friends[wustl_Friends[i]] = n
    
#get max followers
popID = max(follow_Friends.items(), key = operator.itemgetter(1))[0]
print("@" + str(api.get_user(popID).screen_name) + " has " 
      + str(follow_Friends[popID]) + " followers.")
##Answer: @BarackObama has 122389479 followers.##





#######    Followers and their Followers being active   ########
#set up followers and followers of followers list
follows_Follow_Follows = wustl_Follows
#I'm going to throw up
for i in range(0, for_the_gram):
    try:
        follows_Follow_Follows.append(api.get_user(wustl_Follows[i]).followers_ids())
        time.sleep(10)
        #Damn tweeperrors
        if len(follows_Follow_Follows) % 100 == 0:
            print(str(len(follows_Follow_Follows)))
        else:
            continue
    except tweepy.TweepError as e:
        print("API call to get follower ids failed: " + str(e.reason) + " Skipping this user.")
    
#setup empty dictionary for statuses
followfollow_Status = {}
#for loop to get status count for each user, then adding to dictionary
for i in range(0,len(follows_Follow_Follows)):
    try:
        #get statuses count
        n = api.get_user(follows_Follow_Follows[i]).statuses_count
        #update dictionary
        followfollow_Status[follows_Follow_Follows[i]] = n
        #Because this takes so long, I'd like to know how far along I am 
        #if loop to print how many entries we have every 100 entries
        if len(followfollow_Status.keys()) % 100 == 0:
            print(str(len(followfollow_Status.keys())))
        else:
            continue
    #Damn tweeperrors
    except tweepy.TweepError as e:
        print("API call to get follower ids failed: " + str(e.reason) + " Skipping this user.")
#get max status entry
followFollowPopID = max(followfollow_Status.items(), key = operator.itemgetter(1))[0]
print("@" + str(api.get_user(followFollowPopID).screen_name) + " has " 
      + str(followfollow_Status[followFollowPopID]) + " statuses.")     
 ##Answer: @tubuann_only has 109826 statuses.##




#######   Followers and their friends being active   ##########
follows_Friends_Follows = wustl_Follows
#Following that line, I threw up
for i in range(0, for_the_gram):
    try:
        for page in tweepy.Cursor(api.friends_ids, screen_name= api.get_user(wustl_Follows[i]).screen_name).pages():
            follows_Friends_Follows.extend(page)
            #time.sleep(10)            
    except tweepy.TweepError as e:
            print("API call to get follower ids failed: " + str(e.reason) + " Skipping this user.")
    
friendfollow_Status = {}
#for loop to get status count for each user, then adding to dictionary
for i in range(0,len(follows_Friends_Follows)):
    try:
        #get statuses count
        n = api.get_user(follows_Friends_Follows[i]).statuses_count
        #update dictionary
        friendfollow_Status[follows_Friends_Follows[i]] = n
        #Because this takes so long, I'd like to know how far along I am 
        #if loop to print how many entries we have every 100 entries
        if len(friendfollow_Status.keys()) % 100 == 0:
            print(str(len(followfollow_Status.keys())))
        else:
            continue
    except tweepy.TweepError as e:
        print("API call to get follower ids failed: " + str(e.reason) + " Skipping this user.")
    
#get max status entry
friendFollowPopID = max(friendfollow_Status.items(), key = operator.itemgetter(1))[0]
print("@" + str(api.get_user(friendFollowPopID).screen_name) + " has " 
      + str(friendfollow_Status[followFollowPopID]) + " statuses.")
##I ran my code poorly over the past 4 days, and so did not have enough time to get this 
##answer.  The code looks correct, it just takes hours to run and keeps getting interrupted.