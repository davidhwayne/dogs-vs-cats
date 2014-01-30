import os
from nolearn.convnet import ConvNetFeatures
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
from sklearn import svm

pretraindir = '/home/david/Projects/dogscats/pretrain/'
traindir = '/home/david/Projects/dogscats/train/'

def get_dataset():
	cats = traindir + 'cat/'
	catfilenames = [cats + fn for fn in os.listdir(cats)]
	dogs = traindir + 'dog/'
	dogfilenames = [dogs + fn for fn in os.listdir(dogs)]

	labels = [0] * len(catfilenames) + [1] * len(dogfilenames)
	filenames = catfilenames + dogfilenames
	return shuffle(filenames, labels, random_state=0)

convnet = ConvNetFeatures(
	pretrained_params=pretraindir + 'imagenet.decafnet.epoch90',
	pretrained_meta=pretraindir + 'imagenet.decafnet.meta',
	)
clf = svm.SVC(kernel='linear')
pl = Pipeline([
	('convnet', convnet),
	('clf', clf),
	])
x, y = get_dataset()
XT, YT = x[:100], y[:100]
test, ans = x[100:300], y[100:300]
print "Fitting..."
pl.fit(XT, YT)
print "Predicting..."
predict = pl.predict(test)
print "Accuracy: %.3f" % accuracy_score(ans, predict)

