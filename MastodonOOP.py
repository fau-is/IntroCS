
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
    client_id="SOXp3afnWgFJrQf2_UIlqgPva--ZhdBZHS9fyik8Rvg",
    client_secret="HW8bhQJlzAx1eGmLGUvK-qxi4ej8QRDylPFro0El6To",
    access_token="eJpW5z5P82AYIHSzcd6oeHEPaSrP4SMGYn_nxoICLEE",
    api_base_url="https://mastodon.social"
)



#======================
# Global variables & functions
#======================

# Problem 1 

# TODO: Object Toot
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


# Problem 2

# TODO: get_text_content (global function)
def get_text_content(toot):
    content_html = toot['content']
    soup = BeautifulSoup(content_html, 'html.parser')
    content_text = soup.get_text()
    return content_text


#======================
# Loading
#======================

# Problem 3

# TODO: Load function
def load(hashtag):
    # empty dictionary for loaded toots
    toots_dict = []
    
    # Load all toots with a specific hashtag into a dictionary, limit to 100 toots
    toots = mastodon.timeline_hashtag(hashtag, limit=10)
    
    # Process the retrieved toots
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
    
    # return toot dictionary
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



# MEDIA TRIGGERS

# Problem 4

# TODO: MediaTrigger
class MediaTrigger(Trigger):
    def evaluate(self, toot):
        media = toot.media
        if media:
            return True 
        return False
    
# Problem 5

# TODO: ImageMediaTrigger
class ImageMediaTrigger(MediaTrigger):
    def evaluate(self, toot):
        media = toot.media
        for content in media:
            if content["type"] == "image":
                return True
        return False

# Problem 6

# TODO: VideoMediaTrigger
class VideoMediaTrigger(MediaTrigger):
    def evaluate(self, toot):
        media = toot.media
        for content in media:
            if content["type"] == "video": #hier TypeError: string indices must be integers, not 'str', mit [1] hat es gelaufen, aber falsches ergebnis rausgekommen  
                return True
        return False

# Problem 7

# TODO: GifMediaTrigger
class GifMediaTrigger(MediaTrigger):
    def evaluate(self, toot):
        media = toot.media
        for content in media:
            if content["type"] == "gifv":
                return True
        return False

# Problem 8

# TODO: AudioMediaTrigger
class AudioMediaTrigger(MediaTrigger):
    def evaluate(self, toot):
        media = toot.media
        for content in media:
            if content["type"] == "audio":
                return True
        return False
    
# Problem 9

# TODO: LanguageTrigger
class LanguageTrigger(Trigger):
    def __init__(self, language):
        self.language = language
        
    def evaluate(self, toot):
        langu = toot.language
        if self.language == langu:
            return True 
        return False
    
# Problem 10

# TODO: PollTrigger
class PollTrigger(Trigger):
    def evaluate(self, toot):
        poll = toot.poll
        if poll:
            return True 
        return False
    
# Problem 11

# TODO: MentionsTrigger
class MentionsTrigger(Trigger):
    def evaluate(self, toot):
        mentions = toot.mentions
        if mentions:
            return True 
        return False


# Problem 12

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def evaluate(self, toot):
        text = toot.content.lower()
        for letter in string.punctuation:
            clean_text = text.replace(letter, ' ')
        words = clean_text.split()
        single_phrase = self.phrase.split()         #Ist Zeile 182 bis 186 nötig? Teilen wir hier nicht alles, nur um es dann wieder
                                                    #zusammenzusetzen? --> ja sieht so aus. Ich wollte es auskommentiert mal runnen, 
                                                    #aber hab die xlsx libraries nicht installiert, kannst du aj evtl. bitte mal machen
        list_text = " ".join(words)
        list_trigger= " ".join(single_phrase)

        if list_trigger in list_text:
            return True
        else:
            return False



# TIME TRIGGERS

# Problem 13

# TODO: TimeTrigger
class TimeTrigger(Trigger):
    def __init__(self, ptime):
        format = '%Y-%m-%d %H:%M:%S'
        ptime = datetime.strptime(ptime, format)
        ptime = ptime.replace(tzinfo=pytz.timezone("EST"))
        self.ptime = ptime


# Problem 14

# TODO: BeforeTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, toot):
        clock = toot.pubdate.replace(tzinfo=pytz.timezone("EST"))
        return self.ptime > clock

# Problem 15

# TODO: AfterTrigger
class AfterTrigger(TimeTrigger):
    def evaluate(self, toot):
        clock = toot.pubdate.replace(tzinfo=pytz.timezone("EST"))
        return self.ptime < clock


#======================
# COMPOSITE TRIGGERS
#======================

# Problem 16

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, toot):
        result = self.trigger.evaluate(toot)
        return not result

# Problem 17

# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, toot):
        result1 = self.trigger1.evaluate(toot)
        result2 = self.trigger2.evaluate(toot)
        return result1 and result2


# Problem 18

# TODO: OrTrigger
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

# Problem 19

# TODO: Filter_toots
def filter_toots(toots, triggerlist):
    """
    Takes in a list of Toot instances.

    Returns: a list of only the toots for which a trigger in triggerlist fires.
    """
    trigger_toots = []
    for toot in toots:
        all_true = True
        for trigger in triggerlist:
            if not trigger.evaluate(toot):
                all_true = False
        if all_true:
            trigger_toots.append(toot)

    return trigger_toots


#======================
# Loading into Excel 
#======================

# Problem 19

# Load_to_workbook
def load_to_workbook(dictionary):
    # Load the existing workbook
    workbook = load_workbook('objects.xlsx')

    # Choose the existing worksheet you want to write data into
    worksheet = workbook['Sheet1']  # Replace 'Sheet1' with the actual sheet name

    # Get the data in 'probe' list and write it to the existing worksheet
    for row, toot in enumerate(dictionary, 2):  # Start from row 2 to avoid overwriting the headers
        worksheet.cell(row=row, column=1, value=toot.account["username"])
        worksheet.cell(row=row, column=2, value=toot.pubdate.replace(tzinfo=None))
        worksheet.cell(row=row, column=3, value=toot.content)

    # Save the modified workbook
    workbook.save('objects.xlsx')
    return 


 
if __name__ == '__main__':
    
    #Use your load function to load all toots by a specified hashtag
    hashtag = 'SMS'
    dictionary = load(hashtag)
    
    ai = PhraseTrigger(
        phrase = 'Sonne Mond Sterne'
    )
    ki = PhraseTrigger(
        phrase = 'Ticket'
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

    image_media_filter = ImageMediaTrigger()
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
    
    
    triggers = [ ai, ki, language_de ]

    filtered_toots = filter_toots(dictionary, triggers)
    load_to_workbook(filtered_toots)



        