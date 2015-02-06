from nose.tools import *
import raop.preprocess.preprocess as preprocess


testDict = {'text' : 'I am here.'}

def test_set_dict():
	'''Test to load dictionary'''
	preProcObj = preprocess.Preprocess()
	preProcObj.setDictionary(testDict)
	assert_equal(preProcObj.kaggleDict,testDict)


def test_tokenize():
	'''Test for word tokenizer'''
	preProcObj = preprocess.Preprocess()
	preProcObj.setDictionary(testDict)
	preProcObj.tokenize(preProcObj.kaggleDict.get('text'))
	assert_equal(preProcObj.tokenizedText, ['I', 'am', 'here', '.'])


def test_pos_tag():
	'''Test for pos tagger'''
	preProcObj = preprocess.Preprocess()
	preProcObj.setDictionary(testDict)
	preProcObj.tokenize(preProcObj.kaggleDict.get('text'))
	preProcObj.posTag(preProcObj.tokenizedText)
	assert_equal(preProcObj.POS_TaggedText , [('I', 'PRP'), ('am', 'VBP'), ('here', 'RB'), ('.', '.')])

