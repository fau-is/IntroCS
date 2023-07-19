# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []

    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = ""
        try:
            description = translate_html(entry.description)
        except:
            description = translate_html(entry.title_detail)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        #newsStory = NewsStory(guid, title, description, link, pubdate)
        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory:
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


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

# PHRASE TRIGGERS

# Problem 2
# PhraseTrigger
# use string.punctuaion to
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        text = text.lower()
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

# Problem 3
# TitleTrigger
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        tit = story.get_title()
        return self.is_phrase_in(tit)

# Problem 4
# DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        descript = story.get_description()
        return self.is_phrase_in(descript)


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
        clock = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        return self.ptime > clock

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        clock = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        return self.ptime < clock

# COMPOSITE TRIGGERS

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


#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll


if __name__ == '__main__':
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        #t1 = TitleTrigger("election")
        #t2 = DescriptionTrigger("Trump")
        #t3 = DescriptionTrigger("Biden")
        #t4 = AndTrigger(t2, t3)
        #triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        #triggerlist = read_trigger_config('triggers.txt')s

        # HELPER CODE - you don't need to understand this!
        # Reads and writes Newsstories to stories.txt in specified format
        # Retrieves and filters the stories from the RSS feeds
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                guidShown.append(newstory.get_guid())

        while True:


            print("Polling . . .", end=' ')
            # Get stories from BBC's Top Stories RSS news feed
            stories = process("http://feeds.bbci.co.uk/news/rss.xml")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)


            #@ISMAMA
            file = open('stories.txt', 'w')
            for s in stories:
                file.write(s.title.strip())
                file.write("\n")
                for i in range(len(s.title)):
                    file.write("-")
                file.write("\n")
                file.write(s.description.strip())
                file.write("\n")
                file.write(s.link.strip())
                file.write("\n")
                file.write("_"*60)
                for s in range(2):
                    file.write("\n")
            file.close()

            #Do not uncomment these lines
            #Dlist(map(get_cont, stories))
            #Dscrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)