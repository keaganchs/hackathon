import users

def add_test_data_to_db():
    users.create_user({
        "email": "johndoe@gmail.com",
        "password": "JDOE0Likes0Fruit"
    })

    