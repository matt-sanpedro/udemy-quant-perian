import numpy as np
import pandas as pd

# pandas series object
# help(pd.Series)

country_indices = ['USA', 'Canada', 'Mexico']
indep_year = [1776, 1867, 1821]
# country_series = pd.Series(data=indep_year, index=country_indices)
country_series = pd.Series(indep_year, country_indices)

print(country_series)
print("\nThis pandas series is of data type: {}".format(type(country_series)))

# can use numeric or label indices
print(country_series[0]) # throws warning: treating keys as positions (deprecated)
print(country_series['USA'])

# dictionaries
ages = {
    'Sam': 5,
    'Frank': 10,
    'Spike': 7
}
ages_series = pd.Series(ages)
print('Frank is {} years old!'.format(ages_series['Frank']))
