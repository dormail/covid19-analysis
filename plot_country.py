import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd

from element_of import element_of

# if there is only one country (the other functions are based on this one
def plot_one(country,data):
    if type(country) != str:
        raise TypeError

    # extracting info about spcific country
    inf_comul_pd = data[2].loc[data[2]["country/region"] == country]
    inf_change_pd = data[0].loc[data[2]["country/region"] == country]
    deaths_comul_pd = data[3].loc[data[2]["country/region"] == country]
    deaths_comul_pd = data[1].loc[data[2]["country/region"] == country]


    # loading country info into list
    inf_comul, inf_change, deaths_comul, deaths_change = [], [], [], []
    for i in range(1,inf_comul_pd.shape[1]):
        inf_comul.append(inf_comul_pd.iat[0,i])
        deaths_comul.append(deaths_comul_pd.iat[0,i])

        #deaths.append(deaths_temp.iat[0,i])



    # data cleaning
    # removing initial spots that are smaller than minimum (to make graph more readable)
    minimum =  1000
    for i in range(0,len(inf_comul)):
        if inf_comul[0] < minimum:
            inf_comul.pop(0)
            deaths_comul.pop(0)
        else:
            break

    # setting up subplots
    fig = mpl.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(211)

    ax1.set_ylabel("no. of cases")
    ax1.set_title("Confirmed cases of Covid-19 in " + country)

    x = np.linspace(0,len(inf_comul),len(inf_comul))
    zeros = np.zeros(len(inf_comul))
    # filled area:
    ax1.fill_between(x,inf_comul,zeros, color='tomato')
    ax1.fill_between(x,deaths_comul,zeros, color='black')


    # normal plotting:
    #ax1.plot(x,infected, 'tomato')



    #ax.fill_between(x,deaths,np.zeros(len(x)), 'k')



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


