from sanic import Sanic
from handlers.routes import blueprint as service_one_blueprint
from tortoise import Tortoise

DATABASE_URL = "sqlite://db.sqlite3"


app = Sanic("ServiceOneApp")
app.blueprint(service_one_blueprint)

@app.listener('before_server_start')
async def init_db(app, loop):
    config = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["models.models"],
            "default_connection": "default",
            }
        },
    }
    await Tortoise.init(config)
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True, auto_reload=True)
