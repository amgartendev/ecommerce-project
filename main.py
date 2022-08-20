from typing import List, Dict
from time import sleep
from models.product import Product
from utils.helper import format_float_str

products: List[Product] = []
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
    print('======== Register Product ========')
    name: str = input('Insert the product: ')
    price: float = float(input('Insert the price: '))

    product: Product = Product(name, price)

    products.append(product)

    print(f'{product.name} registered!')
    sleep(1)
    menu()


def list_products() -> None:
    if len(products) > 0:
        print('======== Products List ========')
        for product in products:
            print(product)
            print('--------')
            sleep(.5)
    else:
        print("We don't have any registered products yet")
    sleep(2)
    menu()


def cart_product() -> None:
    pass


def view_cart() -> None:
    pass


def buy() -> None:
    if len(cart) > 0:
        total_price: float = 0

        print('======== Products in your Cart ========')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                total_price += data[0].price * data[1]
                print('--------')
                sleep(.5)
        print(f'Total: {format_float_str(total_price)}')
        print('Thanks! Come back soon :)')
        cart.clear()
        sleep(4)
    else:
        print("You don't have any product in your cart. Let's buy some!!")
    sleep(2)
    menu()


def get_product_by_code(code: int) -> Product:
    pass


if __name__ == '__main__':
    main()
