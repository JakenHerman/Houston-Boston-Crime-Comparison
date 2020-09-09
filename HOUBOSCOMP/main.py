# Houston Crime Statistics for 2018 Sourced by Houston, Texas Police Dept:
# http://www.houstontx.gov/police/cs/crime-stats-archives.htm

# Boston Crime Statistics for 2018 Sourced By Analyze Boston:
# https://data.boston.gov/

# import necessary packages and libraries
from glob import glob
import pandas as pd


# take all 2018 houston csv files and combine them in one DataFrame
def combine_houston_data():
    all_files = glob('../data/*.csv')
    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, encoding='windows-1252', low_memory=False)
        li.append(df)

    return pd.concat(li, axis=0, ignore_index=True)


# set up our boston crime data variable
boston_data = pd.read_csv('../data/BOS.csv', encoding='windows-1252', low_memory=False)


# set up our houston crime data variable
houston_data = combine_houston_data()


if __name__ == '__main__':
    print('')
