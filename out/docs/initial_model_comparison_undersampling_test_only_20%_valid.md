#### when tested on row baised test data:-
|          Classifier          | Accuracy | F1 Score |
|------------------------------|----------|----------|
| <class 'sklearn.dummy.DummyClassifier'> fot test | 12.5 | 2.7778 |
| <class 'sklearn.dummy.DummyClassifier'> fot train | 25.0 | 10.0 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._perceptron.Perceptron'> fot test | 62.8378 | 58.3415 |
| <class 'sklearn.linear_model._perceptron.Perceptron'> fot train | 55.5866 | 51.8252 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._base.LinearRegression'> fot test | 85.473 | 85.9395 |
| <class 'sklearn.linear_model._base.LinearRegression'> fot train | 86.406 | 86.6101 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot test | 86.8243 | 86.7755 |
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot train | 88.8734 | 88.8132 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot test | 98.3108 | 98.3168 |
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
| <class 'sklearn.svm._classes.SVC'> fot test | 92.2297 | 92.035 |
| <class 'sklearn.svm._classes.SVC'> fot train | 95.9497 | 95.9222 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot test | 96.9595 | 97.001 |
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|

#### when tested on balnced test data:-
|          Classifier          | Accuracy | F1 Score |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot test | 84.4595 | 83.996 |
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot train | 88.8734 | 88.8132 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot test | 96.6216 | 96.6192 |
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
| <class 'sklearn.svm._classes.SVC'> fot test | 88.5135 | 88.0045 |
| <class 'sklearn.svm._classes.SVC'> fot train | 97.4395 | 97.4304 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot test | 96.6216 | 96.6473 |
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
