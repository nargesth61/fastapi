from typing import List

from fastapi import BackgroundTasks, FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from db.models import Userdb
from dotenv import dotenv_values
import jwt



config = dotenv_values(".env")

conf = ConnectionConfig(
    MAIL_USERNAME =config["ENAIL"],
    MAIL_PASSWORD = config["PASS"],
    MAIL_FROM = config["ENAIL"],
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = False,
    VALIDATE_CERTS = True
)

async def send_email(email:List[str] , instance:str):
    create_token={
        "id":instance.id,
        "username":instance.username
    }
    token = jwt.encode(create_token,config["SECRET"],algorithm=("HS256"))
     

    template = f"""
    <!DOCTYPE html>
     <html>
      <head>
      </head>
        <body>
           <div style="display : flex ; aling-item:center ; justify-content:center
            felx-direction : column ">
            <h3>Account verification</h3>
            <br>
            <p>thanks for commit</p>
            <a style="margin-top:1rem; padding:1rem; font-size : 1rem; href="http://localhost:8000/verifiction/?token={token}">
            your email confirmation</a>
        </body>
    </html>
    """
 
    print(email)
    print(instance.username)
    message = MessageSchema(
            subject="easy vrify email",
            recipients=email,
            body=template,
            subtype='html'
                          )
    fm = FastMail(conf)
    await fm.send_message(message)
    print('yes')