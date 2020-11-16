import check50
import check50.py
import datetime
#from ps5_test import *
#from ps5 import *

@check50.check()
def testNewsStoryConstructor():
    """testNewsStoryConstructor"""
    if check50.run("python -m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryConstructor") == False:
        raise check50.error

@check50.check()
def testNewsStoryGetGuid():
    """testNewsStoryGetGuid"""
    check50.run("python -m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryGetGuid")

@check50.check()
def testNewsStoryGetTitle():
    """testNewsStoryGetGuid"""
    check50.run("python -m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryGetTitle")

@check50.check()
def testNewsStoryGetdescription():
    """testNewsStoryGetdescription"""
    check50.run("python - m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryGetdescription")

@check50.check()
def testNewsStoryGetLink():
    """testNewsStoryGetLink"""
    check50.run("python - m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryGetLink")

@check50.check()
def testNewsStoryGetTime():
    """testNewsStoryGetTime"""
    check50.run("python - m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryGetTime")

@check50.check()
def test1TitleTrigger():
    """test1TitleTrigger"""
    check50.run("python - m unittest ps5_test.ProblemSet5.test1TitleTrigger")

@check50.check()
def test2TitleTrigger():
    """test2TittleTrigger"""
    check50.run("python - m unittest ps5_test.ProblemSet5.test2TitleTrigger")

@check50.check()
def test2DescriptionTrigger():
    """test2DescriptionTrigger"""
    check50.run("python - m unittest ps5_test.ProblemSet5.test2DescriptionTrigger")

@check50.check()
def test3altBeforeAndAfterTrigger():
    """test3altBeforeAndAfterTrigger"""
    check50.run("python - m unittest ps5_test.ProblemSet5.test3altBeforeAndAfterTrigger")

@check50.check()
def test3BeforeAndAfterTrigger():
    """test3BeforeAndAfterTrigger"""
    #check50.run("python - m unittest ps5_test.ProblemSet5.test3BeforeAndAfterTrigger")
    dt = datetime.timedelta(seconds=5)
    now = datetime(2016, 10, 12, 23, 59, 59)
    ancient = NewsStory('', '', '', '', datetime(1987, 10, 15))
    just_now = NewsStory('', '', '', '', now - dt)
    in_a_bit = NewsStory('', '', '', '', now + dt)
    future = NewsStory('', '', '', '', datetime(2087, 10, 15))

    s1 = BeforeTrigger('12 Oct 2016 23:59:59')
    s2 = AfterTrigger('12 Oct 2016 23:59:59')

    self.assertTrue(s1.evaluate(ancient), "BeforeTrigger failed to fire on news from long ago")
    self.assertTrue(s1.evaluate(just_now), "BeforeTrigger failed to fire on news happened right before specified time")

    self.assertFalse(s1.evaluate(in_a_bit), "BeforeTrigger fired to fire on news happened right after specified time")
    self.assertFalse(s1.evaluate(future), "BeforeTrigger fired to fire on news from the future")

    self.assertFalse(s2.evaluate(ancient), "AfterTrigger fired to fire on news from long ago")
    self.assertFalse(s2.evaluate(just_now), "BeforeTrigger fired to fire on news happened right before specified time")

    self.assertTrue(s2.evaluate(in_a_bit), "AfterTrigger failed to fire on news just after specified time")
    self.assertTrue(s2.evaluate(future), "AfterTrigger failed to fire on news from long ago")


@check50.check()
def test4NotTrigger():
    """test4NotTrigger"""
    check50.run("python - m unittest ps5_test.ProblemSet5.test4NotTrigger")

@check50.check()
def test5AndTrigger():
    """test5AndTrigger"""
    check50.run("python - m unittest ps5_test.ProblemSet5.test5AndTrigger")

@check50.check()
def test6OrTrigger():
    """test6OrTrigger"""
    check50.run("python - m unittest ps5_test.ProblemSet5.test6OrTrigger")

@check50.check()
def test7FilterStories():
    """test7FilterStories"""
    check50.run("python - m unittest ps5_test.ProblemSet5.test7FilterStories")

@check50.check()
def test8FilterStories2():
    """Test8FilterStories2"""
    check50.run("python - m unittest ps5_test.ProblemSet5.test8FilterStories2")

