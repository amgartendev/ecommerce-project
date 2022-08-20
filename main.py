from typing import List, Dict
from time import sleep
from models.product import Product
from utils.helper import format_float_str

product: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    pass


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
