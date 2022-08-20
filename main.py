from typing import List, Dict
from time import sleep
from models.product import Product
from utils.helper import format_float_str

product: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print("=====================================")
    print("===========     Welcome to   ========")
    print("===========  Amgarten's shop ========")
    print("=====================================")

    print('Select an option: ')
    print('1 - Register Product')
    print('2 - List Products')
    print('3 - Add to Cart')
    print('4 - View Cart')
    print('5 - Buy')
    print('6 - Exit')

    option: int = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        list_products()
    elif option == 3:
        cart_product()
    elif option == 4:
        view_cart()
    elif option == 5:
        buy()
    elif option == 6:
        print('See you!')
        sleep(2)
        exit(0)
    else:
        print('Error: Select a valid option!')
        menu()


def register_product() -> None:
    pass


def list_products() -> None:
    pass


def cart_product() -> None:
    pass


def view_cart() -> None:
    pass


def buy() -> None:
    pass


def get_product_by_code(code: int) -> Product:
    pass


if __name__ == '__main__':
    main()
