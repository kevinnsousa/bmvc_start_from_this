from app.models.user_account import UserAccount
import json
import uuid

class DataRecord():
    """Banco de dados JSON para o recurso Usuários"""

    def __init__(self):
        self.__user_accounts = []
        self.__authenticated_users = {}
        self.read()

    def read(self):
        try:
            with open("app/controllers/db/user_accounts.json", "r") as arquivo_json:
                user_data = json.load(arquivo_json)
                self.__user_accounts = [UserAccount(**data) for data in user_data]
        except FileNotFoundError:
            self.__user_accounts.append(UserAccount('Guest', '010101'))

    def getCurrentUser(self, session_id):
        if session_id in self.__authenticated_users:
            return self.__authenticated_users[session_id]
        return None

    def getUserName(self, session_id):
        if session_id in self.__authenticated_users:
            return self.__authenticated_users[session_id].username
        return None

    def checkUser(self, username, password):
        for user in self.__user_accounts:
            if user.username == username and user.password == password:
                session_id = str(uuid.uuid4())
                self.__authenticated_users[session_id] = user
                return session_id
        return None

    def logout(self, session_id):
        if session_id in self.__authenticated_users:
            del self.__authenticated_users[session_id]