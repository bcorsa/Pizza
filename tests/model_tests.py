from nose.tools import *
import raop.model.ml as model
from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib

iris_testdata = datasets.load_iris()
X_set, Y_set = iris_testdata.data, iris_testdata.target
classifier = svm.SVC()
outputModelFileName = 'test-data/pickle-items/test-output.pkl'
inputModelFileName = 'test-data/pickle-items/test-input.pkl'

def test_save_model():
    modelObj = model.MLmodel(classifier,X_set, Y_set)
    modelObj.saveModel(outputModelFileName)
    origModel = joblib.load(inputModelFileName)
    newModel = joblib.load(outputModelFileName)
    #this test shows that attributes matchs from the two model objects
    assert_equal(origModel.kernel,newModel.kernel)

def crossValidate_test():
    expected_results = [ 1.,  1., 0.86666666666666667,1.,  0.93333333333333335,\
    1.,1.,  1., 1.,  1. ]
    modelObj = model.MLmodel(classifier,X_set, Y_set)
    modelObj.crossValidate()
    assert_equal((expected_results == modelObj.cv_accuracy).all(), True)
 

