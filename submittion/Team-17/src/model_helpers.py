import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve
from sklearn.model_selection import LearningCurveDisplay, ShuffleSplit
from sklearn.model_selection import learning_curve

'''
    a method to help u draw a validation curve
'''
def draw_validation_curve(x, y, classifier ,param_name="gamma", param_range=np.logspace(-4, 3, 10), scoring="f1_weighted", n_jobs=2,y_lim=0.0, cv=5):
    
    train_scores, test_scores = validation_curve(
        classifier,
        x,
        y,
        param_name=param_name,
        param_range=param_range,
        scoring=scoring,
        n_jobs=n_jobs,
        cv=cv
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.title(f'Validation Curve with {str(classifier.__class__.__name__)}')
    plt.xlabel(r"$\gamma$")
    plt.ylabel("Score")
    plt.ylim(y_lim, 1.1)
    lw = 2
    plt.semilogx(
        param_range, train_scores_mean, label="Training score", color="darkorange", lw=lw
    )
    plt.fill_between(
        param_range,
        train_scores_mean - train_scores_std,
        train_scores_mean + train_scores_std,
        alpha=0.2,
        color="darkorange",
        lw=lw,
    )
    plt.semilogx(
        param_range, test_scores_mean, label="Cross-validation score", color="navy", lw=lw
    )
    plt.fill_between(
        param_range,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.2,
        color="navy",
        lw=lw,
    )
    plt.legend(loc="best")
    plt.show()
    return test_scores_mean, train_scores_mean

'''
    a method to help u draw the learning curve
'''
def draw_learning_curve(x, y, classifier, train_sizes=np.linspace(0.1, 1.0, 10), score_name="f1_weighted", n_jobs=10, cv_n_splits=10):
    fig, ax = plt.subplots( figsize=(5, 7), sharey=True)

    common_params = {
        "X": x,
        "y": y,
        "train_sizes": train_sizes,
        "cv": ShuffleSplit(n_splits=cv_n_splits, test_size=0.2, random_state=0),
        "score_type": "both",
        "n_jobs": n_jobs,
        "line_kw": {"marker": "o"},
        "std_display_style": "fill_between",
        "score_name": score_name,
    }


    LearningCurveDisplay.from_estimator(classifier, **common_params, ax=ax)
    handles, label = ax.get_legend_handles_labels()
    ax.legend(handles[:2], ["Training Score", "Test Score"])
    ax.set_title(f"Learning Curve for {classifier.__class__.__name__}")

'''
    draw complecity analysis
'''
def draw_scalability_curves(x, y, classifier, train_sizes=np.linspace(0.1, 1.0, 5), score_name="f1_weighted", n_jobs=10, cv_n_splits=10):
    common_params = {
        "X": x,
        "y": y,
        "train_sizes": train_sizes,
        "cv": ShuffleSplit(n_splits=cv_n_splits, test_size=0.2, random_state=0),
        "n_jobs": n_jobs,
        "return_times": True,
        "scoring": score_name
    }


    train_sizes, _, test_scores, fit_times, score_times = learning_curve(
        classifier, **common_params
    )
    print(score_times)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 12), sharex=True)

    # scalability regarding the fit time
    ax[0].plot(train_sizes, fit_times.mean(axis=1), "o-")
    ax[0].fill_between(
        train_sizes,
        fit_times.mean(axis=1) - fit_times.std(axis=1),
        fit_times.mean(axis=1) + fit_times.std(axis=1),
        alpha=0.3,
    )
    ax[0].set_ylabel("Fit time (s)")
    ax[0].set_title(
        f"Fit time Scalability of the {classifier.__class__.__name__} classifier"
    )

    # scalability regarding the score time
    ax[1].plot(train_sizes, score_times.mean(axis=1), "o-")
    ax[1].fill_between(
        train_sizes,
        score_times.mean(axis=1) - score_times.std(axis=1),
        score_times.mean(axis=1) + score_times.std(axis=1),
        alpha=0.3,
    )
    ax[1].set_ylabel("Score time (s)")
    ax[1].set_xlabel("Number of training samples")
    ax[1].set_title(
        f"Score time Scalability of the {classifier.__class__.__name__} classifier"
    )

    fig, ax = plt.subplots(figsize=(8, 3))


    ax.plot(fit_times.mean(axis=1), test_scores.mean(axis=1), "o-")
    ax.fill_between(
        fit_times.mean(axis=1),
        test_scores.mean(axis=1) - test_scores.std(axis=1),
        test_scores.mean(axis=1) + test_scores.std(axis=1),
        alpha=0.3,
    )
    ax.set_ylabel("f1_weighted")
    ax.set_xlabel("Fit time (s)")
    ax.set_title(
        f"Performance of the {classifier.__class__.__name__} classifier"
    )

    plt.show()

    return fit_times, score_times