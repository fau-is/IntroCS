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
    
    def test_MediaTrigger(self):
        media = MastodonOOP.MediaTrigger()
        
        self.assertTrue(media.evaluate(self.toot_true))
        self.assertFalse(media.evaluate(self.toot_false))
            
    def test_ImageMediaTrigger(self):
        # TypeError: string indices must be integers, not 'str'
        # self.toot_true.media = {"type":"image"}
        video = MastodonOOP.ImageMediaTrigger()
        
        self.assertTrue(video.evaluate(self.toot_true))
        self.assertFalse(video.evaluate(self.toot_false))

    def test_VideoMediaTrigger(self):
        # TypeError: string indices must be integers, not 'str'
        # self.toot_true.media = {"type":"video"}
        
        self.toot_video= MastodonOOP.Toot (
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
            media = [{"id": "123","type":"video"}],
            language = 'en',
            poll = True        
        )
        video = MastodonOOP.VideoMediaTrigger()
        
        self.assertTrue(video.evaluate(self.toot_video))
        self.assertFalse(video.evaluate(self.toot_false))
        
    def test_GifMediaTrigger(self):
        # AssertionError: False is not true
        # media type anpassen
        # self.toot_true.media[1] = "gifv"
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
        gif = MastodonOOP.GifMediaTrigger()
        
        self.assertTrue(gif.evaluate(self.toot_gif))
        self.assertFalse(gif.evaluate(self.toot_false))
        
    def test_AudioMediaTrigger(self):
        # AssertionError: False is not true
        # media type muss angepasst werden        
        self.toot_audio = MastodonOOP.Toot (
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
            media = [{"id": "123","type":"audio"}],
            language = 'en',
            poll = True        
        )
        audio = MastodonOOP.AudioMediaTrigger()
        
        self.assertTrue(audio.evaluate(self.toot_audio))
        self.assertFalse(audio.evaluate(self.toot_false))
        
    def test_LanguageTrigger(self):
        # AttributeError: 'str' object has no attribute 'evaluate'
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