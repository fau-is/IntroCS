import unittest
import MastodonOOP


class Test_mediaTriggers(unittest.TestCase):
    
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
    
    def test_NotTrigger(self):
        # not trigger initiation with media trigger 
        nottrigger = MastodonOOP.NotTrigger( MastodonOOP.MediaTrigger() )
        
        self.assertTrue(nottrigger.evaluate(self.toot_false))
        self.assertFalse(nottrigger.evaluate(self.toot_true))   
            
    def test_AndTrigger(self):
        # TypeError: OrTrigger.evaluate() takes 2 positional arguments but 3 were given
        self.toot_gif = MastodonOOP.Toot (
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
        
        media = MastodonOOP.MediaTrigger()
        gif = MastodonOOP.GifMediaTrigger()
        andtrigger = MastodonOOP.AndTrigger(
            trigger1 = media, 
            trigger2 = gif
            )
        
        self.assertTrue(andtrigger.evaluate(self.toot_true, self.toot_gif))
        self.assertFalse(andtrigger.evaluate(self.toot_true, self.toot_true))
        
    def test_OrTrigger(self):
        # TypeError: OrTrigger.evaluate() takes 2 positional arguments but 3 were given
        # Error solved? Sieht so aus als gäbe es da kein Problem mehr
        poll = MastodonOOP.PollTrigger()
        mentions = MastodonOOP.MentionsTrigger()
        ortrigger = MastodonOOP.OrTrigger(
            trigger1 = poll, 
            trigger2 = mentions
            )
        
        self.assertTrue(ortrigger.evaluate(self.toot_false, self.toot_true))
        self.assertFalse(ortrigger.evaluate(self.toot_false, self.toot_false))         
    
if __name__ == '__main__':
    unittest.main()