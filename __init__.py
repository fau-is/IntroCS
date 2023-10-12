import check50
import check50.py

@check50.check()
def test_API():
    """testAPI"""
    check50.run("python3 -m unittest test.Mastodon.test_API").exit(0)

@check50.check()
def test_Toot():
    """testToot"""
    check50.run("python3 -m unittest test.Mastodon.test_Toot").exit(0)


@check50.check()
def test_load():
    """testLoadFunction"""
    check50.run("python3 -m unittest test.Mastodon.test_load").exit(0)
    
@check50.check()
def test_GetTextContent():
    """testGetTextContent"""
    check50.run("python3 -m unittest test.Mastodon.test_GetTextContent").exit(0)
    
@check50.check()
def test_MediaTrigger():
    """testMediaTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_MediaTrigger").exit(0)
    
@check50.check()
def test_ImageMediaTrigger():
    """testImageMediaTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_ImageMediaTrigger").exit(0)
    
@check50.check()
def test_VideoMediaTrigger():
    """testVideoMediaTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_VideoMediaTrigger").exit(0)
    
@check50.check()
def test_GifMediaTrigger():
    """testGifMediaTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_GifMediaTrigger").exit(0)
    
@check50.check()
def test_AudioMediaTrigger():
    """testAudioMediaTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_AudioMediaTrigger").exit(0)
    
@check50.check()
def test_LanguageTrigger():
    """testLanguageTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_LanguageTrigger").exit(0)
    
@check50.check()
def test_PollTrigger():
    """testPollTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_PollTrigger").exit(0)

@check50.check()
def test_MentionsTrigger():
    """testMentionsTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_MentionsTrigger").exit(0)
    
@check50.check()
def test_PhraseTrigger():
    """testPhraseTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_PhraseTrigger").exit(0)
    
@check50.check()
def test_TimeTrigger():
    """testTimeTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_TimeTrigger").exit(0)
    
@check50.check()
def test_BeforeTrigger():
    """testBeforeTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_BeforeTrigger").exit(0)
    
@check50.check()
def test_AfterTrigger():
    """testAfterTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_AfterTrigger").exit(0)
    
@check50.check()
def test_NotTrigger():
    """testNotTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_NotTrigger").exit(0)
    
@check50.check()
def test_AndTrigger():
    """testAndTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_AndTrigger").exit(0)
    
@check50.check()
def test_OrTrigger():
    """testOrTrigger"""
    check50.run("python3 -m unittest test.Mastodon.test_OrTrigger").exit(0)
    
@check50.check()
def test_Filter():
    """testFilter"""
    check50.run("python3 -m unittest test.Mastodon.test_Filter").exit(0)
    
@check50.check()
def test_Load_to_Workbook():
    """testLoad_to_Workbook"""
    check50.run("python3 -m unittest test.Mastodon.test_Load_to_Workbook").exit(0)