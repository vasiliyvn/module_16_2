from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# python -m uvicorn module_16_1:app
@app.get('/')
async def page():
    return f'Главная страница'


@app.get('/user/admin')
async def admin():
    return f'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def userid(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=3)):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user/{username}/{age}')
async def user(username: Annotated[str, Path(min_length=5, max_length=20,
        description='Enter username', example='Vasya_User')],
        age: int = Path(ge=18, le=120, description='Enter age', example=36)):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
