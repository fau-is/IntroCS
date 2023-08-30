import unittest
import MastodonOOP
from openpyxl import load_workbook
import openpyxl
import os


class Test_FilterExcel(unittest.TestCase):
    
    def setUp(self):
        self.toot_true = MastodonOOP.Toot (
            account = [{"id": 123, "username": "Marco"}],
            toot_id = True,
            content = 'dog',
            user_id = True,
            hashtags = [{'name': 'dog', 'url': True, 'history': ''}],
            bookmark = True,
            no_replies = True,
            url = True,
            count_replies = True,
            pubdate = True,
            mentions = True,
            media = [{"id": "123","type":"image"}],
            language = 'en',
            poll = True        
        )
        self.toot_false = MastodonOOP.Toot (
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
            media = False,
            language = '',
            poll = False        
        )
    
    def tearDown(self):
        pass
    
    def test_Filter(self):
        poll = MastodonOOP.PollTrigger()
        mentions = MastodonOOP.MentionsTrigger()
        media = MastodonOOP.MediaTrigger()

        toot_list_true = [self.toot_true]
        toot_list_false = [self.toot_false]
        trigger_list = [poll, mentions, media]

        filter_true = MastodonOOP.filter_toots(toots = toot_list_true, triggerlist = trigger_list)
        filter_false = MastodonOOP.filter_toots(toots = toot_list_false, triggerlist = trigger_list)

        self.assertIsNotNone(filter_true)
        self.assertEqual(filter_true, toot_list_true)

        self.assertEqual(filter_false, [])
        
        # Traceback (most recent call last):
        # File "/Users/hannajobst/Documents/FAU Informatik/Industrial Digital/PSet/IntroCS/test_FilterLoad2Workbook.py", line 61, in test_Filter
        # self.assertIsNone(filter_false)
        # AssertionError: [<MastodonOOP.Toot object at 0x109f81910>] is not None
        
        # Entweder ich hab es so behoben, indem ich False anstat '' gemacht habe ansonsten müssen wir nochmal schauen was in Realität returnt wird

    def test_Load_to_Workbook(self):
        temp_filename = 'test_objects.xlsx'
        workbook = openpyxl.Workbook()
        workbook.save(temp_filename)
        toot_list = [self.toot_true]
        # hashtag = 'SMS'
        # toot_list = MastodonOOP.load(hashtag)
        MastodonOOP.load_to_workbook(toot_list, temp_filename)

        # Aber hier ist das Problem dass wir Username und Pubdate nur als True speichern, das müssten wir ändern
        # Bei der "Live-Daten"-Methode wäre das kein Problem-

        saved_workbook = load_workbook(temp_filename)
        saved_worksheet = saved_workbook.active

        # Check if the written data matches our expectations
        self.assertEqual(saved_worksheet['A2'].value, toot_list[0].account[0]["username"])
        self.assertEqual(saved_worksheet['B2'].value, toot_list[0].pubdate.replace(tzinfo=None))
        self.assertEqual(saved_worksheet['C2'].value, toot_list[0].content)

        saved_workbook.close()

        os.remove(temp_filename)
        # AssertionError: None != 'Marco'
        # AttributeError: 'bool' object has no attribute 'replace'

    
    
if __name__ == '__main__':
    unittest.main()