import unittest
import IntroCS.MastodonOOP


class Test_mediaTriggers(unittest.TestCase):
    
    def setUp(self):
        toot_true = MastodonOOP.Toot (
            account = '',
            toot_id = '',
            content = '',
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
        toot_false = MastodonOOP.Toot (
            account = '',
            toot_id = '',
            content = '',
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
    
    def test_MediaTrigger(self):
        toot_true = {"media": True}
        toot_false = {"media": False}
        
        self.assertTrue(MastodonOOP.MediaTrigger.evaluate(toot_true))
        self.assertFalse(MastodonOOP.MediaTrigger.evaluate(toot_false))

    def test_VideoMediaTrigger(self):
        # wie funktioniert der filter ???
        # toot_true = {content["type"] = "video" }
        toot_false = {"media": False}
        
        #self.assertTrue(MastodonOOP.VideoMediaTrigger.evaluate(toot_true))
        self.assertFalse(MastodonOOP.VideoMediaTrigger.evaluate(toot_false))
        
    def test_GifMediaTrigger(self):
        toot_true = {"media": True}
        toot_false = {"media": False}
        
        self.assertTrue(MastodonOOP.GifMediaTrigger.evaluate(toot_true))
        self.assertFalse(MastodonOOP.GifMediaTrigger.evaluate(toot_false))
        
    def test_AudioMediaTrigger(self):
        toot_true = {"media": True}
        toot_false = {"media": False}
        
        self.assertTrue(MastodonOOP.AudioMediaTrigger.evaluate(toot_true))
        self.assertFalse(MastodonOOP.AudioMediaTrigger.evaluate(toot_false))
        
    def test_LanguageTrigger(self):
        english = MastodonOOP.NotTrigger("en")
        
        toot_true = {"language": "en"}
        toot_false = {"language": "du"}
        
        self.assertTrue(english.evaluate(toot_true))
        self.assertFalse(english.evaluate(toot_false))  
    
    def test_PollTrigger(self):
        # poll_filter = PollTrigger()
        toot_true = {"media": True}
        toot_false = {"media": False}
        
        self.assertTrue(MastodonOOP.PollTrigger.evaluate(toot_true))
        self.assertFalse(MastodonOOP.PollTrigger.evaluate(toot_false))
        
    def test_MentionsTrigger(self):
        toot_true = {"media": True}
        toot_false = {"media": False}
        
        self.assertTrue(MastodonOOP.MentionsTrigger.evaluate(toot_true))
        self.assertFalse(MastodonOOP.MentionsTrigger.evaluate(toot_false))
        
    def test_PhraseTrigger(self):
        phrase = MastodonOOP.PhraseTrigger("dog")

        toot_true = {"content": "dog"}
        toot_false = {"content": "sun"}
        
        self.assertTrue(phrase.evaluate(toot_true))
        self.assertFalse(phrase.evaluate(toot_false)) 
    
if __name__ == '__main__':
    unittest.main()