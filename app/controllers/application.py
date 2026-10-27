from bottle import template, request
from app.controllers.datarecord import DataRecord

class Application():

    def __init__(self):
        self.pages = {
            'helper': self.helper,
            'portal': self.portal,
            'dashboard': self.dashboard
        }
        self.__model = DataRecord()
        self.__current_username = None

    def render(self, page, parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
            return content(parameter)

    def get_session_id(self):
        return request.get_cookie('session_id')

    def helper(self):
        return template('app/views/html/helper')

    def portal(self):
        return template('app/views/html/portal')

    def dashboard(self, parameter=None):
        return template('app/views/html/dashboard')

    def is_authenticated(self, username):
        session_id = self.get_session_id()
        current_username = self.__model.getUserName(session_id)
        return username == current_username

    def authenticate_user(self, username, password):
        session_id = self.__model.checkUser(username, password)
        if session_id:
            self.logout_user()
            self.__current_username = self.__model.getUserName(session_id)
            return session_id, username
        return None, None

    def logout_user(self):
        self.__current_username = None
        session_id = self.get_session_id()
        if session_id:
            self.__model.logout(session_id)