from inventory import Inventory
from enum import Enum
from abc import ABC, abstractmethod
from datetime import date
import uuid
import json


class ProductEnum(Enum):
    ELECTRONICS = 1
    FOOD = 2
    CLOTHING = 3


class Product(ABC):

    def __init__(self, name, category : ProductEnum, price, stock, inventory: Inventory):
        self.id = uuid.uuid4()
        self.name = name
        self.category = category
        self.price = price
        self.inventory = inventory
        self.stock = stock


    def get_discounted_price(self, discount_percentage, quantity):
        new_price = ((100-discount_percentage)*self.price) / 100
        return quantity*new_price

    @abstractmethod
    def is_eligible_for_discount(self):
        pass

    @abstractmethod
    def get_product_details(self):
        pass
 
    
    
class Electronics(Product):

    def __init__(self, product_details, inventory):
        super().__init__(product_details["name"], ProductEnum.ELECTRONICS, product_details["price"],  product_details["stock"], inventory)
        self.warrenty = product_details["warrenty"]

    def is_eligible_for_discount(self):
        return True

    def get_product_details(self):
        return {"id": self.id, "name":self.name , "price": self.price, "category": self.category.value, "warrenty": self.warrenty, "quantity": 1}


class Clothing(Product):

    def __init__(self, product_details, inventory):
        super().__init__(product_details["name"], ProductEnum.CLOTHING, product_details["price"],  product_details["stock"], inventory)
        self.fabric = product_details["fabric"]
        self.size = product_details["size"] 

    def is_eligible_for_discount(self):
        return True

    def get_product_details(self):
        return {"id" : self.id ,"name":self.name , "price": self.price, "category": self.category.value, "fabric": self.fabric, "size" : self.size, "quantity": 1}
        


class Food(Product):

    def __init__(self, product_details, inventory):
        super().__init__(product_details["name"], ProductEnum.FOOD, product_details["price"], product_details["stock"], inventory,)
        self.expiry_date = product_details["expiry_date"]

    def get_product_details(self):
        return {"id" : self.id, "name":self.name , "price": self.price, "category": self.category.value, "expiry_date": str(self.expiry_date), "quantity": 1}
        

    def is_eligible_for_discount(self):
        if (self.expiry_date - date.today()).days > 30:
            return False
        else:
            return True


