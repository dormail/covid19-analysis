import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd

from element_of import element_of

# if there is only one country (the other functions are based on this one
def plot_one(country,data):
    if type(country) != str:
        raise TypeError

    # extracting info about spcific country
    inf_temp = data[2].loc[data[2]["country/region"] == country]
    deaths_temp = data[3].loc[data[2]["country/region"] == country]

    # loading country info into list
    infected = []
    deaths = []
    for i in range(1,inf_temp.shape[1]):
        infected.append(inf_temp.iat[0,i])
        deaths.append(deaths_temp.iat[0,i])


    # data cleaning
    # removing initial spots that are smaller than minimum (to make graph more readable)
    minimum =  1000
    for i in range(0,len(infected)):
        if infected[0] < minimum:
            infected.pop(0)
            deaths.pop(0)
        else:
            break

    # setting up subplots
    fig = mpl.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(211)

    ax1.set_ylabel("no. of cases")
    ax1.set_title("Confirmed cases of Covid-19 in " + country)

    x = np.linspace(0,len(infected),len(infected))
    zeros = np.zeros(len(infected))
    # filled area:
    ax1.fill_between(x,infected,zeros, color='tomato')
    ax1.fill_between(x,deaths,zeros, color='black')


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


