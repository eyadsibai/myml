import pandas as pd


def convert_column_of_lists_to_df(column: pd.Series, prefix='', prefix_sep=''):
    """

    :param df:
    :param column_name:
    :return:

            index groups
        0     ['a','b','c']
        1     ['c']
        2     ['b','c','e']
        3     ['a','c']
        4     ['b','e']


        output

        index  a   b   c   d   e
        0      1   1   1   0   0
        1      0   0   1   0   0
        2      0   1   1   0   1
        3      1   0   1   0   0
        4      0   1   0   0   0

    """

    return pd.get_dummies(column.apply(pd.Series), prefix=prefix, prefix_sep=prefix_sep).sum(level=0, axis=1)
