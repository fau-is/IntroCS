import unittest
import MastodonOOP


class Test_AttributeTriggers(unittest.TestCase):
    
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
            media = [{"id": 123,"type":"image"},
                     {"id": 1234,"type":"video"},
                     {"id": 12345,"type":"gifv"},
                     {"id": 123456,"type":"audio"},
                     {"id": 1234567,"type":"unknown"} 
                     ],
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
    
    def test_MediaTrigger(self):
        media = MastodonOOP.MediaTrigger()
        
        self.assertTrue(media.evaluate(self.toot_true))
        self.assertFalse(media.evaluate(self.toot_false))
            
    def test_ImageMediaTrigger(self):
        video = MastodonOOP.ImageMediaTrigger()
        
        self.assertTrue(video.evaluate(self.toot_true))
        self.assertFalse(video.evaluate(self.toot_false))

    def test_VideoMediaTrigger(self):
        video = MastodonOOP.VideoMediaTrigger()
        
        self.assertTrue(video.evaluate(self.toot_true))   
        self.assertFalse(video.evaluate(self.toot_false))
        
    def test_GifMediaTrigger(self):
        gif = MastodonOOP.GifMediaTrigger()
        
        self.assertTrue(gif.evaluate(self.toot_true))   
        self.assertFalse(gif.evaluate(self.toot_false))
        
    def test_AudioMediaTrigger(self):
        audio = MastodonOOP.AudioMediaTrigger()
        
        self.assertTrue(audio.evaluate(self.toot_true))   
        self.assertFalse(audio.evaluate(self.toot_false))
        
    def test_LanguageTrigger(self):
        english = MastodonOOP.LanguageTrigger("en")
        
        self.assertTrue(english.evaluate(self.toot_true))
        self.assertFalse(english.evaluate(self.toot_false))  
    
    def test_PollTrigger(self):
        poll_filter = MastodonOOP.PollTrigger()
        
        self.assertTrue(poll_filter.evaluate(self.toot_true))
        self.assertFalse(poll_filter.evaluate(self.toot_false))
        
    def test_MentionsTrigger(self):
        mentions = MastodonOOP.MentionsTrigger()
        
        self.assertTrue(mentions.evaluate(self.toot_true))
        self.assertFalse(mentions.evaluate(self.toot_false))
        
    def test_PhraseTrigger(self):
        phrase = MastodonOOP.PhraseTrigger("dog")
        
        self.assertTrue(phrase.evaluate(self.toot_true))
        self.assertFalse(phrase.evaluate(self.toot_false)) 
    
if __name__ == '__main__':
    unittest.main()