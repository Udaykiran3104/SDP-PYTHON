import typer
from models import create_tables , Inventory ,User , Cart
from commands import inventory ,user , cart

app=typer.Typer()

app.add_typer(inventory.app,name="inventory")
app.add_typer(user.app,name="user")
app.add_typer(cart.app,name="cart")
   
if __name__ == "__main__":

    create_tables()
    app()
 