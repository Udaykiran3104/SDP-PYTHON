from models import Cart , Inventory , User

class CartService:
        def add_item(self,username:str , item_name:str , quantity:int ):
               user = User.get(user_name = username)
               item = Inventory.get(name=item_name)
               cart_item = Cart.create(user=user , item=item , quantity=quantity) 
               print(f"{cart_item.item.name} added to the cart")


        def remove_item(self,username:str):
              user = User.get(user_name = username) 
              user.delete_instance()
              print(f"{user.user_name} removed from cart")