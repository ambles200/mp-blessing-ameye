# Goals
# As a user I want to:
# create a product or courier and add it to a list
# view all products or couriers
# persist my data
# STRETCH I want to be able to update or delete a product or courier


# Spec
# A product should just be a string containing its name, i.e: "Coke Zero"
# A list of products should be a list of strings , i.e: ["Coke Zero"]
# A courier should just be a string containing its name, i.e: "John"
# A list of couriers should be a list of strings , i.e: ["John"]
# Data should be persisted to a .txt file on a new line for each courier or product , ie:
# John
# Claire


# LOAD products list from products.txt
# LOAD couriers list from couriers.txt

import myFunctions


my_products = myFunctions.read_file_list("products.txt")
my_courier = myFunctions.read_file_list("couriers.txt")

# --------------------------Orders List----------------------------------
orders_list = [{
    "customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "courier": "1",
    "status": "Preparing"
},
    {
    "customer_name": "Shaw",
    "customer_address": "Unit 17, 15 Market Street, MANCHESTER, M1 2ER",
    "customer_phone": "0747667345",
    "courier": "2",
    "status": "Out for delivery"
}
]

# -------------------Order Status List---------------------------
order_status = ["Preparing", "Out for delivery", "Delivered"]


# PRINT main menu options
while True:
    myFunctions.menu_1()
# GET user input for main menu option
    main_nav = int(input("Make a selection: "))
    if main_nav == 0:
        myFunctions.write_list_to_file(my_products, "products.txt")
        myFunctions.write_list_to_file(my_courier, "couriers.txt")
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
            elif sub_nav == 1:
                while True:
                    print(my_products)
                    break
# PRINT products list
# ELSE IF user input is 2:
# # CREATE new product
# GET user input for product name
# APPEND product name to products list
            elif sub_nav == 2:
                while True:
                    new_prod = input("Enter new product: ")
                    my_products.append(new_prod)
                    new_item = open("products.txt", "w")
                    for product in my_products:
                        new_item.write(product + "\n")
                    print(my_products)
                    new_item.close()
                    break


# ELSE IF user input is 3:
# # STRETCH GOAL - UPDATE existing product
# PRINT product names with its index value
# GET user input for product index value
# GET user input for new product name
# UPDATE product name at index in products list

            elif sub_nav == 3:
                index = 0
                for product in my_products:
                    print(f"{index} {product}")
                    index += 1
                while True:
                    prod_id = int(input(
                        "Enter Product ID: "))
                    prod_name = str(input("Enter New Product Name: "))

                    if my_products[prod_id]:
                        my_products[prod_id] = prod_name
                        myFunctions.write_list_to_file(
                            my_products, "products.txt")
                    print(my_products)
                    break
# ELSE IF user input is 4:
# # STRETCH GOAL - DELETE product
# PRINT my_products list
# GET user input for product index value
# DELETE product at index in my_products list
            else:
                sub_nav == 4
                for index, product in enumerate(my_products):
                    print(f"{index} {product}")
                prod_id = int(input("Enter product ID to be deleted: "))
                my_products.pop(prod_id)
                myFunctions.write_list_to_file(
                    my_products, "products.txt")
                print("Product deleted")
                print(my_products)
                break


# # couriers menu
# ELSE IF user input is 2:
    elif main_nav == 2:
        while True:
            # PRINT courier menu options
            myFunctions.menu_3()
# GET user input for courier menu option
            # IF user inputs 0:
            # RETURN to main menu
            cour_nav = int(input("Please select an option: "))
            if cour_nav == 0:
                break
                # ELIF user inputs 1:
            elif cour_nav == 1:
                while True:
                    print(my_courier)
                    break
                # PRINT couriers list
                # ELSE IF user input is 2:
                # # CREATE new courier
            elif cour_nav == 2:
                while True:
                    cour_nav = input("Enter Courier Name: ")
                    my_courier.append(cour_nav)
                    new_item = open("couriers.txt", "w")
                    for courier in my_courier:
                        new_item.write(courier + "\n")
                    print(my_courier)
                    print("New Courier Added")
                    new_item.close()
                    break

                # GET user input for courier name
                # APPEND courier name to couriers list
                # ELSE IF user input is 3:
                # STRETCH GOAL - UPDATE existing courier
                # PRINT courier names with its index value
                # GET user input for courier index value
                # GET user input for new courier name
                # UPDATE courier name at index in couriers list
            elif cour_nav == 3:
                for index, courier in enumerate(my_courier):
                    print(f"{index} {courier}")
                courier_id = int(input(
                    "Enter Courier ID "))
                courier_name = str(input("Enter New Courier Name: "))

                if my_courier[courier_id]:
                    my_courier[courier_id] = courier_name
                    myFunctions.write_list_to_file(
                        my_courier, "couriers.txt")
                    print(my_courier)
                    print("Courier updated")
                    break

                # ELSE IF user input is 4:
                # # STRETCH GOAL - DELETE courier
                # PRINT courier list
                # GET user input for courier index value
                # DELETE courier at index in courier list

            else:
                cour_nav == 4
                for index, courier in enumerate(my_courier):
                    print(f"{index} {courier}")
                courier_id = int(input("Enter courier ID to be deleted: "))
                my_courier.pop(courier_id)
                myFunctions.write_list_to_file(
                    my_courier, "couriers.txt")
                print("Courier deleted")
                print(my_courier)
                break


