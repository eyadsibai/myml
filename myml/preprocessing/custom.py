from collections import Iterable
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class OneHotEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        # TODO this should work with numpy arrays/ dataframes
        self._columns = None

    def fit(self, X):
        self._columns = self._one_hot_dataframe(X).columns
        return self

    def get_feature_names(self):
        return self._columns

    def transform(self, X):
        assert isinstance(self._columns, Iterable)
        result = self._one_hot_dataframe(X)
        result = result[self._columns]
        for col in self._columns:
            if col not in result.columns:
                result[col] = 0
        return result[self._columns]

    @staticmethod
    def _one_hot_dataframe(data: pd.Series) -> pd.Series:
        """ Takes a dataframe and a list of columns that need to be encoded.
        Returns the vectorized data
        """
        dummy_na = not all(data.notnull())
        result = pd.get_dummies(data, prefix=data.name, prefix_sep='=',
                                dummy_na=dummy_na)

        return result
