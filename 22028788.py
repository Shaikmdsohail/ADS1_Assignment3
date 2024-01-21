
"""
Name: Shaik Mohammed Sohail
Student ID: 22028788
Course: 7PAM2000-0901-2023 - Applied Data Science 1
Assignment 3: Clustering and Fitting
University: Msc Data Science (SW) with Placement Year
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def readFile(fileName):
    '''
    Parameters
    ----------
    fileName: The argument which parsed from main function is the filename for the dataset

    Returns
    -------
    This function reads the csv file and filters the data as per the requirement.
    '''
    
    db = pd.read_csv(fileName,skiprows = 3)
    db.set_index('Country Name', inplace=True)
    
    db_f = db[db["Indicator Code"] == "EN.ATM.GHGT.ZG"]
    db_p = db[db["Indicator Code"] == "SP.POP.GROW"]
    
    period = ["2000","2002","2004","2006","2008","2010","2012","2014","2016","2018"]
    
    db_fw = db_f[period]
    db_pg = db_p[period]
    
    db_fw = db_fw.loc[["United Kingdom", "China", "United States", "India","Germany"]]
    db_pg = db_pg.loc[["United Kingdom", "China", "United States", "India","Germany"]]
    
    db_fw_T = db_fw.transpose()
    db_pg_T = db_pg.transpose()
    
    
    return db_fw, db_fw_T, db_pg, db_pg_T

def Line(df):
    '''
    Parameters
    ----------
    df : This is the dataframe parsed from the main function from plotting the line graph

    Returns
    -------
    The function return nothng but plots the Line graph for the parsed data frame.
    '''
    
    df.plot(kind="line", figsize=(10, 5))
    plt.title("Total Emission of Green House gases")
    plt.xlabel("Year")
    plt.ylabel("Percentage of Emission")
    plt.legend()
    plt.show()
    


def Bar(data,data1):
    '''

    Parameters
    ----------
    data : The data is parsed argument from main fnction which should be the dataframe type.
    data1 : This the dataframe parsed from main function which contains data regarding population growth

    Returns
    -------
    The function return nothng but plots the bar graph for the parsed data frame.
    '''
    
    data = data.loc[:,["2000","2006","2012","2018"]]
    data1 = data1.loc[:,["2000","2006","2012","2018"]]
    
    data.plot(kind="bar", figsize=(10, 5))
    plt.title("Total Emission of Green House gases")
    plt.xlabel("Countries")
    plt.ylabel("Percentage of Emission")
    plt.legend()
    plt.show()
    
    data1.plot(kind="bar", figsize=(10, 5))
    plt.title("Total Population Growth")
    plt.xlabel("Countries")
    plt.ylabel("Count Population Growth")
    plt.legend()

def exponential_growth(x,a,b):
    return a * np.exp(b * x)



#Main Function
dataset = "API_19_DS2_en_csv_v2_6300757.csv"
db_Fw, db_Fw_T, db_Pg, db_Pg_T = readFile(dataset)

Bar(db_Fw,db_Pg)

Line(db_Fw_T)

db = pd.read_csv(dataset,skiprows = 3)
db = db[db["Indicator Code"] == "EN.ATM.GHGT.ZG"]
db = db[db["Country Name"] == "China"]
period = ["2000","2002","2004","2006","2008","2010","2012"]
db = db[period]


xdata = np.array(["2000","2002","2004","2006","2008","2010","2012"])
ydata = np.array(db.values.flatten())

initial_guess = [1.0, 0.1]  # Adjust these values based on your data
popt, pcov = curve_fit(exponential_growth, xdata, ydata, p0=initial_guess, maxfev=1000)


xdata = np.array([int(year) for year in xdata])
x_fit = np.linspace(min(xdata), max(xdata), 100)
y_fit = exponential_growth(x_fit, *popt)

plt.scatter(xdata, ydata, label='Data')
plt.plot(x_fit, y_fit, label='Fitted Curve', color='red')
plt.title('Exponential Growth Curve Fit')
plt.xlabel('Year')
plt.ylabel('Emission Value')
plt.legend()
plt.show()

