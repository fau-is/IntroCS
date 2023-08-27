import unittest
import MastodonOOP
from openpyxl import load_workbook
import os


class Test_FilterExcel(unittest.TestCase):
    
    def setUp(self):
        self.toot_true = MastodonOOP.Toot (
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
            mentions = '',
            media = '',
            language = '',
            poll = ''        
        )
    
    def tearDown(self):
        pass
    
    def test_Filter(self):
        poll = MastodonOOP.PollTrigger()
        mentions = MastodonOOP.MentionsTrigger()
        media = MastodonOOP.MediaTrigger()

        toot_list_true = [self.toot_true]
        toot_list_false = [self.toot_true]
        trigger_list = [poll, mentions, media]

        filter_true = MastodonOOP.filter_toots(toots = toot_list_true, triggerlist = trigger_list)
        filter_false = MastodonOOP.filter_toots(toots = toot_list_false, triggerlist = trigger_list)

        self.assertIsNotNone(filter_true)
        self.assertEqual(filter_true, toot_list_true)

        self.assertIsNone(filter_false)
            
    def test_Load_to_Workbook(self):
        # Wollen wir den Studis das überhaupt selber schreiben lassen oder vorgeben?

        temp_filename = 'test_objects.xlsx'


        hashtag = 'SMS'
        toot_list = MastodonOOP.load(hashtag)
        MastodonOOP.load_to_workbook(toot_list, temp_filename)

        # oder || eins muss auskommentiert werden sonst nimmts immer die Mock-Up Variante, weil Neu-Initialisierung

        toot_list = [self.toot_true] # Aber hier ist das Problem dass wir Username und Pubdate nur als True speichern, das müssten wir ändern
                                     # Bei der "Live-Daten"-Methode wäre das kein Problem-


        saved_workbook = load_workbook(temp_filename)
        saved_worksheet = saved_workbook.active

        # Check if the written data matches our expectations
        self.assertEqual(saved_worksheet['A2'].value, toot_list[0].account["username"])
        self.assertEqual(saved_worksheet['B2'].value, toot_list[0].pubdate.replace(tzinfo=None))
        self.assertEqual(saved_worksheet['C2'].value, toot_list[0].content)

        saved_workbook.close()

        os.remove(temp_filename)

    
    
if __name__ == '__main__':
    unittest.main()