import pandas as pd

registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})
print('Registrations df:\n{}'.format(registrations))
print('Logins df:\n{}'.format(logins))

# merge: left
df_left = pd.merge(left=registrations, right=logins, how='left', on='name')
print('\nMerge - left join:\n{}'.format(df_left))

# merge: right
df_right = pd.merge(left=registrations, right=logins, how='right', on='name')
print('Merge - right join:\n{}'.format(df_right))
