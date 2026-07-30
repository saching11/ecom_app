from exceptions.invalid_price_error import InvalidPriceError
class Product:
    id: int
    name: str
    price: float
    stock: int
    category: str

    def __init__(self, id: int, name: str, price: float, stock: int, category: str) -> None:
        self._validate_id(id)
        self._validate_stock(stock)
        self.id = id
        self.rename(name)
        self.change_price(price)
        self.stock = stock
        self.category = category
    
    def rename(self, new_name: str) -> None:
        self._validate_name(new_name)
        self.name = new_name.strip()
    
    def change_price(self, new_price: int) -> None:
        self._validate_price(new_price)
        self.price = new_price
    
    def increase_stock(self, quantity: int) -> None:
        self._validate_stock(quantity)
        self.stock += quantity

    def decrease_stock(self, quantity: int) -> None:
        self._validate_stock(quantity)
        if quantity < self.stock:
            self.stock -= quantity
    
    def is_in_stock(self) -> bool:
        if self.stock > 0:
            return True
        return False

    def _validate_id(self, id) -> None:
        if id is None:
            raise ValueError("Please give an id")

    def _validate_name(self, name) -> None:
        if name is None or name.strip() == "":
            raise ValueError("Name cannot be empty")

    def _validate_price(self, price) -> None:
        if price is None or price < 0:
            raise InvalidPriceError("Price cannot be less than or equal to 0")

    def _validate_stock(self, quantity) -> None:
        if quantity is None or quantity <= 0:
            raise ValueError("Quantity cannot be less than or equal to 0")


