from nose.tools import *
import raop.featureextract.featureextract as featureextract




def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def testEvidence():
    '''Test for find evidence function'''
    testTextEvi_true="This is the state of my refrigerator: [Linky](http://i.imgur.com/JRvYJ5s.jpg)"
    testTextEvi_false="http://www.4chan.org was not my favorite website "
  
    featObj = featureextract.FeatureExtract()
    featObj.findEvidence(testTextEvi_true)
    assert_equal(featObj.evidence,True)
    featObj.findEvidence(testTextEvi_false)
    assert_equal(featObj.evidence,False)
     
