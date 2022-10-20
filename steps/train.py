"""
This module defines the following routines used by the 'train' step of the regression pipeline:

- ``estimator_fn``: Defines the customizable estimator type and parameters that are used
  during training to produce a model pipeline.
"""


def estimator_fn(estimator_params = {}):
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    from sklearn.linear_model import LogisticRegression
    from sklearn.multioutput import MultiOutputClassifier
    from sklearn.linear_model import SGDClassifier

    return SGDClassifier(random_state=16, **estimator_params)
