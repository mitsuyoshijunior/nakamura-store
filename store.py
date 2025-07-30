from time import sleep

from models.product import Product
from utils.helper import format_currency

products: list[Product] = []
shopping_cart: dict[Product, int] = {}

def main() -> None:
    menu()

def menu() -> None:
    print("=====================================")
    print("      Welcome to Nakamura Store      ")
    print("=====================================\n")

    print("Please select an option:")
    print("1. Register product")
    print("2. Show products")
    print("3. Buy products")
    print("4. View cart")
    print("5. Place order")
    print("6. Exit\n")

    choice: int = int(input("Enter your choice (1-6): "))

    if choice == 1:
        register_product()
    elif choice == 2:
        show_products()
    elif choice == 3:
        buy_product()
    elif choice == 4:
        view_cart()
    elif choice == 5:
        order()
    elif choice == 6:
        print('Come back soon!')
        sleep(2)
        exit(0)
    else:
        print('Invalid Option. Try again.')
        sleep(2)
        menu()

def register_product() -> None:
    print('Product registration')
    print('====================')

    name: str = input('Type the product name: ')
    price: float = float(input('Type the product price: '))

    product: Product = Product(name, price)

    products.append(product)

    print(f'The product was registered.')
    sleep(2)
    menu()

def show_products() -> None:
    if len(products) > 0: 
        print('Available Products List') 
        print('-----------------------')
        for i in products:
            print(i)
            print('----------------')
        input('Type anything to go back to the menu: ')
        menu()
    else:
        print('No available products yet.')
        sleep(2)
        menu()

def buy_product() -> None:
    if len(products) > 0:
        print('--------------------------------')
        print('====== Available Products ======')

        for i in products:
            print(i)
            print('------------------------------')
            sleep(1)

        code: int = int(input('Enter the product code you want:'))

        product: Product = get_product_by_code(code)

        if product:
            shopping_cart[product] = shopping_cart.get(product, 0) + 1
            print(f'There are now {shopping_cart.get(product, 0)} products in the cart.')
            sleep(2)
            menu()
        else:
            'Invalid code. Try again.'
            sleep(2)
            menu()
    else:
        print('No available products yet.')
        sleep(2)
        menu()
            
def view_cart() -> None:
    if len(shopping_cart) > 0:
        print('Products in the shopping cart: ')

        for key, value in shopping_cart.items():
            print(key)
            print(f'Quantity: {value}')
            print('---------------------')
            sleep(1)
    else:
        print('There are not products in the shopping cart.')
        sleep(2)
    menu()

def order() -> None:
    if len(shopping_cart) > 0:
        total_amount: float = 0

        for product, quantity in shopping_cart.items():
            print(f'Product name: {product.name}')
            print(f'Quantity: {quantity}')
            print('-------------------------')

            price = product.price * quantity
            
            total_amount += price

        print(f'Total amount: {format_currency(total_amount)}')
        print('\n')
        print('Come back soon!')
        sleep(3)
        exit(0)
    else:
        print('There are not products in the shopping cart.')
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