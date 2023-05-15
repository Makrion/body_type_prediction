#### when tested on row baised test data:-
|          Classifier          | Accuracy | F1 Score |
|------------------------------|----------|----------|
| <class 'sklearn.dummy.DummyClassifier'> fot test | 12.3874 | 2.7307 |
| <class 'sklearn.dummy.DummyClassifier'> fot train | 25.0 | 10.0 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._perceptron.Perceptron'> fot test | 72.973 | 68.4317 |
| <class 'sklearn.linear_model._perceptron.Perceptron'> fot train | 67.6064 | 59.8996 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._base.LinearRegression'> fot test | 84.9099 | 85.4158 |
| <class 'sklearn.linear_model._base.LinearRegression'> fot train | 86.0638 | 86.2723 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot test | 84.4595 | 84.4355 |
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot train | 88.5638 | 88.5111 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot test | 96.8468 | 96.8706 |
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
| <class 'sklearn.svm._classes.SVC'> fot test | 92.7928 | 92.632 |
| <class 'sklearn.svm._classes.SVC'> fot train | 95.1596 | 95.1095 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot test | 96.3964 | 96.4281 |
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|

#### when tested on balnced test data:-
|          Classifier          | Accuracy | F1 Score |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot test | 81.5476 | 81.4904 |
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot train | 88.5638 | 88.5111 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot test | 98.3333 | 98.3355 |
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
| <class 'sklearn.svm._classes.SVC'> fot test | 87.0238 | 86.6617 |
| <class 'sklearn.svm._classes.SVC'> fot train | 97.1277 | 97.1149 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot test | 94.7619 | 94.7667 |
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
