import collections
import json
import logging
import functools
import re

import altair
import nameparser
import probablepeople

json_dump_kwargs = {
    'ensure_ascii': False,
    'indent': 2,
    'sort_keys': True,
}

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
    if path is None:
        return json.dumps(data, **json_dump_kwargs)
    with open(path, 'w') as write_file:
        json.dump(data, write_file, **json_dump_kwargs)

def df_to_datatables(df, path=None, double_precision=5, indent=2):
    """
    Convert a pandas dataframe to a JSON object formatted for datatables input.
    """
    dump_str = df.to_json(orient='split', double_precision=double_precision)
    obj = json.loads(dump_str)
    del obj['index']
    obj = collections.OrderedDict(obj)
    obj.move_to_end('data')
    if path is None:
        return json.dumps(obj, **json_dump_kwargs)
    with open(path, 'w') as write_file:
        json.dump(obj, write_file, **json_dump_kwargs)

# Invalid name characters from http://stackoverflow.com/q/1261338/4651668
invalid_name = re.compile(r"[<,\"@/{}*$%?=>:|;#]")

@functools.lru_cache(maxsize=10**6)
def get_standard_author(author):
    """
    Given a bioRxiv author, return their name in 'first last' format. Return
    `None` if the author is detected to be erroneous or not an invdivual.
    """
    author = author.rstrip(',*;')
    author_lower = author.lower()
    if 'consortium' in author_lower:
        logging.info('"{}" removed as a consortium'.format(author))
        return None
    if 'project' in author_lower:
        logging.info('"{}" removed as project'.format(author))
        return None
    if re.search(invalid_name, author):
        logging.info('"{}" removed due to invalid characters'.format(author))
        return None
    name = nameparser.HumanName(author)
    standard_author = '{} {}'.format(name.first, name.last)
    return standard_author
