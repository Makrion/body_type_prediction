#### when tested on row baised test data:-
|          Classifier          | Accuracy | F1 Score |
|------------------------------|----------|----------|
| <class 'sklearn.dummy.DummyClassifier'> fot test | 12.5 | 2.7778 |
| <class 'sklearn.dummy.DummyClassifier'> fot train | 25.0 | 10.0 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._perceptron.Perceptron'> fot test | 76.3514 | 72.7989 |
| <class 'sklearn.linear_model._perceptron.Perceptron'> fot train | 70.2536 | 64.3415 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._base.LinearRegression'> fot test | 86.1486 | 86.5454 |
| <class 'sklearn.linear_model._base.LinearRegression'> fot train | 86.8116 | 86.9791 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot test | 87.8378 | 87.823 |
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot train | 89.0942 | 89.0157 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot test | 97.6351 | 97.6463 |
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
| <class 'sklearn.svm._classes.SVC'> fot test | 92.2297 | 92.1331 |
| <class 'sklearn.svm._classes.SVC'> fot train | 96.413 | 96.3957 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot test | 96.2838 | 96.3321 |
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|

#### when tested on balnced test data:-
|          Classifier          | Accuracy | F1 Score |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot test | 85.0 | 84.8807 |
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot train | 89.0942 | 89.0157 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot test | 97.7778 | 97.7832 |
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
| <class 'sklearn.svm._classes.SVC'> fot test | 88.4722 | 88.2609 |
| <class 'sklearn.svm._classes.SVC'> fot train | 98.0072 | 98.0029 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot test | 96.25 | 96.2772 |
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
