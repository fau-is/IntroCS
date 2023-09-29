import unittest
import MastodonOOPsolution


class Test_mediaTriggers(unittest.TestCase):
    
    def setUp(self):
        self.toot_true = MastodonOOPsolution.Toot (
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
            mentions = '',
            media = [{"id": "123","type":"image"}],
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
            mentions = '',
            media = '',
            language = '',
            poll = ''        
        )
    
    def tearDown(self):
        pass
    
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
        self.assertFalse(andtrigger.evaluate(self.toot_true))
        
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
    
if __name__ == '__main__':
    unittest.main()