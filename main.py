"""Program that processing avocado.csv file then give statistic about
the lowest and highest average price for each type of avocados by region and year
and also give the lowest and highest price of all time for each type."""

import csv
import pandas as pd
from displaystatistic import display_statistic_avocados


with open('avocado.csv') as data_file:
    df = pd.DataFrame(csv.DictReader(data_file))
    df = df[['AveragePrice', 'type', 'year', 'region']].rename(
        columns={'AveragePrice': 'price'})

    display_statistic_avocados(df, 'conventional')
    display_statistic_avocados(df, 'organic')
