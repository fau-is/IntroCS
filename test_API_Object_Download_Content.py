import unittest
import MastodonOOPsolution
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
        self.toot_true = MastodonOOPsolution.Toot (
            account = True,
            toot_id = True,
            content = '<p>Hello from Python</p>',
            user_id = True,
            hashtags = [{'name': 'dog', 'url': True, 'history': ''}],
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
    

    def test_api(self):
        self.assertIsInstance(MastodonOOPsolution.mastodon, Mastodon)


    def test_toot(self):   
        assert all(hasattr(self.toot_true, attr) for attr in ["content", "account", "toot_id", "user_id", "hashtags", "bookmark", "no_replies", "url", "count_replies", "pubdate", "mentions", "media", "language", "poll"]), "You are missing an attribute, check again!"
        # eine Nachricht

    def test_load(self):
        toots_dict = []
        hashtag = "Moin"
        mastodon = Mastodon(
            client_id="SOXp3afnWgFJrQf2_UIlqgPva--ZhdBZHS9fyik8Rvg",
            client_secret="HW8bhQJlzAx1eGmLGUvK-qxi4ej8QRDylPFro0El6To",
            access_token="eJpW5z5P82AYIHSzcd6oeHEPaSrP4SMGYn_nxoICLEE",
            api_base_url="https://mastodon.social"
        )

        toots = mastodon.timeline_hashtag(hashtag, limit=10)
        result = MastodonOOPsolution.load(hashtag)
        true_bool = True

        for toot in toots:
            content_text = get_text_content(toot)
            toot = MastodonOOPsolution.Toot(
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

        for toot in result:
            # Extract the toot_id from the current Toot object
            toot_id = toot.toot_id

            # Check if the toot_id is present in toots_dict
            self.assertTrue(any(toot_id == t.toot_id for t in toots_dict))
            
            if not any(toot_id == t.toot_id for t in toots_dict):
                true_bool = False

        for toot in toots_dict:
        # Extract the toot_id from the current Toot object
            toot_id = toot.toot_id

        # Check if the toot_id is present in result (at least once)
            self.assertTrue(any(toot_id == t.toot_id for t in result))
            
            if not any(toot_id == t.toot_id for t in result):
                true_bool = False
            
        # eine Nachricht basierend auf einer BOOL Variable!
        self.assertTrue(true_bool, "Your Loading-Function does not work correctly, check again!")

    def test_GetTextContent(self):
        text = 'Hello from Python'
        text_content = MastodonOOPsolution.get_text_content(self.toot_true)
        self.assertEqual(text, text_content, "Your GetTextContent-Function does not work correctly, check again!")
    # passt
    
    
if __name__ == '__main__':
    unittest.main()