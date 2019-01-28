import asyncio
import async_easyapi
from quart import Quart, Blueprint

loop = asyncio.get_event_loop()

app = Quart(__name__)

my_db = async_easyapi.MysqlDB('root', 'wshwoaini', 'localhost', 3306, 'EDUCATION')
loop.run_until_complete(my_db.connect())


class UserDao(async_easyapi.BusinessDaoBase):
    __db__ = my_db


class UserController(async_easyapi.BaseController):
    __dao__ = UserDao


bp = Blueprint(name='users', import_name='users', url_prefix='')


class UserHandler(async_easyapi.BaseQuartHandler):
    __controller__ = UserController


async_easyapi.register_api(app=bp, view=UserHandler, endpoint='user_api', url='/users')


@bp.route('/complex')
async def complex_api():
    res = UserController.complex_bussiness()
    return res

app.register_blueprint(bp)
if __name__ == '__main__':
    app.run()