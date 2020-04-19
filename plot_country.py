import matplotlib.pyplot as mpl
import numpy as np
import math

from element_of import element_of
from comulate import comulate
from minimum import minimum


# if there is only one country (the other functions are based on this one
def plot_one(country,data):
    if type(country) != str:
        raise TypeError

    # extracting info about spcific country
    inf_change_pd = data[0].loc[data[2]["country/region"] == country]
    deaths_change_pd = data[1].loc[data[2]["country/region"] == country]

    # scaling the change op by the factor n
    n = 5

    # loading country info into list
    days = inf_change_pd.shape[1]
    inf_change = np.zeros(days, dtype='i')
    deaths_change = inf_change.copy()

    for i in range(1,days):
        inf_change[i] = inf_change_pd.iat[0,i]
        deaths_change[i] = deaths_change_pd.iat[0,i]

    inf_comul = comulate(inf_change)
    deaths_comul = comulate(deaths_change)

    # data cleaning
    # removing initial spots that are smaller than minimum (to make graph more readable)
    minimum_inf =  1000
    zeros, inf_comul = minimum(inf_comul, minimum_inf)
    for i in range(0,zeros):
        inf_change = np.delete(inf_change,0)
        deaths_comul = np.delete(deaths_comul,0)
        deaths_change = np.delete(deaths_change,0)

    # the change plot is to wavey to see real change
    # splitting up in x(splits) day-intervalls, to remove noise
    splits = 5
    days = len(inf_comul)
    three_day_intervalls = math.floor(days/splits)
    if (days % splits != 0):
        three_day_intervalls = three_day_intervalls + 1
    inf_cleaned = np.zeros(three_day_intervalls, dtype='i')
    # adding the intervall together by iteration through the lists
    for i in range(0,len(inf_cleaned)-1):
        tmp = 0
        for j in range(0,splits):
            tmp = tmp + inf_change[splits*i + j]
        inf_cleaned[i] = tmp
    # adding the last interval manually
    tmp = 0
    for i in range(0,days % splits):
        tmp = tmp + inf_change[-1*(i+1)]
    try:
        inf_cleaned[-1] = tmp * splits / (days % splits)
    except ZeroDivisionError:
        inf_cleaned[-1] = tmp
    # creating new array with cleaned data, i length of the 
    inf_change_cleaned = np.zeros(days, dtype='i')


    # setting up subplots
    fig = mpl.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(211)

    ax1.set_ylabel("no. of cases")
    ax1.set_title("Confirmed cases of Covid-19 in " + country)

    x = np.linspace(0, len(inf_comul), len(inf_comul))
    x3 = np.linspace(0, splits*len(inf_cleaned), len(inf_cleaned))

    zeros = np.zeros(len(inf_comul))
    # filled area:
    ax1.fill_between(x, inf_comul, zeros, color='tomato')
    ax1.fill_between(x, deaths_comul, zeros, color='black')

    # normal plot (for change)
    ax1.plot(x3, inf_cleaned, 'b+')


# plot multiple countries
def plot_many(countries,data):
    for i in range(0,len(countries)):
        plot_one(countries[i], data)


# checking if there if just one country or multpiple countries
def plot_country(country,data):
    if type(country) == str:
        plot_one(country, data)
    elif type(country) == list:
        plot_many(country,data)

    mpl.show()
