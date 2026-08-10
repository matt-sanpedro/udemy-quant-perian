import pandas as pd

# outer merge allows an output DataFrame with everything present
registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})
print('Registrations df:\n{}'.format(registrations))
print('Logins df:\n{}'.format(logins))

# merge: outer
df = pd.merge(left=registrations, right=logins, how='outer', on='name')
print('\nMerge - outer:\n{}'.format(df))

# since using outer join, the order of left and right does NOT matter
df = pd.merge(left=logins, right=registrations, how='outer', on='name')
print('Merge - outer:\n{}'.format(df))
