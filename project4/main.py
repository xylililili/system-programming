from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from query_function import query1, query2, query3, query4, query5
from tables import team
engine = create_engine('postgresql://postgres:passw0rd@localhost/ACC_BBALL')

# try:
connection = engine.connect()
print('Opened database successfully: ACC_BBALL')
query1(engine, 1, 20, 30, 1, 10, 20, 1, 2, 5, 1, 1, 3, 1, 1, 2, 1, 0, 1);
query1(engine, 1, 35, 40, 0, 10, 20, 0, 2, 5, 0, 1, 3, 0, 1, 2, 0, 0, 1);
query2(engine, "Maroon")
query3(engine, "Duke");
query4(engine, "VA", "Maroon")
query5(engine, 10)
# query5(engine,10)
# query4(engine, "VA", "Maroon");
# query3(engine, "Duke");
# query1(engine,
#         1, 20, 30,
#         1, 10, 20,
#         1, 2, 5,
#         1, 1, 3,
#         1, 1, 2,
#         1, 0, 1
#         )
#query2(engine, "Red")
# except:
#     print('Connection failed.')

