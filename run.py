from data import delete_data, update_data, insert_data, show_products, print_success, print_error
from colorama import Fore


def menu():
    print(Fore.LIGHTCYAN_EX + "Welcome to my program, please select option" + Fore.RESET)
    try:
        choice = int(input(Fore.LIGHTCYAN_EX + "1 ==> Add product\n2 ==> Update product"
                                               "\n3 ==> Delete product\n4 ==> Show products\n"
                                               "0 ==> Exit\n...." + Fore.RESET))
    except ValueError:
        print_error("Wrong input, please try again")
    except TypeError:
        print_error("Wrong input, please try again")
    else:
        if 0 <= choice <= 4:
            return choice
        else:
            print_error("Wrong input, please try again")


def run():
    while True:
        choice = menu()
        if choice == 1:
            insert_data()
        elif choice == 2:
            update_data()
        elif choice == 3:
            delete_data()
        elif choice == 4:
            show_products()
        elif choice == 0:
            print_success("Thank you for using my program")
            break


if __name__ == '__main__':
    run()
