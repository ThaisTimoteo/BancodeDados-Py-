from functions.create_table import create_table
from functions.insert_rows import insert_many_rows

create_table("database.db","nome","id_nome PRIMARY KEY, nome TEXT NOT NULL, id_idade INT")
create_table("database.db","idade"," id_idade PRIMARY KEY, idade INTEGER NOT NULL")

# inserting rows
insert_many_rows(database_name="database.db",
       table_name="nome",
       columns_name="id_nome,nome,id_idade",
       list_values=[(1,'Rafael',1),(2,'Rumble',2),(3,'Silvio',3),(4,'Batata',4)])
insert_many_rows(database_name="database.db",
       table_name="idade",
       columns_name="id_idade,idade",
       list_values=[(44,23),(12,56),(333,79),(455,18)])