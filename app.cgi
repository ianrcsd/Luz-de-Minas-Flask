#!/usr/bin/python3

try:
    from wsgiref.handlers import CGIHandler
    from app import app
    from DB_Operations import get_data_menu, get_data_categoria, get_login, get_registro, post_registro, get_tables, get_fields, get_columns, get_menu_item, get_busca, update_row, get_row_data, get_table_data, insert_row, delete_row


    CGIHandler().run(app)
except Exception as err:
    print("Content-Type: text/html\n\n")
    print(err)