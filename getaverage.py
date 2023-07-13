def sorted_by_year(df, year):
    return df.query("year == @year").drop(columns='year')


def sorted_by_region(df, region):
    return df.query('region == @region').drop(columns='region')


def get_average_by_year_for_regions(df):
    """ Processed dataframe object (avocado's file) then return
    averages prices by region and by year.

     parameters:
     df: dataframe object that will contain information about
      the type of avocado we want to process.

      format of the return object: {year: [(average, region), ...]}"""

    years = df.year.unique()
    regions = df['region'].unique()
    averages = {}

    for year in years:
        data_for_year = sorted_by_year(df, year)
        average_for_regions = []

        for region in regions:
            data_for_region = sorted_by_region(data_for_year, region)
            average_for_region = data_for_region.price.astype(float).mean()
            average_for_regions.append((average_for_region, region))

        averages.update({year: average_for_regions})

    return averages
