from models import User

class UserService:
    def signup(self,user_name:str , password:str):
        user = User.create(user_name=user_name,password=password)
        print(f"{user.user_name} signed up!")

    def login(self,user_name:str , password:str):
        user = User.get(user_name=user_name,password=password)
        print(f"{user.user_name} logged in!")

    def remove(self,user_name:str):
      user = User.get(user_name = user_name) 
      user.delete_instance()
      print(f"{user.user_name} removed from users")
       
