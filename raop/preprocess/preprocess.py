from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem.porter import *
from nltk.corpus import stopwords

class Preprocess(object):
	def __init__(self):
		self.kaggleDict = {}
		self.sentSegmentedText = None
		self.tokenizedText = None
		self.POS_TaggedText = None
		
		#Normalization
		self.lowerCaseText = None
		self.stopWordRmText = None
		self.stemmedText = None
		self.normalisedText = None

		self.concatText = None		

	def setDictionary(self,dictionary):
		'''Sets the dictionary'''
		self.kaggleDict = dictionary
	
	def sentSeg(self, textString):
		'''Splits the string of text into individual sentences, returns a list of sentences'''
		self.sentSegmentedText = sent_tokenize(textString) 
		
	def tokenize(self,textString):
		'''Tokenize a text string using standard nltk tokenizer'''
		self.tokenizedText = word_tokenize(textString)
	
	def posTag(self, tokens):
		'''POS tag a list of tokenized text using standard nltk POS tagger'''
		self.POS_TaggedText = pos_tag(tokens)
	
	def lowerCase(self, tokens):
		'''Convert tokens to lowercase'''
		self.lowerCaseText = [w.lower() for w in tokens ]

	def stopWordRm(self, tokens):
		'''Remove stop words from list of tokens'''
		wstop = stopwords.words('english')	
		self.stopWordRmText = [w for w in tokens if w not in wstop]

	def stem(self, tokens):
		'''Run porter stemmer on list of tokens'''
		stemmer = PorterStemmer()
		self.stemmedText=[stemmer.stem(w) for w in tokens ]
		
	def normalisation(self, tokens):
		'''Run all normalisation functions on list of tokens'''
		self.lowerCase(tokens)
		self.stopWordRm(self.lowerCaseText)
		self.stem(self.stopWordRmText)
		self.normalisedText=self.stemmedText
	
	def concatenate(self, firstKey, secondKey):
		'''Concatenate two string key value pairs from dictionary
		First Key Values + Second Key Values'''
		#self.concatText = str (str(self.kaggleDict.get(firstKey)) + ' ' + str(self.kaggleDict.get(secondKey)))
		self.concatText = str (self.kaggleDict.get(firstKey).encode('utf-8') + ' ' + self.kaggleDict.get(secondKey).encode('utf-8'))

	def dropKey(self, keyName):
		'''Remove specified Key Value from dictionary'''
		self.kaggleDict.pop(keyName)
										

		
