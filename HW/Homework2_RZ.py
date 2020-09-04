# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:59:57 2020

@author: rzava
"""
from bs4 import BeautifulSoup
import urllib
import csv
import os
import io

#Set directory for file
os.chdir('E:/Academic/Summer/Python/Classes/Homework')


def allThesePs(pages):
    with io.open('RZ_scrape.csv', 'w', encoding="utf-8") as f:	#saving csv repository for data  
        w = csv.DictWriter(f, fieldnames = ("Title", "URL", "Number of signatures", "Over 100k signitures", "Issues", "Creator", "Published date"))
        w.writeheader()
        # 	Open the main website
        for i in range(0,pages):
            #taken from lab/lecture adding in page loop
            web_address = 'https://petitions.whitehouse.gov/?page=' + str(i)
            web_page = urllib.request.urlopen(web_address)
            # 	Parse it
            soup = BeautifulSoup(web_page.read())
            #Empty dictionary to index individual url's of petitions
            petition_dictionary = {}
            little_soup = soup.find_all('article')
            #taking all instances of article, and then deleting the first because it is not useful
            del little_soup[0]
            for l in range(0,20):
                #getting url tags
                tag_a = little_soup[l].find_all('a', href=True)
                #getting individual keys
                petition_dictionary["Title"] = tag_a[0].getText()
                #urls for each individual petition
                petition_dictionary["URL"] = "https://petitions.whitehouse.gov" + tag_a[0].get("href")
                #	"Number of signatures"
                tag_span = little_soup[l].find_all('span')
                petition_dictionary["Number of signatures"] = tag_span[1].getText ("signatures-number")
                #	"Over 100k signitures"
                petition_dictionary["Over 100k signitures"] = str(int((petition_dictionary["Number of signatures"]).replace(',', '')) >= 100000)
                #	"Issues"
                tag_h6 = little_soup[l].find_all('h6')
                h6_list = []
                for i in range(0,len(tag_h6)):
                    h6_list.append(tag_h6[i].getText())	
                    petition_dictionary["Issues"] = ", ".join(h6_list)
                    #	"Creator" and "Published date"
                    meta_soup = BeautifulSoup((urllib.request.urlopen(petition_dictionary["URL"])).read())  
                    tag_h4 = meta_soup.find_all('h4')[0]
                    petition_dictionary["Creator"] = (tag_h4.getText()).split(" on ")[0][len("Created by "):] 
                    petition_dictionary["Published date"] = (tag_h4.getText()).split(" on ")[1] 
                    w.writerow(petition_dictionary)




#Running function over first three pages
allThesePs(3)#60 entries, so something worked