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
    if len(products) > 0:
        print('======== Add to your Cart ========')
        print('Insert the code of the product that you want to add to your cart: ')
        print('--------------------------------------------------------------------')
        print('======== Products List ========')
        for product in products:
            print(product)
            print('--------')
            sleep(.5)

        code: int = int(input(''))

        product: Product = get_product_by_code(code)

        if product:
            if len(cart) > 0:
                already_exists: bool = False
                for item in cart:
                    quantity: int = item.get(product)
                    if quantity:
                        item[product] = quantity + 1
                        print(f'You have {quantity + 1} {product.name} in your cart now!')
                        already_exists = True
                        sleep(2)
                        menu()

                if not already_exists:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'{product.name} added to your cart!')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'{product.name} added to your cart!')
                sleep(2)
                menu()
        else:
            print(f'This product does not exist!')
            sleep(2)
            menu()
    else:
        print("We are not selling any item yet... Come back later")
    sleep(2)
    menu()


def view_cart() -> None:
    if len(cart) > 0:
        print('======== Your Cart ========')

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('--------')
                sleep(.5)
    else:
        print("You don't have any product in your cart. Let's buy some!!")
        sleep(2)
        menu()


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
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p


if __name__ == '__main__':
    main()
