"""
Author: Humeyra Copoglu
Date: 25-04-2022
Content: BIN-1a OWE4 Afvinkopdracht 3B
"""
import mysql.connector as sql
success = False

try:
    sql.connect(host='145.74.104.145',
                user='ebcra',
                password='Aa644370!',
                db='blok3')
except Exception as e:
    print("Caught exception: ", e)
    success = False
else:
    success = True

# sql.connect(host='ensembldb.ensembl.org',
#             user='anonymous',
#             db='homo_sapiens_core_95_38')
