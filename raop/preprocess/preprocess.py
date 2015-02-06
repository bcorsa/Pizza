from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

class Preprocess(object):
	def __init__(self):
		self.kaggleDict = {}
		self.tokenizedText = None
		self.POS_TaggedText = None
		
	def setDictionary(self,dictionary):
		self.kaggleDict = dictionary
	
	def tokenize(self,textString):
		'''Tokenize a text string using standard nltk tokenizer'''
		self.tokenizedText = word_tokenize(textString)
	
	def posTag(self, tokens):
		'''POS tag a list of tokenized text using standard nltk POS tagger'''
		self.POS_TaggedText = pos_tag(tokens)
	
	#def normalization(self, tokens):
		
		
