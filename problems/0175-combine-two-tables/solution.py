import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df_merged = pd.merge(person , address, on = 'personId', how="left")
    return df_merged[['firstName', 'lastName', 'city', 'state']]
