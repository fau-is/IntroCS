import check50
import check50.py
from mastodon import Mastodon


@check50.check()
def test_file_exists():
    """test.py exists"""
    check50.exists("test.py")
    

@check50.check()
def mastodonOOP_exists():
    """MastodonOOP.py exists"""
    check50.exists("MastodonOOP.py")
    
@check50.check()
def group_members_exists():
    """group_members.txt exists"""
    check50.exists("group_members.txt")

@check50.check()
def test_API():
    """testAPI"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_API").exit(0)
    except:
        raise check50.Failure("Your API-Initiation does not correctly work, check again if you are missing anything!")

        
@check50.check()
def test_Toot():
    """testToot"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_Toot").exit(0)
    except:
        raise check50.Failure("The object Toot did not get inizalized as required.")

@check50.check()
def test_load():
    """testLoadFunction"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_load").exit(0)
    except:
        raise check50.Failure("The download of toots does not work correct.")
    
@check50.check()
def test_GetTextContent():
    """testGetTextContent"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_GetTextContent").exit(0)
    except:
        raise check50.Failure("Your GetTextContent-Function does not work correctly, check again if only the text remains and no HTML is left!")
    
@check50.check()
def test_MediaTrigger():
    """testMediaTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_MediaTrigger").exit(0)
    except:
        raise check50.Failure("MediaTrigger works not accordingly.")

    
@check50.check()
def test_ImageMediaTrigger():
    """testImageMediaTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_ImageMediaTrigger").exit(0)
    except:
        raise check50.Failure("ImageMediaTrigger works not accordingly.")
        
    
@check50.check()
def test_VideoMediaTrigger():
    """testVideoMediaTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_VideoMediaTrigger").exit(0)
    except:
        raise check50.Failure("VideoMediaTrigger works not accordingly.")
    
@check50.check()
def test_GifMediaTrigger():
    """testGifMediaTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_GifMediaTrigger").exit(0)
    except:
        raise check50.Failure("GifMediaTrigger works not accordingly.")
        
    
@check50.check()
def test_AudioMediaTrigger():
    """testAudioMediaTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_AudioMediaTrigger").exit(0)
    except:
        raise check50.Failure("AudioMediaTrigger works not accordingly.")
        
    
@check50.check()
def test_LanguageTrigger():
    """testLanguageTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_LanguageTrigger").exit(0)
    except:
        raise check50.Failure("LanguageTrigger works not accordingly.")
        
    
@check50.check()
def test_PollTrigger():
    """testPollTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_PollTrigger").exit(0)
    except:
        raise check50.Failure("PollTrigger works not accordingly.")
        

@check50.check()
def test_MentionsTrigger():
    """testMentionsTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_MentionsTrigger").exit(0)
    except:
        raise check50.Failure("MentionsTrigger works not accordingly.")
        
    
@check50.check()
def test_PhraseTrigger():
    """testPhraseTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_PhraseTrigger").exit(0)
    except:
        raise check50.Failure("PhraseTrigger works not accordingly.")
        
    
@check50.check()
def test_TimeTrigger():
    """testTimeTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_TimeTrigger").exit(0)
    except:
        raise check50.Failure("TimeTrigger works not accordingly.")
        
    
@check50.check()
def test_BeforeTrigger():
    """testBeforeTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_BeforeTrigger").exit(0)
    except:
        raise check50.Failure("BeforeTrigger works not accordingly.")
        
    
@check50.check()
def test_AfterTrigger():
    """testAfterTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_AfterTrigger").exit(0)
    except:
        raise check50.Failure("AfterTrigger works not accordingly.")
        
    
@check50.check()
def test_NotTrigger():
    """testNotTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_NotTrigger").exit(0)
    except:
        raise check50.Failure("NotTrigger works not accordingly.")
        
    
@check50.check()
def test_AndTrigger():
    """testAndTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_AndTrigger").exit(0)
    except:
        raise check50.Failure("Andrigger works not accordingly.")
        
    
@check50.check()
def test_OrTrigger():
    """testOrTrigger"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_OrTrigger").exit(0)
    except:
        raise check50.Failure("OrTrigger works not accordingly.")
        
    
@check50.check()
def test_Filter():
    """testFilter"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_Filter").exit(0)
    except:
        raise check50.Failure("The Filter function is not working as required.")
        
    
@check50.check()
def test_Load_to_Workbook():
    """testLoad_to_Workbook"""
    try:
        check50.run("python3 -m unittest test.Mastodon_test.test_Load_to_Workbook").exit(0)
    except:
        raise check50.Failure("Loading to the workbook was not succesful. Make sure to read the openpyxl documentation.")
        