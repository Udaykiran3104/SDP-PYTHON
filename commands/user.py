import typer
from models import create_tables,User
from services.user import UserService

app = typer.Typer()

user= UserService()

@app.command()
def signup(user_name:str , password:str):
    user.signup(user_name,password)

@app.command()
def remove(user_name:str):
    user.remove(user_name)