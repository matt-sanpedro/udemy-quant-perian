import pandas as pd

registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})
print('Registrations df:\n{}'.format(registrations))
print('Logins df:\n{}'.format(logins))

# merging with indices
registrations = registrations.set_index('name')
df = pd.merge(registrations, logins, left_index=True, right_on='name', how='inner')
print('\nMerge - indices:\n{}'.format(df))

# merging with renamed indices
registrations = registrations.reset_index()
registrations.columns = ['reg_name', 'reg_id']
df = pd.merge(registrations, logins, left_on='reg_name', right_on='name', how='inner')
df = df.drop('reg_name', axis=1)
print('Merge - indices:\n{}'.format(df))

# merging with similar column name df
registrations.columns = ['name', 'id']
logins.columns = ['id', 'name']
print('\nRegistrations df:\n{}'.format(registrations))
print('Logins df:\n{}'.format(logins))
df = pd.merge(registrations, logins, how='inner', on='name', suffixes=('_reg', '_log'))
print('Merge - id col:\n{}'.format(df))
