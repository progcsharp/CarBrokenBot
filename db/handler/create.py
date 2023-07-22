from db import make_session, User, Code, Car


def create_code(car, code, description):
    session = make_session()
    code = Code(car, code, description)
    session.add(code)
    session.commit()
    session.close()
    return True


def create_car(name):
    session = make_session()
    car = Car(name)
    session.add(car)
    session.commit()
    session.close()
    return True


async def create_user(tg_id):
    session = make_session()
    user = User(tg_id=tg_id)
    session.add(user)
    session.commit()
    session.close()
    return True
