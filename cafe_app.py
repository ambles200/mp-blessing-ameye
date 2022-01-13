from pymysql.connections import Connection
import myFunctions

# PRINT main menu options
while True:
    myFunctions.menu_1()
# GET user input for main menu option
    main_nav = int(input("Make a selection: "))
    if main_nav == 0:
        break

# ELSE IF user input is 1:
    elif main_nav == 1:
        while True:
            # PRINT product menu options
            myFunctions.menu_2()
# GET user input for product menu option
            sub_nav = int(input("Please choose an option: "))

# IF user inputs 0:
# RETURN to main menu
            if sub_nav == 0:
                break

# ELSE IF user input is 1:
# PRINT products list
            elif sub_nav == 1:
                while True:
                    myFunctions.pretty_table(
                        myFunctions.execute_query("SELECT * from product"))
                    break
# ELSE IF user input is 2:
# INSERT product into products table
            elif sub_nav == 2:
                while True:
                    new_prod = input("Enter new product: ")
                    new_price = input("Enter new product price: ")
                    myFunctions.execute_query(
                        f"INSERT INTO product (prod_name, price) VALUES ('{new_prod}', {new_price})")
                    print("New product added!")
                    print("\n")
                    myFunctions.pretty_table(
                        myFunctions.execute_query("SELECT * from product"))
                    break

# ELSE IF user input is 3:
# UPDATE properties for product in product table
            elif sub_nav == 3:
                while True:
                    print("Before updating record!")
                    myFunctions.pretty_table(myFunctions.execute_query(
                        "select prod_id, prod_name from product"))

                    prod_id = int(input(
                        "Enter Product ID: "))
                    prod_update = input(
                        "Select an update option: \n1. Product Name\n2. Product Price\n3. Both\n ")
                    if prod_update == "1":
                        prod_name = input("Enter updated product name: ")
                        sqlUpdate = f"UPDATE product SET prod_name = '{prod_name}' WHERE prod_id = {prod_id}"
                    elif prod_update == "2":
                        price = float(input("Enter updated price: "))
                        sqlUpdate = f"UPDATE product SET price = {price} WHERE prod_id = {prod_id}"
                    elif prod_update == "3":
                        prod_name = input("Enter updated product name: ")
                        price = float(input("Enter updated price: "))
                        sqlUpdate = f"UPDATE product SET prod_name = '{prod_name}', price = {price} WHERE prod_id = {prod_id}"
                    else:
                        print("Nothing Updated!")

                    myFunctions.execute_query(sqlUpdate)
                    myFunctions.pretty_table(myFunctions.execute_query(
                        "SELECT prod_id, prod_name from product"))
                    print("Product updated successfully!")
                    break

# DELETE product at index in my_products list
            else:
                sub_nav == 4
                print("Before deleting record!")
                myFunctions.pretty_table(myFunctions.execute_query(
                    "select prod_id, prod_name from product"))
                # Get product ID to be deleted
                prod_id = int(input("Enter product ID to be deleted: "))
                # Delete Product
                delete_prod = f"DELETE from product WHERE prod_id = {prod_id}"
                myFunctions.execute_query(delete_prod)
                print("/n")
                myFunctions.pretty_table(myFunctions.execute_query(
                    "SELECT prod_id, prod_name from product"))
                print("Product successfully deleted!")
                break


# # couriers menu
# ELSE IF user input is 2:
    elif main_nav == 2:
        while True:
            # PRINT courier menu options
            myFunctions.menu_3()
            # IF user inputs 0:
            # RETURN to main menu
            cour_nav = int(input("Please select an option: "))
            if cour_nav == 0:
                break
                # ELIF user inputs 1:
            elif cour_nav == 1:
                while True:
                    # PRINT couriers list
                    myFunctions.pretty_table(
                        myFunctions.execute_query("SELECT * from courier"))
                    break

                # ELSE IF user input is 2:
                # CREATE new courier
            elif cour_nav == 2:
                while True:
                    # Print Courier list
                    myFunctions.pretty_table(
                        myFunctions.execute_query("SELECT * from courier"))
                    # Get user input for new courier
                    new_cour = input("Enter Courier Name: ")
                    new_cour_ph = input("Enter phone number for new courier: ")
                    myFunctions.execute_query(
                        f"insert into courier (courier_name, phone) Values ('{new_cour}', {new_cour_ph})")
                    myFunctions.pretty_table(
                        myFunctions.execute_query("SELECT * from courier"))
                    print("New Courier added successfully!")
                    break

                # ELSE IF user input is 3:
                # UPDATE existing courier
            elif cour_nav == 3:
                # Print courier list
                myFunctions.pretty_table(
                    myFunctions.execute_query("Select * from courier"))
                courier_id = int(input(
                    "Enter Courier ID "))
                courier_name = str(input("Enter New Courier Name: "))
                if courier_name == "":
                    print("Nothing updated")
                else:
                    sqlUpdate = f"UPDATE courier SET courier_name = '{courier_name}' WHERE courier_id = {courier_id}"
                    myFunctions.execute_query(sqlUpdate)
                    myFunctions.pretty_table(myFunctions.execute_query(
                        "select * from courier"))
                    print("Courier updated successfully")
                    break

                # ELSE IF user input is 4:
                # DELETE courier
            else:
                cour_nav == 4
                # Print courier list
                print("Before deleting record!")
                myFunctions.pretty_table(
                    myFunctions.execute_query("Select * from courier"))

                courier_id = int(input("Enter courier ID to be deleted: "))
                del_cour = f"DELETE from courier WHERE courier_id = {courier_id}"
                myFunctions.execute_query(del_cour)

                myFunctions.pretty_table(
                    myFunctions.execute_query("Select * from courier"))
                print("Courier deleted")
                break

