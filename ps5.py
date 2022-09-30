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


# Problem 3
# TODO: TitleTrigger


# Problem 4
# TODO: DescriptionTrigger


# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.


# Problem 6
# TODO: BeforeTrigger and AfterTrigger


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger


# Problem 8
# TODO: AndTrigger


# Problem 9
# TODO: OrTrigger

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
    return stories



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