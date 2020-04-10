import numpy as np
import pandas as pd

from element_of import element_of

def convert(source):
    # loading source data from excel sheet in pandas DataFrame
    source = pd.read_excel(source)
    
    # loading a list of countries from the xlsx
    temp = source["countriesAndTerritories"]
    countries = []
    for i in range(0,len(temp)):
        if element_of(temp[i],countries):
            continue
        else:
            countries.append(temp[i])

    # loading a list of all present dates
    temp = [source["year"], source["month"], source["day"]]
    dates = []
    
    for i in range(0,len(temp[0])):
        tmp = [temp[0][i], temp[1][i], temp[2][i]]
        if element_of(tmp,dates):
            continue
        else:
            dates.append(tmp)
    
    #sorting dates
    dates.sort()
    
    # converting the list of dates from array type to string type
    temp = []
    for i in range(0,len(dates)):
        temp.append(str(dates[i][0]) + "/" + str(dates[i][1]) + "/" + str(dates[i][2]))
    
    dates_string = temp.copy()
    
    
    # adding new DataFrame
    # dest is a template for later DataFrames in the analysis
    dest = pd.DataFrame()
    
    # adding list of countries
    dest["country/region"] = countries
    
    # adding columns for all the dates
    temp = np.zeros(len(dest["country/region"]))
    for i in range(0,len(dates_string)):
        dest[dates_string[i]] = temp.copy()
    
    # loading data from source to dest
    
    # generating DataFrames from dest as a template
    infected_change = dest.copy()
    deaths_change = dest.copy()
    infected_sum = dest.copy()
    deaths_sum = dest.copy()
    
    for i in range(0,len(countries)):
        tmp = source.loc[source["countriesAndTerritories"] == countries[i], ["cases","deaths","countriesAndTerritories"]]
        
        cases = tmp["cases"].tolist()
        deaths = tmp["deaths"].tolist()
        
        
        # adding in zeros (not alle countries list all the dates)
        for j in range(0,len(dates_string) - len(cases)):
            cases.append(0)
            deaths.append(0)
        
        # the excel starts with most recent date, we start with oldest -> need to reverse list
        cases.reverse()
        deaths.reverse()
        
        # injection in dataframes
        # using counters to get the accumulated table
        counter_deaths = 0
        counter_infected = 0
        for j in range(0,len(cases)):
            counter_infected += cases[j]
            counter_deaths += deaths[j]
            
            infected_change.iat[i, j+1] = cases[j]
            deaths_change.iat[i, j+1] = deaths[j]
            infected_sum.iat[i, j+1] = counter_infected
            deaths_sum.iat[i, j+1] = counter_deaths


    infected_change.to_csv("infected_new.csv")
    deaths_change.to_csv("deaths_new.csv")
    infected_sum.to_csv("infected_overall.csv")
    deaths_sum.to_csv("deaths_overall.csv")

