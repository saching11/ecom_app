from models.product import Product
class ProductService:
    products: list[Product]
    def __init__(self) -> None:
        self.products = []
    
    def add_product(self, new_product: Product) -> None:
        self._validate_duplicate_id(new_product.id)
        self.products.append(new_product)
    
    def change_price(self, product_id: int, new_price: float) -> None:
        product = self._find_product_by_id(product_id)
        product.change_price(new_price)

    def _validate_duplicate_id(self, new_product_id: int) -> None:
        if self._find_product_by_id(new_product_id) is not None:
            raise Exception("You are trying to insert duplicate product")
    
    def _find_product_by_id(self, product_id: int) -> Product | None:
        for product in self.products:
            if product_id == product.id:
                return product
        raise Exception("Product Not Found")
    