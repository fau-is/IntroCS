
#import feedparser
import string
#import time
#import threading
from content_processor_ps7 import Toot, get_text_content
#from datetime import datetime
#import pytz
from mastodon import Mastodon

mastodon = Mastodon(
    client_id="SOXp3afnWgFJrQf2_UIlqgPva--ZhdBZHS9fyik8Rvg",
    client_secret="HW8bhQJlzAx1eGmLGUvK-qxi4ej8QRDylPFro0El6To",
    access_token="eJpW5z5P82AYIHSzcd6oeHEPaSrP4SMGYn_nxoICLEE",
    api_base_url="https://mastodon.social"
)



#-----------------------------------------------------------------------

#======================
# Data structure design
#======================

# Problem 1 

class Toot:
    def __init__(self, content, account, user_id, hashtags, bookmark, no_replies, url, toot_id, count_replies):
        self.content = content
        self.account = account
        self.user_id = user_id
        self.hashtag = hashtags
        self.bookmark = bookmark
        self.no_replies = no_replies
        self.url = url
        self.toot_id = toot_id
        self.count_replies = count_replies

# hier könnte man alles was in "content_processor_ps7.py" ist implementieren lassen



# Problem 2

#======================
# Code for loading toots with specific hashtag from mastodon
# & put toots in objects dictionary
#======================

def load(url):
    # load all toots with a specififc hashtag into a dictionary 
    hashtag = "Moin" 
    toots = mastodon.timeline_hashtag(hashtag, limit=5)
    toots_dict = []
    # Process and print the retrieved toots
    for toot in toots:
        content_text = get_text_content(toot)
        toot = Toot(
            account = toot['account'],
            toot_id = toot['id'],
            content = content_text,
            user_id = toot['account']['id'],
            hashtags = toot['tags'],
            bookmark = toot['bookmarked'],
            no_replies = toot['replies_count'],
            url = toot['url'],
            count_replies = toot['replies_count']    
        )
        toots_dict.append(toot)



#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# Problem 3

class Media(Trigger):
    def __init__(self, toot_id):
        self.phrase = toot_id

    def is_phrase_in(self, text):
        
            return False





#======================
# COMPOSITE TRIGGERS
#======================

# Problem 7
# NotTrigger

class NotTrigger(Trigger):
    def __init__(self, T):
        self.T = T

    def evaluate(self, story):
        result = self.T.evaluate(story)
        return not result

# Problem 8
# AndTrigger

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trig1 = trigger1
        self.trig2 = trigger2

    def evaluate(self, story):
        result1 = self.trig1.evaluate(story)
        result2 = self.trig2.evaluate(story)
        return result1 and result2


# Problem 9
# OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trig1 = trigger1
        self.trig2 = trigger2

    def evaluate(self, story):
        result1 = self.trig1.evaluate(story)
        result2 = self.trig2.evaluate(story)
        return result1 or result2

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
     pass
 
 if __name__ == '__main__':
     pass