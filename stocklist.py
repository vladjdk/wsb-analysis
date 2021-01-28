from ftplib import FTP
import os
import pandas as pd

def retrfiles():
    ftp = FTP('ftp.nasdaqtrader.com')
    ftp.login()

    ftp.cwd('SymbolDirectory')

    path = os.path.join('./', 'files', 'stocklist')
    if not os.path.isdir(path):
        os.makedirs(path)

    with open('./files/stocklist/nasdaqlisted.txt', 'wb') as fp:
        ftp.retrbinary('RETR nasdaqlisted.txt', fp.write)

    with open('./files/stocklist/otherlisted.txt', 'wb') as fp:
        ftp.retrbinary('RETR otherlisted.txt', fp.write)



def retrdataframe():
    retrfiles()

    dfs = []

    nasdaq_df = pd.read_csv('./files/stocklist/nasdaqlisted.txt', '|')
    nasdaq_df = nasdaq_df[:-1]
    nasdaq_df.rename(columns={'Security Name': 'Name'}, inplace=True)
    nasdaq_df['Exchange'] = 'NASDAQ'
    nasdaq_df = nasdaq_df[['Symbol', 'Name', 'Round Lot Size', 'Test Issue', 'Exchange']].reset_index(drop=True)
    dfs.append(nasdaq_df)


    other_df = pd.read_csv('./files/stocklist/otherlisted.txt', '|')
    other_df = other_df[:-1]
    other_df.rename(columns={'ACT Symbol': 'Symbol', 'Security Name': 'Name'}, inplace=True)
    other_df.loc[other_df['Exchange'] == 'A', 'Exchange'] = 'NYSE MKT'
    other_df.loc[other_df['Exchange'] == 'N', 'Exchange'] = 'NYSE'
    other_df.loc[other_df['Exchange'] == 'P', 'Exchange'] = 'NYSE ARCA'
    other_df.loc[other_df['Exchange'] == 'Z', 'Exchange'] = 'BATS'
    other_df.loc[other_df['Exchange'] == 'V', 'Exchange'] = 'IEXG'
    other_df = other_df[['Symbol', 'Name', 'Round Lot Size', 'Test Issue', 'Exchange']].reset_index(drop=True)
    dfs.append(other_df)


    combined_df = pd.concat(dfs, axis=0).drop_duplicates(subset='Symbol').reset_index(drop=True)

    return combined_df
