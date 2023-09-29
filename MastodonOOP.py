
import string
from datetime import datetime
import pytz
from mastodon import Mastodon
from openpyxl import load_workbook
from bs4 import BeautifulSoup

#-----------------------------------------------------------------------

#======================
# Code for API access
# Get the different variables from your mastodon account
#======================

# Problem 0

mastodon = Mastodon(

)



#======================
# Global variables & functions
#======================

# Problem 1 

# TODO: Object Toot
class Toot:
    pass


# Problem 2

# TODO: get_text_content (global function)
def get_text_content(): pass


#======================
# Loading
#======================

# Problem 3

# TODO: Load function
def load():
    pass


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



# MEDIA TRIGGERS

# Problem 4

# TODO: MediaTrigger
class MediaTrigger():
    pass


# Problem 5

# TODO: ImageMediaTrigger
class ImageMediaTrigger():
    def evaluate():
        pass

# Problem 6

# TODO: VideoMediaTrigger
class VideoMediaTrigger():
    def evaluate():
        pass

# Problem 7

# TODO: GifMediaTrigger
class GifMediaTrigger():
    def evaluate():
        pass

# Problem 8

# TODO: AudioMediaTrigger
class AudioMediaTrigger():
    def evaluate():
        pass
    
# Problem 9

# TODO: LanguageTrigger
class LanguageTrigger():
    def __init__():
        pass
        
    def evaluate(self, toot):
        pass
    
    
# Problem 10

# TODO: PollTrigger
class PollTrigger():
    def evaluate():
        pass
    
# Problem 11

# TODO: MentionsTrigger
class MentionsTrigger():
    def evaluate():
        pass


# Problem 12

# TODO: PhraseTrigger
class PhraseTrigger():
    def __init__():
        pass

    def evaluate(self, toot):
        pass



# TIME TRIGGERS

# Problem 13

# TODO: TimeTrigger
class TimeTrigger():
    def __init__():
        pass


# Problem 14

# TODO: BeforeTrigger
class BeforeTrigger():
    def evaluate(s):
        pass
    
    
# Problem 15

# TODO: AfterTrigger
class AfterTrigger():
    def evaluate():
        pass


#======================
# COMPOSITE TRIGGERS
#======================

# Problem 16

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__():
        pass

    def evaluate():
        pass

# Problem 17

# TODO: AndTrigger
class AndTrigger():
    def __init__():
        pass

    def evaluate():
        pass

# Problem 18

# TODO: OrTrigger
class OrTrigger():
    def __init__():
        pass

    def evaluate():
        pass

#======================
# Filtering
#======================

# Problem 19

# TODO: Filter_toots
def filter_toots():
    """
    Takes in a list of Toot instances.

    Returns: a list of only the toots for which a trigger in triggerlist fires.
    """
    pass


#======================
# Loading into Excel 
#======================

# Problem 20
# TODO: Load_to_workbook
def load_to_workbook(dictionary, workbook):
    # Load the existing workbook
    
    # Choose the existing worksheet you want to write data into

    # Get the data in 'probe' list and write it to the existing worksheet

    # Save the modified workbook
    pass


 
if __name__ == '__main__':
    
    #Use your load function to load all toots by a specified hashtag
    pass