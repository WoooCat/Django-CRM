from django.db import connection

# Створення бази даних PostgreSQL
with connection.cursor() as cursor:
    cursor.execute("CREATE DATABASE crm_database")


print("All Done!")
