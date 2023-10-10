import unittest
import MastodonOOPsolution
from mastodon import Mastodon
from bs4 import BeautifulSoup
import openpyxl
import os
import datetime


def get_text_content(toot):
    content_html = toot['content']
    soup = BeautifulSoup(content_html, 'html.parser')
    content_text = soup.get_text()
    return content_text


class Test_Mastodon(unittest.TestCase):
    
    def setUp(self):
        self.toot_true = MastodonOOPsolution.Toot (
            account = [{"id": 123, "username": "Marco"}],
            toot_id = True,
            content = '<p>Hello from Python, dog</p>',
            user_id = True,
            hashtags = [{'name': 'dog', 'url': True, 'history': ''}],
            bookmark = True,
            no_replies = True,
            url = True,
            count_replies = True,
            pubdate = "2022-07-22 09:37:34",
            mentions = True,
            media = [{"id": 123,"type":"image"},
                     {"id": 1234,"type":"video"},
                     {"id": 12345,"type":"gifv"},
                     {"id": 123456,"type":"audio"},
                     {"id": 1234567,"type":"unknown"} 
                     ],
            language = 'en',
            poll = True        
        )
        self.toot_false = MastodonOOPsolution.Toot (
            account = '',
            toot_id = '',
            content = 'sun',
            user_id = '',
            hashtags = '',
            bookmark = '',
            no_replies = '',
            url = '',
            count_replies = '',
            pubdate = '',
            mentions = False,
            media = '',
            language = '',
            poll = False        
        )
        
        self.toot_before = MastodonOOPsolution.Toot (
            account = [{"id": 123, "username": "Marco"}],
            toot_id = True,
            content = 'dog',
            user_id = True,
            hashtags = True,
            bookmark = True,
            no_replies = True,
            url = True,
            count_replies = True,
            pubdate = '2022-07-22 09:37:34+00:00' ,
            mentions = True,
            media = [{"id": "123","type":"image"}],
            language = 'en',
            poll = True        
        )

        self.toot_before.pubdate = datetime.datetime.strptime(self.toot_before.pubdate, "%Y-%m-%d %H:%M:%S%z")

        self.toot_after = MastodonOOPsolution.Toot (
            account = '',
            toot_id = '',
            content = 'sun',
            user_id = '',
            hashtags = '',
            bookmark = '',
            no_replies = '',
            url = '',
            count_replies = '',
            pubdate = '2024-07-22 09:37:34+00:00' ,
            mentions = '',
            media = '',
            language = '',
            poll = ''        
        )
        self.toot_after.pubdate = datetime.datetime.strptime(self.toot_after.pubdate, "%Y-%m-%d %H:%M:%S%z")

        
        self.clock = '2023-07-22 09:37:34+00:00'
    
    def tearDown(self):
        pass
    

    def test_API(self):
        self.assertIsInstance(MastodonOOPsolution.mastodon, Mastodon)
        # KP ob das so klappt
        # --> hier wird kein Error angegeben


    def test_Toot(self):        
        self.assertTrue(hasattr(self.toot_true, "content"))
        self.assertTrue(hasattr(self.toot_true, "account"))
        self.assertTrue(hasattr(self.toot_true, "toot_id"))
        self.assertTrue(hasattr(self.toot_true, "user_id"))
        self.assertTrue(hasattr(self.toot_true, "hashtags"))
        self.assertTrue(hasattr(self.toot_true, "bookmark"))
        self.assertTrue(hasattr(self.toot_true, "no_replies"))
        self.assertTrue(hasattr(self.toot_true, "url"))
        self.assertTrue(hasattr(self.toot_true, "count_replies"))
        self.assertTrue(hasattr(self.toot_true, "pubdate"))
        self.assertTrue(hasattr(self.toot_true, "mentions"))
        self.assertTrue(hasattr(self.toot_true, "media"))
        self.assertTrue(hasattr(self.toot_true, "language"))
        self.assertTrue(hasattr(self.toot_true, "poll"))


    def test_load(self):
        toots_dict = []
        hashtag = "Moin"
        mastodon = Mastodon(
            client_id="SOXp3afnWgFJrQf2_UIlqgPva--ZhdBZHS9fyik8Rvg",
            client_secret="HW8bhQJlzAx1eGmLGUvK-qxi4ej8QRDylPFro0El6To",
            access_token="eJpW5z5P82AYIHSzcd6oeHEPaSrP4SMGYn_nxoICLEE",
            api_base_url="https://mastodon.social"
        )
        # Load all toots with a specific hashtag into a dictionary, limit to 10 toots
        toots = mastodon.timeline_hashtag(hashtag, limit=10)
        result = MastodonOOPsolution.load(hashtag)

        # Process the retrieved toots
        for toot in toots:
            content_text = get_text_content(toot)
            toot = MastodonOOPsolution.Toot(
                account = toot['account'],
                toot_id = toot['id'],
                content = content_text,
                user_id = toot['account']['id'],
                hashtags = toot['tags'],
                bookmark = toot['bookmarked'],
                no_replies = toot['reblogs_count'],
                url = toot['url'],
                count_replies = toot['replies_count'],
                pubdate = toot['created_at'],
                mentions = toot['mentions'],
                media = toot['media_attachments'],
                language = toot['language'], 
                poll = toot['poll'] 
            )
            toots_dict.append(toot)

        for toot in result:
            # Extract the toot_id from the current Toot object
            toot_id = toot.toot_id

            # Check if the toot_id is present in toots_dict
            self.assertTrue(any(toot_id == t.toot_id for t in toots_dict))

        for toot in toots_dict:
        # Extract the toot_id from the current Toot object
            toot_id = toot.toot_id

        # Check if the toot_id is present in result (at least once)
            self.assertTrue(any(toot_id == t.toot_id for t in result))
            
        # AssertionError: Lists differ: [<Mas[23 chars] 0x111decb90>, <MastodonOOPsolution.Toot object at 0x1[341 chars]d10>] != [<Mas[23 chars] 0x114c42490>]


    def test_GetTextContent(self):
        text = 'Hello from Python, dog'
        text_content = MastodonOOPsolution.get_text_content(self.toot_true)
        self.assertEqual(text, text_content)
        
    def test_MediaTrigger(self):
        media = MastodonOOPsolution.MediaTrigger()
        
        self.assertTrue(media.evaluate(self.toot_true))
        self.assertFalse(media.evaluate(self.toot_false))
            
    def test_ImageMediaTrigger(self):
        video = MastodonOOPsolution.ImageMediaTrigger()
        
        self.assertTrue(video.evaluate(self.toot_true))
        self.assertFalse(video.evaluate(self.toot_false))

    def test_VideoMediaTrigger(self):
        video = MastodonOOPsolution.VideoMediaTrigger()
        
        self.assertTrue(video.evaluate(self.toot_true))   
        self.assertFalse(video.evaluate(self.toot_false))
        
    def test_GifMediaTrigger(self):
        gif = MastodonOOPsolution.GifMediaTrigger()
        
        self.assertTrue(gif.evaluate(self.toot_true))   
        self.assertFalse(gif.evaluate(self.toot_false))
        
    def test_AudioMediaTrigger(self):
        audio = MastodonOOPsolution.AudioMediaTrigger()
        
        self.assertTrue(audio.evaluate(self.toot_true))   
        self.assertFalse(audio.evaluate(self.toot_false))
        
    def test_LanguageTrigger(self):
        english = MastodonOOPsolution.LanguageTrigger("en")
        
        self.assertTrue(english.evaluate(self.toot_true))
        self.assertFalse(english.evaluate(self.toot_false))  
    
    def test_PollTrigger(self):
        poll_filter = MastodonOOPsolution.PollTrigger()
        
        self.assertTrue(poll_filter.evaluate(self.toot_true))
        self.assertFalse(poll_filter.evaluate(self.toot_false))
        
    def test_MentionsTrigger(self):
        mentions = MastodonOOPsolution.MentionsTrigger()
        
        self.assertTrue(mentions.evaluate(self.toot_true))
        self.assertFalse(mentions.evaluate(self.toot_false))
        
    def test_PhraseTrigger(self):
        phrase = MastodonOOPsolution.PhraseTrigger("dog")
        
        self.assertTrue(phrase.evaluate(self.toot_true))
        self.assertFalse(phrase.evaluate(self.toot_false))
        
        
    def test_TimeTrigger(self):
        formatted_time = datetime.datetime.strptime('2023-07-22 09:37:34-05:00', "%Y-%m-%d %H:%M:%S%z")
        triggered_time = MastodonOOPsolution.TimeTrigger(self.clock)
        
        self.assertEqual(triggered_time.ptime, formatted_time)
        # Chat gpt vorschlag isoformat() nach ptime
        # ValueError: unconverted data remains: +00:00 (behoben)
        # AssertionError: datetime.datetime(2023, 7, 22, 9, 37, 34, tzinfo=<StaticTzInfo 'EST'>) != '2023-07-22 09:37:34-05:00'
        # LAU --> weißt du wo hier das Problem sein könnte 

            
    def test_BeforeTrigger(self):
        toot_before = self.toot_before
        toot_after = self.toot_after
        before = MastodonOOPsolution.BeforeTrigger(ptime= self.clock)

        self.assertTrue(before.evaluate(toot_before))
        self.assertFalse(before.evaluate(toot_after))
        # TypeError: str.replace() takes no keyword arguments
        # Wenn das so funktioniert können wir das auf AfterTrigger auch anwenden
        # ne, leider nicht --> TypeError: str.replace() takes no keyword arguments

    def test_AfterTrigger(self):
        test_clock = datetime.datetime.strptime(self.clock, "%Y-%m-%d %H:%M:%S%z")
        time = test_clock < self.toot_after.pubdate
        time2 = test_clock < self.toot_before.pubdate
        after = MastodonOOPsolution.AfterTrigger(self.clock)
        self.assertEqual(after.evaluate(self.toot_after), time)
        self.assertEqual(after.evaluate(self.toot_before), time2)
        
    def test_NotTrigger(self):
        # not trigger initiation with media trigger 
        nottrigger = MastodonOOPsolution.NotTrigger( MastodonOOPsolution.MediaTrigger() )
        
        self.assertTrue(nottrigger.evaluate(self.toot_false))
        self.assertFalse(nottrigger.evaluate(self.toot_true))   
            
    def test_AndTrigger(self):
        # TypeError: OrTrigger.evaluate() takes 2 positional arguments but 3 were given
        self.toot_gif = MastodonOOPsolution.Toot (
            account = True,
            toot_id = True,
            content = 'dog',
            user_id = True,
            hashtags = True,
            bookmark = True,
            no_replies = True,
            url = True,
            count_replies = True,
            pubdate = True,
            mentions = True,
            media = [{"id": "123","type":"gifv"}],
            language = 'en',
            poll = True        
        )
        
        media = MastodonOOPsolution.MediaTrigger()
        gif = MastodonOOPsolution.GifMediaTrigger()
        andtrigger = MastodonOOPsolution.AndTrigger(
            trigger1 = media, 
            trigger2 = gif
            )
        
        self.assertTrue(andtrigger.evaluate(self.toot_gif))
        self.assertFalse(andtrigger.evaluate(self.toot_false))
        
    def test_OrTrigger(self):
        # TypeError: OrTrigger.evaluate() takes 2 positional arguments but 3 were given
        # Error solved? Sieht so aus als gäbe es da kein Problem mehr
        poll = MastodonOOPsolution.PollTrigger()
        mentions = MastodonOOPsolution.MentionsTrigger()
        ortrigger = MastodonOOPsolution.OrTrigger(
            trigger1 = poll, 
            trigger2 = mentions
            )
        
        self.assertTrue(ortrigger.evaluate(self.toot_true))
        self.assertFalse(ortrigger.evaluate(self.toot_false))
        
    def test_Filter(self):
        poll = MastodonOOPsolution.PollTrigger()
        mentions = MastodonOOPsolution.MentionsTrigger()
        media = MastodonOOPsolution.MediaTrigger()

        toot_list_true = [self.toot_true]
        toot_list_false = [self.toot_false]
        trigger_list = [poll, mentions, media]

        filter_true = MastodonOOPsolution.filter_toots(toots = toot_list_true, triggerlist = trigger_list)
        filter_false = MastodonOOPsolution.filter_toots(toots = toot_list_false, triggerlist = trigger_list)

        self.assertIsNotNone(filter_true)
        self.assertEqual(filter_true, toot_list_true)

        self.assertEqual(filter_false, [])
        
        
    def test_Load_to_Workbook(self):
        temp_filename = 'test_objects.xlsx'
        workbook = openpyxl.Workbook()
        workbook.save(temp_filename)
        toot_list = [self.toot_before]

        # hashtag = 'SMS'
        # toot_list = MastodonOOP.load(hashtag)
        
        MastodonOOPsolution.load_to_workbook(toot_list, temp_filename)

        # Aber hier ist das Problem dass wir Username und Pubdate nur als True speichern, das müssten wir ändern
        # Bei der "Live-Daten"-Methode wäre das kein Problem-

        saved_workbook = openpyxl.load_workbook(temp_filename)
        saved_worksheet = saved_workbook.active

        # Check if the written data matches our expectations
        self.assertEqual(saved_worksheet['A2'].value, toot_list[0].account[0]["username"])
        self.assertEqual(saved_worksheet['B2'].value, toot_list[0].pubdate.replace(tzinfo=None))
        self.assertEqual(saved_worksheet['C2'].value, toot_list[0].content)

        saved_workbook.close()

        os.remove(temp_filename)
    
if __name__ == '__main__':
    unittest.main()