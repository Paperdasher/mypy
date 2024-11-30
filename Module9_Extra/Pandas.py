## Pandas
# https://www.w3schools.com/python/pandas/default.asp

"""
As stated earlier, our programs can interact outside of the Python file. 
A big function that many Python programmers use is the Pandas library. This library is powerful, it allows for so much data analysis.
Coding is very valuable in cleaning up data and finding patterns that may help businesses target a specific area or a teacher explain a certain topic more deeply.
Pandas, along with MatPlotLib and Seaborn, are common libraries used by data scientist in order to analyze and visualize data.

For Pandas, we need to import the Pandas library. In many cases, we shorten Pandas to pd, MatPlotLib.pyplot to plt, and Seaborn to sns.
"""

import pandas as pd
import matplotlib.pyplot as plt
import Seaborn as sns

"""
We use csv files to analyze data. CSV(comma-separated values) are like a spreadsheet, and can be opened by spreadsheet apps such as Excel.
Many csv files exist on the internet, and many open source databases provide data based off of studies that are in csv format.

We "read" csv files in order to analyze them. The data file should be in the same folder/directory as the Python file.
"""

df = pd.read_csv("data.csv") # commonly assign variable name df standing for dataframe

"""
We can perform many different operations from here.
"""

df.corr() # shows correlation coefficient of numerical values in the dataset

"""
We can use loc and iloc to "slice" or select what values we'd like to pull out. We can also reassign them to a different variable.
"""
