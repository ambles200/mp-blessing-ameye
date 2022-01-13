import pymysql
import os
from dotenv import load_dotenv
from tabulate import tabulate


# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")


# Establish a database connection
def execute_query(statement, host=host, user=user, password=password, database=database):
    connection = pymysql.connect(
        host=host, user=user, password=password, database=database, autocommit=True, port=3306)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(statement)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


# ------Main Menu Options ------------
def menu_1():
    main_menu = "\n====== Main Menu ======\n0. Exit App\n1. Products Menu\n2. Couriers Menu\n3. Orders Menu"
    print(main_menu)


# ------Sub Menu Options ------------
def menu_2():
    sub_menu = "\n====== Product Menu ======\n0. Main Menu\n1. See Products\n2. Add New Product\n3. Update Product\n4. Delete product"
    print(sub_menu)


# ------Courier Menu Options ------------
def menu_3():
    courier_menu = "\n======= Couriers Menu =======\n0. Main Menu\n1. Choose a courier\n2. Create New Courier\n3. Update Courier Details\n4. Remove Courier"
    print(courier_menu)


# ------Orders Menu Options ------------
def menu_4():
    orders_menu = "\n======= Orders Menu =======\n0. Main Menu\n1. See Orders\n2. Create New Order\n3. Update Order Status\n4. Update Order\n5. Delete Order"
    print(orders_menu)


# -----------------Product Update----------------------------
def write_list_to_file(products_list, product_path):
    with open(product_path, "w") as f:
        for product in products_list:
            f.write(product + "\n")


def read_file_list(product_path):
    with open(product_path, "r") as f:
        product_list = f.read().splitlines()
        return product_list


# -------------------Order Status List---------------------------
# def order_status_list():
#     order_status = ["Preparing", "Out for delivery", "Delivered"]
#     return order_status


def pretty_table(records):
    header = records[0].keys()
    rows = [x.values() for x in records]
    print("\n", tabulate(rows, headers=header))
