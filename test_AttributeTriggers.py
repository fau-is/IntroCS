import unittest
import MastodonOOPsolution


class Test_AttributeTriggers(unittest.TestCase):
    
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
            mentions = '',
            media = '',
            language = '',
            poll = ''        
        )
    
    def tearDown(self):
        pass
    
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
    
if __name__ == '__main__':
    unittest.main()