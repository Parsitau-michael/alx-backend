#!/usr/bin/env python3
"""SessionExpAuth class Definition
"""

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """Class Definition"""
    def __init__(self):
        self.session_duration = int(os.getenv('SESSION_DURATION')) or 0

    def create_session(self, user_id=None):
        """A method that creates a session
        Args:
            - user_id: the user id whose session is to be created
        Returns:
            - created session id
        """
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
                'user_id': user_id,
                'created_at': datetime.now()
        }

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """A method that retrieves the user id from a particular session id
        Args:
            -session_id: the session_id to extract a user id from
        Returns:
            -user_id associated with the passed session_id
        """
        if session_id is None:
            return None

        if session_id not in self.user_id_by_session_id:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)

        if self.session_duration <= 0:
            return session_dict.get('user_id')

        if 'created_at' not in session_dict:
            return None

        if (session_dict.get('created_at')\
                + timedelta(seconds=self.session_duration))\
                < datetime.now():
                    return None

        return session_dict.get('user_id')
