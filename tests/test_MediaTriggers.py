import unittest
from IntroCS.MastodonOOP import MastodonOOP
import json


class Test_mediaTriggers(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_MediaTrigger(self):
        #self.assertEqual(MastodonOOP.MediaTrigger.evaluate(toot_Media), True)
        self.assertTrue(MastodonOOP.MediaTrigger.evaluate(toot_media))
        self.assertFalse(MastodonOOP.MediaTrigger.evaluate(toot_no_media))

    def test_VideoMediaTrigger(self):
        self.assertTrue(MastodonOOP.VideoMediaTrigger.evaluate(toot_video))
        self.assertFalse(MastodonOOP.VideoMediaTrigger.evaluate(toot_no_video))
        
    def test_GifMediaTrigger(self):
        self.assertTrue(MastodonOOP.GifMediaTrigger.evaluate(toot_gif))
        self.assertFalse(MastodonOOP.GifMediaTrigger.evaluate(toot_no_gif))
        
    def test_AudioMediaTrigger(self):
        self.assertTrue(MastodonOOP.AudioMediaTrigger.evaluate(toot_audio))
        self.assertFalse(MastodonOOP.AudioMediaTrigger.evaluate(toot_no_audio))
        
    def test_LanguageTrigger(self):
        english = MastodonOOP.NotTrigger("en")
        
        self.assertTrue(english.evaluate(toot_eng))
        self.assertFalse(english.evaluate(toot_no_eng))  
    
    def test_PollTrigger(self):
        self.assertTrue(MastodonOOP.PollTrigger.evaluate(toot_poll))
        self.assertFalse(MastodonOOP.PollTrigger.evaluate(toot_no_poll))
        
    def test_PhraseTrigger(self):
        phrase = MastodonOOP.NotTrigger("dog")
        
        self.assertTrue(phrase.evaluate(toot_dog))
        self.assertFalse(phrase.evaluate(toot_no_dog)) 
    
if __name__ == '__main__':
    unittest.main()