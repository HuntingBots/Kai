from AsunaRobot import mongodb as db_x

lydia = db_x["CHATBOT"]


def add_chat(chat_id):
    stark = lydia.find_one({"chat_id": chat_id})
    if stark:
        return False
    lydia.insert_one({"chat_id": chat_id})
    return True


def remove_chat(chat_id):
    stark = lydia.find_one({"chat_id": chat_id})
    if not stark:
        return False
    lydia.delete_one({"chat_id": chat_id})
    return True


def get_all_chats():
    r = list(lydia.find())
    if r:
        return r
    return False


def get_session(chat_id):
    stark = lydia.find_one({"chat_id": chat_id})
    if not stark:
        return False
    return stark
