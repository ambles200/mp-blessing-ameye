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
                    print(f"{product} {index}")
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
                    print(f"{product} {index}")
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
                    my_courier.append(input3)
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
                    print(f"{courier} {index}")
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
                    print(f"{courier} {index}")
                courier_id = int(input("Enter courier ID to be deleted: "))
                my_courier.pop(courier_id)
                myFunctions.write_list_to_file(
                    my_courier, "couriers.txt")
                print("Courier deleted")
                print(my_courier)
                break
