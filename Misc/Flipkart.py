class Flipkart:
    products={"NikeShoes":10,"AdidasShoes":10,"NewBalanceShoes":10,"PumaShoes":10}
    def __init__(self,name):
        self.name=name
        self.cart={}
    def add_item(self,item):
        if item in Flipkart.products and Flipkart.products[item]>0:
            if item not in self.cart:
                self.cart[item]=1
                Flipkart.products[item]-=1
            else:
                self.cart[item]+=1
        else:
            print("Item does not exist")
    def remove_item(self,item):
        if item in self.cart:
            if self.cart[item]>1:
                self.cart[item]-=1
                Flipkart.products[item]+=1
            else:
                self.cart.pop(item)
                print("Item not present in your cart")
        else:
            print("Item not found in your cart")

    def cart(self):
        for item in self.cart:
            print(f"{item} ------->{self.cart[item]}")

            

    

c=Flipkart("Robert")

