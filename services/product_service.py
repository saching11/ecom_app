from repositories.product_repository import ProductRepository

class ProductService:
    repository: ProductRepository
    def __init__(self) -> None:
        self.repository = ProductRepository()
    
    def add_product(self, new_product: Product) -> None:
        self.repository.add(new_product)
    
    def change_price(self, product_id: int, new_price: float) -> None:
        product = self.repository.find_by_id(product_id)
        product.change_price(new_price)
    