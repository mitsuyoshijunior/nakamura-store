from utils.helper import format_currency

class Product:

    counter: int = 1

    def __init__(self: object, name: str, price: float) -> None:
        self.__code: str = Product.counter
        self.__name: str = name
        self.__price: float = price
        Product.counter += 1

    @property
    def code(self: object) -> int:
        return self.__code
    
    @property
    def name(self: object) -> str:
        return self.__name 
    
    @property
    def price(self: object) -> float:
        return self.__price
    
    def __str__(self) -> str:
        return f'Code: {self.code} \nName: {self.name} \nPrice: {format_currency(self.price)} \n'
    
    def __eq__(self: object, other: object) -> bool:
        if isinstance(other, Product):
            return self.code == other.code
        return False
    
    def __hash__(self: object) -> int:
        return hash(self.code)