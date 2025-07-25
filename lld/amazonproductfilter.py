from abc import ABC,abstractmethod
from typing import List

class Product:
    def __init__(self,id: str,brand: str,category :str,rating :int,cost :int):
        self.id = id
        self.brand = brand
        self.category = category
        self.rating = rating
        self.cost = cost

class FilterCriteria(ABC):
    @abstractmethod
    def filter(self,products: List[Product]) -> List[Product]:
        pass

class BrandFilter(FilterCriteria):
    def __init__(self,brand :str):
        self.brand = brand
    
    def filter(self,products: List[Product]) -> List[Product]:
        return [product for product in products if product.brand == self.brand]

class CategoryFilter(FilterCriteria):
    def __init__(self,category :str):
        self.category = category
    
    def filter(self,products: List[Product]) -> List[Product]:
        return [product for product in products if product.category == self.category]

class RatingFilter(FilterCriteria):
    def __init__(self,min_rating :int):
        self.min_rating = min_rating
    
    def filter(self,products: List[Product]) -> List[Product]:
        return [product for product in products if product.rating >= self.min_rating]

class CostFilter(FilterCriteria):
    def __init__(self,min_price :int, max_price :int):
        self.min_price = min_price
        self.max_price = max_price
    
    def filter(self,products: List[Product]) -> List[Product]:
        return [product for product in products if self.min_price <= product.cost <= self.max_price]


class ProductFilter:
    def __init__(self):
        self.criteria_list :List[FilterCriteria] = []
    
    def add_criteria(self,criteria :FilterCriteria):
        self.criteria_list.append(criteria)

    def apply_filters(self,products :List[Product]) -> List[Product]:
        for criteria in self.criteria_list:
            products = criteria.filter(products)
        return products
        
