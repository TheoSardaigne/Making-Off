#twite.py
#coding: utf-8

import csv
import json
import twitter
from accesstwit import APIkey, APIsecretkey, Token, Tokensecret 

fichier = "tweet.csv"

t = twitter.Api(consumer_key=APIkey,
	consumer_secret=APIsecretkey,
	access_token_key=Token,
	access_token_secret=Tokensecret,
	tweet_mode="extended"
	)

onCherche = input("vasymongars")

tweets = t.GetSearch(term = onCherche,count = 500,result_type = "recent",return_json = True)

print(json.dumps(tweets, indent=2, sort_keys=True))

h1 = "@le_Parisien"
h2 = "@20Minutes"
h3 = "@lobs"
h4 = "@LesEchos"
h5 = "@TV5MONDE"
h6 = "@Le_Soir3"
h7 = "@ARTEjournal"
h8 = "@LaTribune"
h9 = "@franceinfo"
h10 = "@FRANCE24"
h11 = "@rtlinfo"
h12 = "@Europe1"
h13 = "@RMCinfo"
h14 = "@franceinter"
h15 = "@Charlie_Hebdo"
h16 = "@LEXPRESS"
h17 = "@LePoint"
h18 = "@VICEfr"
h19 = "@radiofrance"
h20 = "@mdiplo"
h21 = "@Mediapart"
h22 = "@RTLFrance"
h23 = "@franceinfo"
h24 = "@lejdd"
h25 = "@RTenfrançais"

def getText(tweet):
    try: text = tweet['retweeted_status']['extended_tweet']['full_text']
    except:
          try: text = tweet['retweeted_status']['full_text']
          except:
        	    try: text = tweet['extended_tweet']['full_text']
                except:
            	      try: text = tweet['full_text']
                      except:
                	        try: text = tweet['retweeted_status']['text']
                            except:
                    	          try: text = tweet['text']
                                  except: 
                        	            text = ''
    return text

for tweet in tweets["statuses"]:
    cuicui=[]
	cuicui.append(tweet["created_at"])
	cuicui.append(getText(tweet))
	cuicui.append(tweet["user"]["name"])
	cuicui.append(tweet["id"])
	cuicui.append(tweet["retweet_count"])
	cuicui.append(tweet["favorite_count"])
	cuicui.append(tweet["lang"])
	cuicui.append(tweet["user"]["location"])




	print("Date/heure ", tweet["created_at"])
	#print("Contenu ", tweet["full_text"])
	print("IdUser: ", tweet["id"])
	print("Language: ", tweet["lang"])
	print("Location: ", tweet["user"]["location"])
    print("Pseudo ", tweet["user"]["name"])
	print("Retweets ", tweet["retweet_count"])
	print("P'tits coeurs ", tweet["favorite_count"])
	print("*"*60)
	
lebron = open(fichier,"a")
james = csv.writer(lebron)
james.writerow(tweet)