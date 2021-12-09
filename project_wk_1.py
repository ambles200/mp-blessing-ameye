# # add some product names
# CREATE products list
products = ["Coke Zero",
            "Tea",
            "Coffee",
            "Fanta",
            "Pepsi Max",
            "Sprite",
            "7Up",
            "Hot White Coffee",
            "Pizzas",
            "Champagne Ham & Cheese",
            "Beef & Onion",
            "Pepperoni"]
main_menu = "\nMain Menu\n0. Exit\n1. Product Menu"
sub_menu = "\nProduct Menu\n0. Exit\n1. See product list\n2. Add new product\n3. Update product list\n4. Delete product"


# PRINT main menu options
while True:
    print(main_menu)
# GET user input for main menu option
    input1 = int(input("Make a selection: "))
# IF user input is 0:
#     EXIT app
    if input1 == 0:
        break
# # products menu
# ELSE IF user input is 1:
    elif input1 == 1:
        while True:
            #     PRINT product menu options
            print(sub_menu)
#     GET user input for product menu option
            input2 = int(input("Please choose an option: "))
#     IF user input is 0:
#         RETURN to main menu
            if input2 == 0:
                break
#     ELSE IF user input is 1:
            elif input2 == 1:
                while True:
                    print(products)
                    break

#     ELSE IF user input is 2:
#         # CREATE new product
            # elif input2
#         GET user input for product name
#         APPEND product name to products list
            elif input2 == 2:
                while True:
                    input2 = input("Enter new product: ")
                    products.append(input2)
                    print(products)
                    break

#
#     ELSE IF user input is 3:
#         # STRETCH GOAL - UPDATE existing product
#         PRINT product names with its index value
#         GET user input for product index value
#         GET user input for new product name
#         UPDATE product name at index in products list

            elif input2 == 3:
                index = 0
                for product in products:
                    print(f"{product} {index}")
                    index += 1
                while True:
                    input3 = int(input(
                        "Enter the product index you want to update: "))
                    input4 = str(input("Enter new product name: "))
                    products[input3] = input4
                    print(products)
                    break


#     ELSE IF user input is 4:
#         # STRETCH GOAL - DELETE product
#         PRINT products list
#         GET user input for product index value
#         DELETE product at index in products list
            else:
                input2 == 4
                index = 0
                for product in products:
                    print(f"{product} {index}")
                    index += 1
                while True:
                    input5 = int(input(
                        "Enter the product index you want to update: "))
                    del products[input5]
                    print("Product deleted")
                    print(products)
                    break
