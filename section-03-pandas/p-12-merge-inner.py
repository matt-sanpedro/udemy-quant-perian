import pandas as pd

"""
merge: combines two DataFrames or series objects with flexible, SQL-style join operations
    - evaluates matching keys between a "left" and "right" dataset
    - contructs a newly combined DataFrame
    - the .merge() method takes in a key argument labeled how with three values:
        1. inner
        2. outer
        3. left or right
    - the on column 
        1. primary identifier (unique per row)
        2. present on both tables being merged
        3. this example, assume names are unique and merge is on="name"
    - merging with how="inner" outputs set of records that match both tables
"""
registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})
print('Registrations df:\n{}'.format(registrations))
print('Logins df:\n{}'.format(logins))

# merge: inner join
df = pd.merge(registrations, logins, how='inner', on='name')
print('Merge - inner join:\n{}'.format(df))

# since using inner join, the order of left and right does NOT matter
df = pd.merge(logins, registrations, how='inner', on='name')
print('Merge - inner join:\n{}'.format(df))
