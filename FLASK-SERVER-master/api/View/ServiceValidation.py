from bson.json_util import dumps
import json
from api.Repository.UsersDao import UsersDao
from main.events_chat import UserConnected
from api.utils.Server_id import TYPE_ADMIN, TYPE_MODERATOR


class ServiceValidation:
    status = None
    User = UsersDao()

    def check_admin(self, creator):
        serialize_user = json.loads(dumps(self.User.get_information_user(creator)))
        type_user = int(serialize_user['type'])
        if type_user != TYPE_ADMIN:
            return False
        return True

    def check_moderator(self, creator):
        serialize_user = json.loads(dumps(self.User.get_information_user(creator)))
        type_user = int(serialize_user['type'])
        if type_user != TYPE_MODERATOR:
            return False
        return True

    def check_balance(self, buyer, product_price):
        response_user = dumps(self.User.get_information_user(buyer))
        serialize_user = json.loads(response_user)
        balance_user = float(serialize_user['balace'])
        if balance_user < product_price:
            return False
        return balance_user

    @staticmethod
    def check_session_sid(user_id):
        for user in UserConnected:
            if user['user'] == user_id:
                return user['user']