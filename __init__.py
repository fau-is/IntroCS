import check50
import check50.py
#from ps5_test import *
#from ps5 import *

@check50.check()
def testNewsStoryConstructor():
    """testNewsStoryConstructor"""
    check50.run("python3 -m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryConstructor").exit(0)

@check50.check()
def testNewsStoryGetGuid():
    """testNewsStoryGetGuid"""
    check50.run("python3 -m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryGetGuid").exit(0)

@check50.check()
def testNewsStoryGetTitle():
    """testNewsStoryGetGuid"""
    check50.run("python3 -m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryGetTitle").exit(0)

@check50.check()
def testNewsStoryGetdescription():
    """testNewsStoryGetdescription"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryGetdescription").exit(0)

@check50.check()
def testNewsStoryGetLink():
    """testNewsStoryGetLink"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryGetLink").exit(0)

@check50.check()
def testNewsStoryGetTime():
    """testNewsStoryGetTime"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5NewsStory.testNewsStoryGetTime").exit(0)

@check50.check()
def test1TitleTrigger():
    """test1TitleTrigger"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5.test1TitleTrigger").exit(0)

@check50.check()
def test2TitleTrigger():
    """test2TittleTrigger"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5.test2TitleTrigger").exit(0)

@check50.check()
def test2DescriptionTrigger():
    """test2DescriptionTrigger"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5.test2DescriptionTrigger").exit(0)

@check50.check()
def test3altBeforeAndAfterTrigger():
    """test3altBeforeAndAfterTrigger"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5.test3altBeforeAndAfterTrigger").exit(0)

@check50.check()
def test3BeforeAndAfterTrigger():
    """test3BeforeAndAfterTrigger"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5.test3BeforeAndAfterTrigger").exit(0)

@check50.check()
def test4NotTrigger():
    """test4NotTrigger"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5.test4NotTrigger").exit(0)

@check50.check()
def test5AndTrigger():
    """test5AndTrigger"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5.test5AndTrigger").exit(0)

@check50.check()
def test6OrTrigger():
    """test6OrTrigger"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5.test6OrTrigger").exit(0)

@check50.check()
def test7FilterStories():
    """test7FilterStories"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5.test7FilterStories").exit(0)

@check50.check()
def test8FilterStories2():
    """Test8FilterStories2"""
    check50.run("python3 - m unittest ps5_test.ProblemSet5.test8FilterStories2").exit(0)

