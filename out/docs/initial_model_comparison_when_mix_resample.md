#### when tested on row baised test data:-
|          Classifier          | Accuracy | F1 Score |
|------------------------------|----------|----------|
| <class 'sklearn.dummy.DummyClassifier'> fot test | 12.5 | 2.7778 |
| <class 'sklearn.dummy.DummyClassifier'> fot train | 25.0 | 10.0 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._perceptron.Perceptron'> fot test | 63.5135 | 52.503 |
| <class 'sklearn.linear_model._perceptron.Perceptron'> fot train | 58.6957 | 48.7728 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._base.LinearRegression'> fot test | 84.7973 | 85.2886 |
| <class 'sklearn.linear_model._base.LinearRegression'> fot train | 86.558 | 86.7719 |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot test | 88.5135 | 88.4048 |
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot train | 89.6014 | 89.5207 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot test | 96.9595 | 96.9851 |
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
| <class 'sklearn.svm._classes.SVC'> fot test | 92.9054 | 92.682 |
| <class 'sklearn.svm._classes.SVC'> fot train | 96.1232 | 96.0898 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot test | 96.2838 | 96.3385 |
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|

#### when tested on balnced test data:-
|          Classifier          | Accuracy | F1 Score |
|------------------------------|----------|----------|
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot test | 85.5556 | 85.3703 |
| <class 'sklearn.linear_model._logistic.LogisticRegression'> fot train | 89.6014 | 89.5207 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot test | 97.0833 | 97.0827 |
| <class 'sklearn.ensemble._weight_boosting.AdaBoostClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
| <class 'sklearn.svm._classes.SVC'> fot test | 88.6111 | 88.3498 |
| <class 'sklearn.svm._classes.SVC'> fot train | 98.3333 | 98.3271 |
|------------------------------|----------|----------|
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot test | 96.25 | 96.2705 |
| <class 'sklearn.ensemble._forest.RandomForestClassifier'> fot train | 100.0 | 100.0 |
|------------------------------|----------|----------|
