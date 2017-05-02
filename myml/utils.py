import pandas as pd


def convert_series_of_lists_to_df(column: pd.Series, prefix='', prefix_sep=''):
    """
    input:

     index    groups
        0     ['a','b','c']
        1     ['c']
        2     ['b','c','e']
        3     ['a','c']
        4     ['b','e']

    output:

    index   a   b   c   d   e
        0   1   1   1   0   0
        1   0   0   1   0   0
        2   0   1   1   0   1
        3   1   0   1   0   0
        4   0   1   0   0   0
    """

    return pd.get_dummies(column.apply(pd.Series), prefix=prefix, prefix_sep=prefix_sep).sum(level=0, axis=1)


def plot_features_ditributions(df: pd.DataFrame, target_column: str):

    # Plotting the histogram of every feature per class (0 = no fraud, 1 = fraud)
    columns = sorted(col for col in df.columns if col != target_column)
    width = 2 # int(np.sqrt(len(columns)))
    height = np.ceil(len(columns) / width)
    with plt.rc_context(rc={'figure.figsize': (10, 25)}):
        fig = plt.figure()
        for col_i, col in enumerate(columns):
            fig.add_subplot(height, width, col_i + 1)
            value_range = (df[col].quantile(.01), df[col].quantile(.99))
            # TODO find a way get a good bin numbers check brute force plotter
            df.groupby(target_column)[col].plot.hist(alpha=0.5, normed=True, bins=20, range=value_range)
            plt.title("Feature '{}'".format(col), fontdict=dict(fontsize=10))
    plt.tight_layout()
