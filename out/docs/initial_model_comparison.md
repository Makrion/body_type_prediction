#### when tested on row baised test data:-
|          Classifier          | Accuracy | F1 Score |
|------------------------------|----------|----------|
| <class 'sklearn.dummy.DummyClassifier'> fot test | 12.5 | 2.7778 |
| <class 'sklearn.dummy.DummyClassifier'> fot train | 25.0 | 10.0 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._perceptron.Perceptron'> fot test | 61.1486 | 56.4309 |
| <class 'sklearn.linear_model._perceptron.Perceptron'> fot train | 50.9311 | 41.9229 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._base.LinearRegression'> fot test | 84.7973 | 85.303 |
| <class 'sklearn.linear_model._base.LinearRegression'> fot train | 86.8715 | 87.0489 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot test | 87.8378 | 87.6478 |
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot train | 88.9199 | 88.8426 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot test | 96.6216 | 96.628 |
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
| <class 'sklearn.svm._classes.SVC'> fot test | 92.2297 | 92.039 |
| <class 'sklearn.svm._classes.SVC'> fot train | 95.6238 | 95.5942 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot test | 95.9459 | 95.9957 |
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|

#### when tested on balnced test data:-
|          Classifier          | Accuracy | F1 Score |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot test | 85.1399 | 84.9745 |
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot train | 88.9199 | 88.8426 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot test | 98.2517 | 98.2507 |
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
| <class 'sklearn.svm._classes.SVC'> fot test | 91.0839 | 90.939 |
| <class 'sklearn.svm._classes.SVC'> fot train | 97.1601 | 97.1503 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot test | 97.2028 | 97.217 |
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
