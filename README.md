# Nakamura Store

Simple terminal application for managing a store, allowing product registration, listing, buying, viewing the cart, and placing orders.

## Features

- Register new products with name and price.
- Show available products list.
- Buy products by adding them to the shopping cart.
- View products and quantities in the cart.
- Place an order showing the total amount.
- Exit the system with a goodbye message.

## How to use

1. Run the program:
   ```bash
   python store.py
   ```

2. Choose an option from the menu:
    
    1: Register product
    
    2: Show products
    
    3: Buy products
    
    4: View cart
    
    5: Place order

    6: Exit

3. Follow the on-screen instructions for each option.

## Dependencies

- Python 3.10 or higher
- Project files:
  - `store.py` (main file)
  - `models/product.py` (Product class)
  - `utils/helper.py` (format_currency function)

## Notes

- The shopping cart is stored in memory while the program runs.
- The program uses pauses (`sleep`) to improve terminal experience.

