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
class NewsStory(object):
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
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def is_phrase_in(self, text):

        no_punct_text = ''.join(ch if ch not in string.punctuation else ' ' for ch in text.upper())
        cleaned_text = ' '.join(no_punct_text.split()) + ' '
        no_punct_phrase = ''.join(ch if ch not in string.punctuation else ' '
                                  for ch in self.phrase.upper())
        cleaned_phrase = ' '.join(no_punct_phrase.split()) + ' '

        if cleaned_phrase not in cleaned_text:
            return False
        else:
            return True

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())


# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, pubtime):

        pubtime = datetime.strptime(pubtime, '%d %b %Y %H:%M:%S')
        pubtime = pubtime.replace(tzinfo=pytz.timezone('EST'))
        self.pubtime = pubtime

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.get_pubdate().replace(tzinfo=pytz.timezone('EST')) < self.pubtime:
            return True
        else:
            return False

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.get_pubdate().replace(tzinfo=pytz.timezone('EST')) > self.pubtime:
            return True
        else:
            return False



# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)

    triggered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                triggered_stories.append(story)
    return triggered_stories



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
    trigger_dict = {}
    trigger_list = []

    for i in range (len(lines)):
        trigger = lines[i].split(',')
        if trigger[1] == 'TITLE':
            trigger_dict[trigger[0]] = TitleTrigger(trigger[2])
        elif trigger[1] == 'DESCRIPTION':
            trigger_dict[trigger[0]] = DescriptionTrigger(trigger[2])
        elif trigger[1] == 'AFTER':
            trigger_dict[trigger[0]] = AfterTrigger(trigger[2])
        elif trigger[1] == 'BEFORE':
            trigger_dict[trigger[0]] = BeforeTrigger(trigger[2])
        elif trigger[1] == 'NOT':
            trigger_dict[trigger[0]] = NotTrigger(trigger[2])
        elif trigger[1] == 'AND':
            trigger_dict[trigger[0]] = AndTrigger(trigger_dict[trigger[2]], trigger_dict[trigger[3]])
        elif trigger[0] == 'ADD':
            for x in range(1, len(trigger)):
                trigger_list.append(trigger_dict[trigger[x]])
    return trigger_list


    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll


if __name__ == '__main__':
    try:
        #t1 = TitleTrigger("election")
        #t2 = DescriptionTrigger("Trump")
        #t3 = DescriptionTrigger("Biden")
        #t4 = AndTrigger(t2, t3)
        #triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        triggerlist = read_trigger_config('triggers.txt')

        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                guidShown.append(newstory.get_guid())

        while True:


            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://feeds.bbci.co.uk/news/rss.xml")
            #http://news.google.com/news?output=rss

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

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

            #Dlist(map(get_cont, stories))
            #Dscrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)