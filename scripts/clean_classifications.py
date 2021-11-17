import pandas as pd
from datetime import date


def load(path: str = '../data/classifications_cset.csv') -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.lower().str.replace(
        'classifications.', '').str.replace(' ', '_')
    df['beginning_date'] = pd.to_datetime(
        df['beginning_date'], utc=True).dt.date
    df['ending_date'] = pd.to_datetime(df['ending_date'], utc=True).dt.date
    return df


def save(df: pd.DataFrame) -> None:
    fmt = date.today().strftime('%Y%m%d')
    df.to_csv(f'../data/classifications_processed-{fmt}.csv', index=False)


if __name__ == '__main__':
    save(clean(load()))
