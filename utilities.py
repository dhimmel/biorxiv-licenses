import json

import altair

def tidy_split(df, column, sep='|', keep=False):
    """
    Split the values of a column and expand so the new DataFrame has one split
    value per row. Filters rows where the column is missing. Discuss at
    http://stackoverflow.com/a/39946744/4651668.

    Params
    ------
    df : pandas.DataFrame
        dataframe with the column to split and expand
    column : str
        the column to split and expand
    sep : str
        the string used to split the column's values
    keep : bool
        whether to retain the presplit value as it's own row

    Returns
    -------
    pandas.DataFrame
        Returns a dataframe with the same columns as `df`.
    """
    indexes = list()
    new_values = list()
    df = df.dropna(subset=[column])
    for i, presplit in enumerate(df[column].astype(str)):
        values = presplit.split(sep)
        if keep and len(values) > 1:
            indexes.append(i)
            new_values.append(presplit)
        for value in values:
            indexes.append(i)
            new_values.append(value)
    new_df = df.iloc[indexes, :].copy()
    new_df[column] = new_values
    return new_df

def df_to_vega_lite(df, path=None):
    """
    Export a pandas.DataFrame to a vega-lite data JSON.
    
    Params
    ------
    df : pandas.DataFrame
        dataframe to convert to JSON
    path : None or str
        if None, return the JSON str. Else write JSON to the file specified by
        path.
    """
    chart = altair.Chart(data=df)
    data = chart.to_dict()['data']['values']
    kwargs = {'ensure_ascii': False, 'indent': 2, 'sort_keys': True}
    if path is None:
        return json.dumps(data, **kwargs)
    with open(path, 'w') as write_file:
        json.dump(data, write_file, **kwargs)
