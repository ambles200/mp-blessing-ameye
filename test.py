import sys

main_menu = ["Espresso, Ice Blended, Tea, Pastries"]


def menu():
    print("***************Welcome To Street Wise Pop Up Cafe*******************")

    choice = input("""
                   Please choose your menu:
                   Espresso
                   Ice_Blended
                   Tea
                   Pasteries
                   No Option
                    """)

    while choice == "Espresso":
        espresso = ["Macchiato, Latte, Mocha, Cortado, Americano"]
        print(espresso)

    # elif choice == "E":
    #     sys.exit

    # else:
    #     print("You must select an option")


# while True:
    menu()