# orders menu - WEEK 3 UPDATE
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
        # PRINT orders dictionary
            elif order_nav == 1:
                print(orders_list)
        # ELSE IF user input is 2:
            elif order_nav == 2:
                for index, courier in enumerate(my_courier):
                    print(f"{index} {courier}")
                while True:
                    order = {}
                    order["customer_name"] = input("Enter customer name: ")
                    order["customer_address"] = input(
                        "Enter customer address: ")
                    order["customer_phone"] = input("Enter customer phone: ")
                    order["courier"] = input("Enter courier: ")
                    order["status"] = "Preparing"
                    orders_list.append(order)
                    print(orders_list)
                    break
# # GET user input for customer name
# GET user input for customer address
# GET user input for customer phone number
# PRINT couriers list with index value for each courier

# GET user input for courier index to select courier
# SET order status to be 'PREPARING'
# APPEND order to orders list

# ELSE IF user input is 3:
# UPDATE existing order status
# PRINT orders list with its index values
# GET user input for order index value
# PRINT order status list with index values
# GET user input for order status index value
# UPDATE status for order

            elif order_nav == 3:
                for index, order_status in enumerate(order_status):
                    print(f"{index} {order_status}")
                # for key, value in orders_list[0].items():
                #     print("{}, {}".format(key, value))
                update_order = input("Enter Order ID To Be Updated: ")

                if update_order == 0:
                    print(order_status[0])
                elif update_order == 1:
                    print(order_status[1])
                else:
                    update_order == 2
                    print(order_status[2])

                    # print("Error! please select a number between 0 - 2")

# ELSE IF user input is 4:
# # STRETCH - UPDATE existing order
# PRINT orders list with its index values

            elif order_nav == 4:
                for index, orders_list in enumerate(orders_list):
                    print(index, orders_list["customer_name"], orders_list["customer_address"],
                          orders_list["customer_phone"], orders_list["courier"], orders_list["status"])
                # for index, order in enumerate(orders_list):
                #     for key, value in order.items():
                #         print("{}, {}, {}".format(index, key, value))
                order_index = int(input("Enter order ID to be updated: "))
                while True:
                    order = {}
                    order["customer_name"] = input(
                        "Enter new customer name: ")
                    order["customer_address"] = input(
                        "Enter new customer address: ")
                    order["customer_phone"] = input(
                        "Enter new customer phone: ")
                    order["courier"] = input("Enter new courier: ")
                    order["status"] = input("Enter new status: ")
                    if order["customer_name"] == "":
                        print("Nothing updated")
                    else:
                        orders_list[order_index] = order
                    print(orders_list)
                    break
        # GET user input for order index value
        # FOR EACH key-value pair in selected order:
        # GET user input for updated property
        # IF user input is blank:
        # do not update this property
        # ELSE:
        # update the property value with user input
        # ELSE IF user input is 5:
            else:
                order_nav == 5
                for index, orders_list in enumerate(orders_list):
                    print(index, orders_list["customer_name"], orders_list["customer_address"],
                          orders_list["customer_phone"], orders_list["courier"], orders_list["status"])
        # # STRETCH GOAL - DELETE courier
        # PRINT orders list
        # GET user input for order index value
                order_index = int(input("Enter order ID to be deleted: "))
                for i in range(len(orders_list)):
                    if orders_list[i] == order_index:
                        del orders_list[i]
                        break
                print("Order deleted")
                print(orders_list)
