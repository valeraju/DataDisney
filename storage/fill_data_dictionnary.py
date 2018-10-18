import pandas as pd
import os

df = pd.DataFrame(pd.date_range(start='10/11/2018', end='12/31/2019'), columns=['DATE', 'TYPE_JOURNEE_SAISON_TARIFAIRE'])
with open(os.path.expanduser('~') + "/DataRaw/data_dictionnary.csv", 'w') as file:
    df.to_csv(file.name, sep='\t', encoding='utf-8')
