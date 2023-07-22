
#import feedparser
import string
#import time
#import threading
from content_processor_ps7 import Toot, get_text_content
from datetime import datetime
import pytz
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
    def __init__(self, content, account, user_id, hashtags, bookmark, no_replies, url, toot_id, count_replies, pubdate):
        self.content = content
        self.account = account
        self.user_id = user_id
        self.hashtag = hashtags
        self.bookmark = bookmark
        self.no_replies = no_replies
        self.url = url
        self.toot_id = toot_id
        self.count_replies = count_replies
        self.pubdate = pubdate

# hier könnte man alles was in "content_processor_ps7.py" ist implementieren lassen



# Problem 2

#======================
# Code for loading toots with specific hashtag from mastodon
# & put toots in objects dictionary
# and implement get_text_content
#======================

limit = 50

def load(hashtag):
    # load all toots with a specififc hashtag into a dictionary 
    toots = mastodon.timeline_hashtag(hashtag, limit=limit)
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
            count_replies = toot['replies_count'],
            pubdate = toot['created_at'] 
            # return value '2023-07-22 09:37:34+00:00' 
        )
        toots_dict.append(toot)
    return toots_dict



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
            pass


# Problem 2
# PhraseTrigger
# use string.punctuaion to
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def evaluate(self, text):
        text = text.content.lower()
        for letter in string.punctuation:
            clean_text = text.replace(letter, ' ')
        words = clean_text.split()
        single_phrase = self.phrase.split()
        #for m in single_phrase:
        #   for i, word in enumerate(words):
        #      if m == word:
        #         test.append(i)
        list_text = " ".join(words)
        list_trigger= " ".join(single_phrase)

        if list_trigger in list_text:
            return True
        else:
            return False

#class Content(PhraseTrigger):
 #   def evaluate(self, toot):
  #      content = toot.content
   #     return self.is_phrase_in(content)


# TIME TRIGGERS

# Problem 5
# TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, ptime):
        format = '%d %b %Y %H:%M:%S'
        ptime = datetime.strptime(ptime, format)
        ptime = ptime.replace(tzinfo=pytz.timezone("EST"))
        self.ptime = ptime


# Problem 6
# BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        clock = story.pubdate.replace(tzinfo=pytz.timezone("EST"))
        return self.ptime > clock

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        clock = story.pubdate.replace(tzinfo=pytz.timezone("EST"))
        return self.ptime < clock


#======================
# COMPOSITE TRIGGERS
#======================

# Problem 7
# NotTrigger

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        result = self.trigger.evaluate(story)
        return not result

# Problem 8
# AndTrigger

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        result1 = self.trigger1.evaluate(story)
        result2 = self.trigger2.evaluate(story)
        return result1 and result2


# Problem 9
# OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        result1 = self.trigger1.evaluate(story)
        result2 = self.trigger2.evaluate(story)
        return result1 or result2

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # Problem 10
    trigger_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                trigger_stories.append(story)
                break
    return trigger_stories


 
if __name__ == '__main__':

    dictionary = load('MoIN')
    gpt = PhraseTrigger(
        phrase = 'kiel'
    )
    ppt = PhraseTrigger(
        phrase = 'wetter'
    )
    not_filter = NotTrigger(
        trigger= ppt
    )
    and_filter = AndTrigger(
        trigger1= gpt,
        trigger2= not_filter
    )
    
    triggers = [ and_filter ]
    results = []
    #for i in range(35):     
       # result = gpt.is_phrase_in(dictionary[i].content)
        #if result:
          #  results.append(dictionary[i].content)
    probe = filter_stories(dictionary, triggers)
    for i in range(len(probe)):     
        print(probe[i].content)