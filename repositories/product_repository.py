from models.product import Product
from exceptions import *

class ProductRepository:
    products: list[Product]
    def __init__(self) -> None:
        self.products = []
    
    def add(self, new_product: Product) -> None:
        self._validate_duplicate_id(new_product.id)
        self.products.append(new_product)
    
    def delete(self, product_id: int) -> None:
        product: Product = self.find_by_id(product_id)
        self.products.remove(product)
    
    def get_all(self) -> list[Product]:
        return self.products
    
    def count(self) -> int:
        return len(self.products)

    def find_by_id(self, product_id: int) -> Product:
        for product in self.products:
            if product_id == product.id:
                return product
        raise ProductNotFoundError("Product Not Found")

    def _exists(self, product_id: int) -> bool:
        for product in self.products:
            if product_id == product.id:
                return True
        return False

    def _validate_duplicate_id(self, new_product_id: int) -> None:
        if self._exists(new_product_id):
            raise DuplicateProductError("You are trying to insert duplicate product")
    