# ELSE IF user input is 3:
# IF user input is 0:
# RETURN to main menu
    elif main_nav == 3:
        while True:
            myFunctions.menu_4()
            order_nav = int(input("please enter an option: "))
            if order_nav == 0:
                break
        # ELSE IF user input is 1:
        # PRINT orders table
            elif order_nav == 1:
                myFunctions.pretty_table(
                    myFunctions.execute_query("SELECT * from orders"))
        # ELSE IF user input is 2:
            elif order_nav == 2:
                # Get customer details
                while True:
                    new_cust_fname = input("Enter customer first name: ")
                    new_cust_lname = input("Enter customer last name: ")
                    new_cust_ph = input("Enter customer phone: ")
                    new_cust_add = input("Enter customer address: ")
                    # Print list of products
                    myFunctions.pretty_table(
                        myFunctions.execute_query("SELECT * from product"))
                    # Get user to select products for order
                    prod_order = input(
                        "Select desired product(s) by index, separated by space: ")
                    print("\n")
                    prod_list = prod_order.split()
                    print("Your Selection: ", prod_list)

                    # convert each item to int type
                    for i in range(len(prod_list)):
                        prod_list[i] = int(prod_list[i])
                    # Print list of couriers
                    myFunctions.pretty_table(
                        myFunctions.execute_query("SELECT * from courier"))
                    # Get user's desired courier
                    mycourier = int(input("Enter desired courier ID: "))
                    # courier_name = mycourier[courID]

                    # Define order status
                    o_status = "Preparing"
                    myFunctions.execute_query(
                        f"INSERT INTO orders (firstName, lastName, phone, custAddress, courier, delStatus, items) VALUES ('{new_cust_fname}', '{new_cust_lname}', '{new_cust_ph}', '{new_cust_add}', '{mycourier}', '{o_status}', '{prod_list}')")

                    print("New order added!")
                    myFunctions.pretty_table(
                        myFunctions.execute_query("SELECT * from orders"))
                    break

            elif order_nav == 3:
                # UPDATE existing order status
                myFunctions.pretty_table(
                    myFunctions.execute_query("SELECT * FROM orders"))
                updateOrder = int(
                    input("Enter the ORDER INDEX you want to update: "))
                print("\n")
                myFunctions.pretty_table(
                    myFunctions.execute_query("SELECT * FROM order_status"))
                new_order_status = int(input("Enter new order status ID: "))
                order_status = myFunctions.execute_query(
                    f"select * from order_status where statusID = {new_order_status}")
                # print(order_status)
                myFunctions.execute_query(
                    f"UPDATE orders SET delStatus = '{order_status[0] ['delStatus']}' WHERE orderID = {updateOrder}")

                # ELSE IF user input is 4:
                # STRETCH - UPDATE existing order
            elif order_nav == 4:
                myFunctions.pretty_table(
                    myFunctions.execute_query("SELECT * from orders"))
                # Get user input for order ID to be updated
                orderID = input(
                    "Enter order ID to be updated: ")
                orderUpdate = input(
                    "Select an update option: \n1. Customer First Name\n2. Customer Last Name\n3. Customer Phone Number\n4. Customer Address\n5. All\n ")
                while True:
                    if orderUpdate == "1":
                        custFName = input(
                            "Enter updated customer first name: ")
                        sqlUpdate = f"UPDATE orders SET firstName = '{custFName}' WHERE orderID = {orderID}"
                    elif orderUpdate == "2":
                        custLName = input("Enter updated customer last name: ")
                        sqlUpdate = f"UPDATE orders SET lastName = '{custLName}' WHERE orderID = {orderID}"
                    elif orderUpdate == "3":
                        custPhone = input(
                            "Enter updated customer phone number: ")
                        sqlUpdate = f"UPDATE orders SET phone = '{custPhone}' WHERE orderID = {orderID}"

                    elif orderUpdate == "4":
                        custAdd = input("Enter updated customer address: ")
                        sqlUpdate = f"UPDATE orders SET custAddress = '{custAdd}' WHERE orderID = {orderID}"

                    elif orderUpdate == "5":
                        custFName = input(
                            "Enter updated customer first name: ")
                        custLName = input("Enter updated customer last name: ")
                        custPhone = input(
                            "Enter updated customer phone number: ")
                        custAdd = input("Enter updated customer address: ")
                        sqlUpdate = f"UPDATE orders SET firstName = '{custFName}', lastName = '{custLName}', phone = '{custPhone}', custAddress = '{custAdd}' WHERE orderID = {orderID}"
                    else:
                        print("Nothing Updated!")

                    myFunctions.execute_query(sqlUpdate)
                    myFunctions.pretty_table(
                        myFunctions.execute_query("SELECT * from orders"))
                    break

            # STRETCH GOAL - DELETE order
            elif order_nav == 5:
                myFunctions.pretty_table(
                    myFunctions.execute_query("Select * from orders"))
                orderID = input(
                    "Enter order ID to be updated: ")
                delOrder = f"DELETE from orders WHERE orderID = {orderID}"
                myFunctions.execute_query(delOrder)

                myFunctions.pretty_table(
                    myFunctions.execute_query("SELECT * from orders"))
                print("Order deleted successfully!")
