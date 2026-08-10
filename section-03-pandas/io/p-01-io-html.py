import pandas as pd
import os

tables = pd.read_html(os.path.join(os.path.dirname(__file__), 'World_Population.html'))
print('Found tables: {}'.format(len(tables)))

# print(tables[3].columns)
world_topten = tables[3]
# print(world_topten)
world_topten.columns = ['Country', 'Population', 'Percent', 'Date', 'Source']
print(world_topten)
world_topten.to_html(os.path.join(os.path.dirname(__file__), 'topten_population.html'))
