import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd

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
    minimum =  500
    for i in range(0,len(infected)):
        if infected[0] < minimum:
            infected.pop(0)
            deaths.pop(0)
        else:
            break

    fig, ax = mpl.subplots()

    x = np.linspace(0,len(infected),len(infected))
    mpl.fill_between(x,infected,np.zeros(len(x)), 'tomato')
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


