import datetime

users_id_data = {
    # user_id: (name, birth_date, guild_id)
    12312312: ("name", datetime.date(2002,1,1), 123123)
}

def get_user_name(user_id):
    return users_id_data.get(user_id)[0]

def get_user_birth_date(user_id):
    return users_id_data.get(user_id)[1]

def get_user_guild(user_id):
    return  users_id_data.get(user_id)[2]