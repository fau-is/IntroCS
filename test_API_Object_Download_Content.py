import unittest
import MastodonOOP
from mastodon import Mastodon
from bs4 import BeautifulSoup
# import resources_tests.toots


def get_text_content(toot):
    content_html = toot['content']
    soup = BeautifulSoup(content_html, 'html.parser')
    content_text = soup.get_text()
    return content_text


class Test_API_Object_Download_Content(unittest.TestCase):
    
    def setUp(self):
        self.toot_true = MastodonOOP.Toot (
            account = True,
            toot_id = True,
            content = 'dog',
            user_id = True,
            hashtags = 'dog',
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
    

    def test_API(self):
        self.assertIsInstance(MastodonOOP.mastodon, Mastodon)
        # KP ob das so klappt
        # --> hier wird kein Error angegeben


    def test_Toot(self):
        self.assertTrue(hasattr(self.toot_true, "content"))
        self.assertTrue(hasattr(self.toot_true, "account"))
        self.assertTrue(hasattr(self.toot_true, "toot_id"))
        self.assertTrue(hasattr(self.toot_true, "user_id"))
        self.assertTrue(hasattr(self.toot_true, "hashtags"))
        self.assertTrue(hasattr(self.toot_true, "bookmark"))
        self.assertTrue(hasattr(self.toot_true, "no_replies"))
        self.assertTrue(hasattr(self.toot_true, "url"))
        self.assertTrue(hasattr(self.toot_true, "count_replies"))
        self.assertTrue(hasattr(self.toot_true, "pubdate"))
        self.assertTrue(hasattr(self.toot_true, "mentions"))
        self.assertTrue(hasattr(self.toot_true, "media"))
        self.assertTrue(hasattr(self.toot_true, "language"))
        self.assertTrue(hasattr(self.toot_true, "poll"))
        
        # Traceback (most recent call last):
        # File "/Users/hannajobst/Documents/FAU Informatik/Industrial Digital/PSet/IntroCS/test_API_Object_Download_Content.py", line 66, in test_Toot
        # self.assertTrue(hasattr(self.toot_true, "hashtags"))
        # AssertionError: False is not true


    def test_load(self):
        toots_dict = []
        hashtag = "AI"
        mastodon = Mastodon(
            client_id="SOXp3afnWgFJrQf2_UIlqgPva--ZhdBZHS9fyik8Rvg",
            client_secret="HW8bhQJlzAx1eGmLGUvK-qxi4ej8QRDylPFro0El6To",
            access_token="eJpW5z5P82AYIHSzcd6oeHEPaSrP4SMGYn_nxoICLEE",
            api_base_url="https://mastodon.social"
        )
        # Load all toots with a specific hashtag into a dictionary, limit to 100 toots
        toots = mastodon.timeline_hashtag(hashtag, limit=10)
        result = MastodonOOP.load(hashtag)

        # Process the retrieved toots
        for toot in toots:
            content_text = get_text_content(toot)
            toot = MastodonOOP.Toot(
                account = toot['account'],
                toot_id = toot['id'],
                content = content_text,
                user_id = toot['account']['id'],
                hashtags = toot['tags'],
                bookmark = toot['bookmarked'],
                no_replies = toot['reblogs_count'],
                url = toot['url'],
                count_replies = toot['replies_count'],
                pubdate = toot['created_at'],
                mentions = toot['mentions'],
                media = toot['media_attachments'],
                language = toot['language'], 
                poll = toot['poll'] 
            )
            toots_dict.append(toot)

            self.assertEqual(result, toots_dict)
            
            # AssertionError: Lists differ: [<Mas[23 chars] 0x111decb90>, <MastodonOOP.Toot object at 0x1[341 chars]d10>] != [<Mas[23 chars] 0x114c42490>]


    def test_GetTextContent(self):
        text = "Test 123"
        toot = "tbd"
        # Hierfür muss noch ein Toot-Object erstellt werden mit originalem HTML-Text
        text_content = MastodonOOP.get_text_content(toot)

        self.assertEqual(text, text_content)
    
if __name__ == '__main__':
    unittest.main()