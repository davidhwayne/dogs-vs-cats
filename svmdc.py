import csv
from sklearn import svm

X=[]
Y=[]
test=[]
ans=[]
with open('traindc.csv','rb') as csvf:
    data=csv.reader(csvf)
    i=0
    for row in data:
	if i<1000:
	        Y.append(int(row[0]))
        	xad=[]
        	for num in row[1:]:
            		xad.append(float(num)/255)
        	X.append(xad)
        else:
        	ans.append(int(row[0]))
		tad=[]
		for num in row[1:]:
			tad.append(float(num)/255)
		test.append(tad)
        	if i>=1099:
			break
	i=i+1
print('Number of training examples = {}'.format(len(X)))
print('Number of test examples = {}'.format(len(test)))
clf = svm.SVC()
print "Fitting..."
clf.fit(X, Y)
print "Predicting..."
predict=clf.predict(test)
count=0
for i in range(len(predict)):
	if predict[i]==ans[i]:
		count=count+1
print('Number of correct predictions = {}'.format(count))
