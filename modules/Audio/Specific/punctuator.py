import pandas as pd

from punctuator import Punctuator

def punctuate(csv_path, text_col):
    """
    This function returns the csv with the punctuations in a specific column

    Parameters
    -----------
    csv_path: path to the csv file
    text_col: the name of the column that contains the text

    Returns
    -------
    modified csv file
        "Hi Im Alex" to "Hi, I'm Alex."
    """

    p = Punctuator('Demo-Europarl-EN.pcl')

    df = pd.read_csv(csv_path)
    for index, row in df[text_col].iteritems():
        df.at[index, text_col] = p.punctuate(str(row))
        df.to_csv(csv_path, index=False)