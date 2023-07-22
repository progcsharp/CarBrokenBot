from db import make_session, Code, Car, User


async def get_code_by_car_id_and_name(car_id, name):
    session = make_session()
    code = session.query(Code).filter(Code.car == car_id, Code.code == name).first()
    return code


async def get_cars():
    session = make_session()
    cars = session.query(Car).all()
    session.close()
    return cars


async def get_user_by_tg_id(tg_ig):
    session = make_session()
    user = session.query(User).filter(User.tg_id == tg_ig).first()
    session.close()
    return user
