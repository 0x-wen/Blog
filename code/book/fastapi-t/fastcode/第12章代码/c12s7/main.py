from fastapi import FastAPI
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

register_tortoise(
    app,
    db_url="mysql://root:12345@127.0.0.1:3306/db",
    modules={"models": ["main"]}
)


# 定义模型类
class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)

    class Meta:
        table = "users"


@app.get("/")
async def index():
    user = await User.filter(name="liuxu").first()
    user.password = "123456789"
    await user.save()
    return user


