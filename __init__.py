import check50
import check50.py
from mastodon import Mastodon



def import_mastodon():
    mastodon = check50.py.import_("MastodonOOP.py")
    if mastodon is None:
        raise check50.Failure("Mastodon Import failed")
    return mastodon

def import_toots(import_mastodon):
    Masto = import_mastodon()
    toot_true = Masto.Toot (
            account = [{"id": 123, "username": "Marco"}],
            toot_id = True,
            content = '<p>Hello from Python, dog</p>',
            user_id = True,
            hashtags = [{'name': 'dog', 'url': True, 'history': ''}],
            bookmark = True,
            no_replies = True,
            url = True,
            count_replies = True,
            pubdate = '2022-07-22 09:37:34+00:00',
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

    toot_false = Masto.Toot (
            account = '',
            toot_id = '',
            content = 'sun',
            user_id = '',
            hashtags = '',
            bookmark = '',
            no_replies = '',
            url = '',
            count_replies = '',
            pubdate = '2024-07-22 09:37:34+00:00',
            mentions = False,
            media = '',
            language = '',
            poll = False        
        )
        
    return toot_true, toot_false

@check50.check()
def test_file_exists():
    """test.py exists"""
    check50.exists("test.py")
    

@check50.check()
def mastodonOOP_exists():
    """MastodonOOP.py exists"""
    check50.exists("MastodonOOP.py")

@check50.check()
def test_API():
    """testAPI"""
    check50.run("python3 -m unittest test.Mastodon_test.test_API").exit(0)
    #Masto = import_mastodon()
    #if not isinstance(Masto.mastodon, Mastodon):
        #raise check50.Failure("Your API-Initiation does not correctly work, check again if you are missing anything!")
    
        
    # IsInstance(MastodonOOPsolution.mastodon, Mastodon, "Your API-Initiation does not correctly work, check again if you are missing anything!")    #output = check50.run("python3 -m unittest test.Mastodon_test.test_API")
    #failed = "Your API-Initiation does not correctly work, check again if you are missing anything!"
    # result = check50.run("python3 -m unittest test.Mastodon_test.tets_API")
    # if not result:
        # raise check50.Failure("Your API-Initiation does not correctly work, check again if you are missing anything!")
    # check50.log("Your API-Initiation works correctly!")
        
        
@check50.check()
def test_Toot():
    """testToot"""
    true, _ = import_toots()
    for attr in ["content", "account", "toot_id", "user_id", "hashtags", "bookmark", "no_replies", "url", "count_replies", "pubdate", "mentions", "media", "language", "poll"]:
        if not hasattr(true, attr):
            raise check50.Failure("Your Toot-Class does not correctly work, check again if you are missing one or more attributes")
    #check50.run("python3 -m unittest test.Mastodon_test.test_Toot").exit(0)


@check50.check()
def test_load():
    """testLoadFunction"""
    check50.run("python3 -m unittest test.Mastodon_test.test_load").exit(0)
    
@check50.check()
def test_GetTextContent():
    """testGetTextContent"""
    check50.run("python3 -m unittest test.Mastodon_test.test_GetTextContent").exit(0)
    
@check50.check()
def test_MediaTrigger():
    """testMediaTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_MediaTrigger").exit(0)
    
@check50.check()
def test_ImageMediaTrigger():
    """testImageMediaTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_ImageMediaTrigger").exit(0)
    
@check50.check()
def test_VideoMediaTrigger():
    """testVideoMediaTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_VideoMediaTrigger").exit(0)
    
@check50.check()
def test_GifMediaTrigger():
    """testGifMediaTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_GifMediaTrigger").exit(0)
    
@check50.check()
def test_AudioMediaTrigger():
    """testAudioMediaTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_AudioMediaTrigger").exit(0)
    
@check50.check()
def test_LanguageTrigger():
    """testLanguageTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_LanguageTrigger").exit(0)
    
@check50.check()
def test_PollTrigger():
    """testPollTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_PollTrigger").exit(0)

@check50.check()
def test_MentionsTrigger():
    """testMentionsTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_MentionsTrigger").exit(0)
    
@check50.check()
def test_PhraseTrigger():
    """testPhraseTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_PhraseTrigger").exit(0)
    
@check50.check()
def test_TimeTrigger():
    """testTimeTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_TimeTrigger").exit(0)
    
@check50.check()
def test_BeforeTrigger():
    """testBeforeTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_BeforeTrigger").exit(0)
    
@check50.check()
def test_AfterTrigger():
    """testAfterTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_AfterTrigger").exit(0)
    
@check50.check()
def test_NotTrigger():
    """testNotTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_NotTrigger").exit(0)
    
@check50.check()
def test_AndTrigger():
    """testAndTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_AndTrigger").exit(0)
    
@check50.check()
def test_OrTrigger():
    """testOrTrigger"""
    check50.run("python3 -m unittest test.Mastodon_test.test_OrTrigger").exit(0)
    
@check50.check()
def test_Filter():
    """testFilter"""
    check50.run("python3 -m unittest test.Mastodon_test.test_Filter").exit(0)
    
@check50.check()
def test_Load_to_Workbook():
    """testLoad_to_Workbook"""
    check50.run("python3 -m unittest test.Mastodon_test.test_Load_to_Workbook").exit(0)
