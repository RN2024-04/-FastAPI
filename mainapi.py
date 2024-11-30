from fastapi import FastAPI
app=FastAPI()
@app.get('/')
async def get_gla()-> dict:
    return {'message':"Главная страница"}
@app.get("/users/{user_id}")
async def read_user(user_id: int)-> dict:
    return {'message':f"Вы вошли как пользователь № {user_id}"}
@app.get('/user/admin')
async def read_admin()-> dict:
    return {'message':"Вы вошли как администратор"}
@app.get("/user")
async def get_pack(username: str,age:int) -> dict:
    return {'message':f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
#uvicorn main:app --reload