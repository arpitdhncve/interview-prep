from abc import ABC, abstractmethod

class ProductViewStrategy(ABC):

    @abstractmethod
    def get_list(self,inventory):
        pass


    @abstractmethod
    def get_product_details(self, product):
        pass




class WithoutDiscount(ProductViewStrategy):

    def get_list(self, inventory, category:None):
        output = []
        for product in inventory.products:
            if product.category == category or category is None:
                if product.stock > 0:
                    product_details = self.get_product_details(product)
                    output.append(product_details)
        return output

    
    def get_product_details(self, product):
        product_details = product.get_product_details()
        return product_details


class DiscountOn(ProductViewStrategy):

    def get_list(self, inventory, category:None):
        output = []
        for product in inventory.products:
            if product.category == category or category is None:
               product_details = self.get_product_details(inventory, product)
               if product_details is not None:
                   output.append(product_details)
        return output

    
    def get_product_details(self, inventory, product):
        if product.stock > 0:
            product_details = product.get_product_details()
            if product.id in inventory.discounts:
                discount_of_product = inventory.discounts[product.id]
                product_details["quantity"] = discount_of_product.quantity
                product_details["discounted_price"] = product.get_discounted_price(discount_of_product.discount, discount_of_product.quantity)
            else:
                product_details["discounted_price"] = "No Discounted Price"
            
            return product_details

       

        