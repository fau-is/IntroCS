
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
    def __init__(self, content, account, user_id, hashtags, bookmark, no_replies, url, toot_id, count_replies, pubdate, mentions, media, language, poll):
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
        self.mentions = mentions
        self.media = media
        self.language = language
        self.poll = poll

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
            pubdate = toot['created_at'],
            mentions = toot['mentions'],
            media = toot['media_attachments'],
            language = toot['language'], 
            poll = toot['poll'] 
            # return value '2023-07-22 09:37:34+00:00' %Y-%b-%d  %H:%M:%S'
        )
        toots_dict.append(toot)
    return toots_dict



#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, toot):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# Problem 3

class MediaTrigger(Trigger):
    def evaluate(self, toot):
        media = toot.media
        if media:
            return True 
        return False
    
class LanguageTrigger(Trigger):
    def __init__(self, language):
        self.language = language
        
    def evaluate(self, toot):
        langu = toot.language
        if self.language ==langu:
            return True 
        return False
    
class PollTrigger(Trigger):
    def evaluate(self, toot):
        poll = toot.poll
        if poll:
            return True 
        return False
    
class MentionsTrigger(Trigger):
    def evaluate(self, toot):
        mentions = toot.mentions
        if mentions:
            return True 
        return False


# Problem 2
# PhraseTrigger
# use string.punctuaion to
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def evaluate(self, toot):
        text = toot.content.lower()
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
        format = '%Y-%m-%d %H:%M:%S'
        ptime = datetime.strptime(ptime, format)
        ptime = ptime.replace(tzinfo=pytz.timezone("EST"))
        self.ptime = ptime


# Problem 6
# BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, toot):
        clock = toot.pubdate.replace(tzinfo=pytz.timezone("EST"))
        return self.ptime > clock

class AfterTrigger(TimeTrigger):
    def evaluate(self, toot):
        clock = toot.pubdate.replace(tzinfo=pytz.timezone("EST"))
        return self.ptime < clock


#======================
# COMPOSITE TRIGGERS
#======================

# Problem 7
# NotTrigger

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, toot):
        result = self.trigger.evaluate(toot)
        return not result

# Problem 8
# AndTrigger

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, toot):
        result1 = self.trigger1.evaluate(toot)
        result2 = self.trigger2.evaluate(toot)
        return result1 and result2


# Problem 9
# OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, toot):
        result1 = self.trigger1.evaluate(toot)
        result2 = self.trigger2.evaluate(toot)
        return result1 or result2

#======================
# Filtering
#======================

# Problem 10
def filter_toots(toots, triggerlist):
    """
    Takes in a list of Toot instances.

    Returns: a list of only the toots for which a trigger in triggerlist fires.
    """
    # Problem 10
    trigger_toots = []
    for toot in toots:
        for trigger in triggerlist:
            if not trigger.evaluate(toot):
                break
            
        trigger_toots.append(toot)
    return trigger_toots


 
if __name__ == '__main__':
    
    #first hashtag is already a filter (kind of)
    hashtag = 'ChatGPT'
    dictionary = load(hashtag)
    
    ai = PhraseTrigger(
        phrase = 'AI'
    )
    ki = PhraseTrigger(
        phrase = 'KI'
    )
    university = PhraseTrigger(
        phrase = 'university'
    )
    application = PhraseTrigger(
        phrase = 'application'
    )
    not_filter = NotTrigger(
        trigger= university
    )
    or_filter = OrTrigger(
        trigger1= ai,
        trigger2= ki
    )

    media_filter = MediaTrigger()
    not_media = NotTrigger(
        trigger= media_filter
    )
    
    language_de = LanguageTrigger(
        language= 'de'
    )
    language_en = LanguageTrigger(
        language= 'en'
    )
    or_language = OrTrigger(
        trigger1= language_de,
        trigger2= language_en
    )
    
    mentions_filter = MentionsTrigger()
    poll_filter = PollTrigger()
    
    before_filter = BeforeTrigger(
        ptime= '2023-07-14 13:23:05'
    )
    after_filter = AfterTrigger(
        ptime= '2023-07-14 13:23:05'
    )
    
    
    triggers = [ or_filter, not_filter, not_media,  after_filter ]

    probe = filter_toots(dictionary, triggers)
    for i in range(len(probe)): 
   
        print(probe[i].content)