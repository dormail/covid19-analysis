import pandas as pd
import numpy as np

from convert_format import convert
from plot_country import plot_country

# adding the excel via download
FilePlace = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-04-10.xlsx"

# loading pandas DataFrames from the excel
# structure of data:
# data = [infected_change,deaths_change,infected_sum,deaths_sum]
data = convert(FilePlace, False)

country = ["Germany","Italy"]

plot_country(country,data)
