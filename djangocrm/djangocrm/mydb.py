from django.db import connection


with connection.cursor() as cursor:
    cursor.execute("CREATE DATABASE crm_database")

# print("All Done!")
