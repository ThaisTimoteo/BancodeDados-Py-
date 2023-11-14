#importing things to use:
import pandas as pd
import sqlite3

#creating a tibble for using as database:
data = pd.DataFrame({
    'ID':[1,2,3,4],
    'Name': ['Lily', 'Rose', 'Hydrangea', 'Sunflower'] 
    'Color': ['White','Red', 'Blue','Yellow']
    })

#calling the tibble above:
data

#acessing the sqlite server and oppening the connection:
base = sqlite3.connect('mydatabase.db')

#using the 'to sql' method to save the dataframe to a table:
data.to_sql('tabela_de_flores', base, if_exists='replace', index=False)

#closing the connection to the database:
base.close()