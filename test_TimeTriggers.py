import unittest
import MastodonOOP


class Test_TimeTriggers(unittest.TestCase):
    
    def setUp(self):
        self.toot_before = MastodonOOP.Toot (
            account = True,
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
        self.toot_after = MastodonOOP.Toot (
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

        self.clock = '2023-07-22 09:37:34+00:00' 
    
    def tearDown(self):
        pass
    
    def test_TimeTrigger(self):
        formatted_time = '2023-07-22 09:37:34-05:00'
        triggered_time = MastodonOOP.TimeTrigger(self.clock)
        
        self.assertEqual(triggered_time.ptime, formatted_time)
        # Chat gpt vorschlag isoformat() nach ptime
        # ValueError: unconverted data remains: +00:00 (behoben)
        # AssertionError: datetime.datetime(2023, 7, 22, 9, 37, 34, tzinfo=<StaticTzInfo 'EST'>) != '2023-07-22 09:37:34-05:00'
        # LAU --> weißt du wo hier das Problem sein könnte 

            
    def test_BeforeTrigger(self):
        toot_before = self.toot_before
        toot_after = self.toot_after
        before = MastodonOOP.BeforeTrigger(ptime= self.clock)

        self.assertTrue(before.evaluate(toot_before))
        self.assertFalse(before.evaluate(toot_after))
        # TypeError: str.replace() takes no keyword arguments
        # Wenn das so funktioniert können wir das auf AfterTrigger auch anwenden
        # ne, leider nicht --> TypeError: str.replace() takes no keyword arguments

    def test_AfterTrigger(self):
        time = self.clock < self.toot_after.pubdate
        time2 = self.clock < self.toot_before.pubdate
        after = MastodonOOP.AfterTrigger(self.clock)
        self.assertEqual(after.evaluate(self.toot_after), time)
        self.assertEqual(after.evaluate(self.toot_before), time2)
    
    
if __name__ == '__main__':
    unittest.main()