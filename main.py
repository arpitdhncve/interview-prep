
from datetime import date
from random import randint
from unicodedata import category
from product import  ProductEnum
from inventory import Inventory
from InventoryManagement import InventoryManagement
from offers import OfferManagement
from productView import WithoutDiscount, DiscountOn


def main():
    print("In the main")
    
    inventory1 = Inventory()

   
    InventoryManagement.add_product(inventory1, {"name": "tv", "price": 36000, "stock" : 10, "warrenty": 2}, ProductEnum.ELECTRONICS)
    InventoryManagement.add_product(inventory1, {"name": "fridge", "price": 20000, "stock" : 10, "warrenty": 5}, ProductEnum.ELECTRONICS)
    InventoryManagement.add_product(inventory1, {"name": "jeans", "price": 3600, "stock" : 10, "fabric": "silk", "size" : "38"}, ProductEnum.CLOTHING)
    InventoryManagement.add_product(inventory1, {"name": "T shirt", "price": 1800, "stock" : 10, "fabric": "silk", "size" : "34"}, ProductEnum.CLOTHING)
    InventoryManagement.add_product(inventory1, {"name": "kurkure", "price": 36, "stock" : 20, "expiry_date" : date(2024, 11, 23)}, ProductEnum.FOOD)
    InventoryManagement.add_product(inventory1, {"name": "Chips", "price": 36, "stock" : 20, "expiry_date" : date(2024, 10, 23)}, ProductEnum.FOOD)


    
    print(inventory1.get_all_products())
    print()
    print("Category wise product")
    print()
    print(inventory1.get_product_by_category(ProductEnum.CLOTHING))

    print()
    print()

    OfferManagement.update_category_offer(inventory1, ProductEnum.CLOTHING, 15)
    OfferManagement.update_category_offer(inventory1, ProductEnum.ELECTRONICS, 20)
    OfferManagement.update_category_offer(inventory1, ProductEnum.FOOD, 18)


    for product in inventory1.get_product_by_category(ProductEnum.CLOTHING):
        quantity = randint(1,4)
        discount_percentage = randint(10,20)
        OfferManagement.update_discount_details(inventory1, product["id"], quantity, discount_percentage)


    print()
    print()


    inventory1.update_discount_status(DiscountOn())

    print("Discount On")
    print()

    print(inventory1.get_all_products())



    
   


if __name__ == "__main__":
    main()