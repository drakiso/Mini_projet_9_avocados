import operator
from getaverage import get_average_by_year_for_regions


def display_statistic_avocados(df, type_avocados):
    """display statistic about the lowest and highest average price for each type
    of avocados by region and year and also give the lowest and highest price
    of all time for each type.

    parameters:

    df : dataframe object that contains all the information about avocado
    type_avocados: the type of avocado that will be processed"""

    avocado = df.query("type == @type_avocados").copy()
    avocado.drop(columns='type', inplace=True)

    avocado_average = get_average_by_year_for_regions(avocado)

    print(f"Regions which had the lowest average price "
          f"for {type_avocados} avocados each year:")

    for year, data in avocado_average.items():
        price, location = min(data, key=operator.itemgetter(0))

        print(f"{year} ==> Region: {location}, Price: ${price:.2f}")

    print("\nRegions which had the highest average price "
          f"for {type_avocados} avocados each year:")

    for year, data in avocado_average.items():
        price, location = max(data, key=operator.itemgetter(0))

        print(f"{year} ==> Region: {location}, Price: ${price:.2f}")

    print(f"\nLowest all time price for {type_avocados} avocados: "
          f"${avocado.price.min()}")

    print(f"Highest all time price for {type_avocados} avocados: "
          f"${avocado.price.max()}")

    print("--------------------------------------------------------------------------\n")
