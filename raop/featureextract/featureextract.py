import re

class FeatureExtract(object):
    def  __init__(self):
        self.evidence = None
        self.statusKarma = None
	self.statusAccAge = None
	self.statusPrevAct = None

    def findEvidence(self,textString):
	'''Find reddit post with image/proof'''

	regex = re.compile(r"([Hh]ttp(\S)+((imgur)|(youtube))(\w|\W)+)|([Hh]ttp(\S)+((jpe?g)|(png)))")
	match = re.search(regex,textString)	
	if match: 	
            self.evidence = True
	else :
	    self.evidence = False
