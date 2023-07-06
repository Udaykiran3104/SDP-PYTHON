import typer
from models import create_tables
from services.cart import CartService

app = typer.Typer()

cart_service= CartService()

@app.command()
def add_item(username:str , item_name:str , quantity:int ):
    cart_service.add_item(username,item_name,quantity)

@app.command()
def remove_item(user_name:str):
    cart_service.remove(user_name)