"""
Created on Fri Nov  6 14:12:23 2020
@author: mohamedkhaled
project name: Twitter Bot - On This Day

"""

from requests import get
import tweepy
import json
import datetime
from time import sleep

# facts api connection

reqheader = {
    'x-rapidapi-key': "62dc246400msh752bd4bfd1c78e0p13c8cdjsnaef91be599fb",
    'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }

querystring = {"fragment" : "True", "json": "True"}

#twitter connection

TWauth = tweepy.OAuthHandler("********************",
                           "*****************")

TWauth.set_access_token("***********************", 
                      "******************")

hashtags = '#thisdaybot #factoftoday'

def timeaware():
    
    dateaware = datetime.datetime.now()
    
    _day = dateaware.day
    _month = dateaware.month
    _year = dateaware.year
    
    return(_day,_month,_year)

def urlconstruct(day,month):
    
        queryurl = f"https://numbersapi.p.rapidapi.com/{month}/{day}/date"
        
        return(queryurl)

def factgetter(url): 
    
    response = get( url, headers= reqheader, params = querystring)
    
    res_obj = json.loads(response.text)
    
    return(res_obj)

def Tweetconstructor(factobj, curry):
    
    tweettext = factobj["text"]
    factyear = int(factobj["year"])
    
    if factyear < 0:
        
        tweetage = "On this day " + str(factyear).lstrip('-') + ' BC, '
        
    else:
        
        tweetage = 'On this day ' + str(int(curry) - int(factyear)) + ' years ago, '
        
    return({'tweet' : tweettext, 'age': tweetage})
    
def Tweet(tweetobj):
    
    api = tweepy.API(TWauth)
    
    tweettext = tweetobj['age'] + tweetobj['tweet'] + '.' + hashtags
    
    api.update_status(tweettext)

    
if __name__ == "__main__":
    
    while True:
        
        TriggerTime = "20:45"
                
        now = datetime.datetime.now()

        reference = now.strftime("%H:%M")
        
        if reference == TriggerTime:
                
            _day, _month, _year = timeaware()
                
            url = urlconstruct(_day, _month) 
    
            fact = factgetter(url)
    
            tweetdata = Tweetconstructor(fact, _year)

            Tweet(tweetdata)
        
        sleep(60)
     