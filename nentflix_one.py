import numpy as np
import pandas as pd


def gat_counts():
    csvfile = pd.read_csv("netflix_titles.csv")
    years = np.array(csvfile.release_year)
    years_unique = np.flip(np.unique(years))
    count_arr = np.bincount(years)
    counts = [count_arr[a] for a in years_unique]
    end = pd.Series(data=counts, index=years_unique)
    return end

#
# print(gat_counts())
