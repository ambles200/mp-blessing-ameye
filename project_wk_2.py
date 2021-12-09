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

# PRINT main menu options
# GET user input for main menu option

main_menu = "\nMain Menu\n0. Exit\n1. Product Menu"
sub_menu = "\nProduct Menu\n0. Exit\n1. See product list\n2. Add new product\n3. Update product list\n4. Delete product"
