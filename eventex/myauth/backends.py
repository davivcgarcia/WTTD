# coding: utf-8
"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.contrib.auth import get_user_model


class EmailBackend(object):
    """
    Backend that implements a custom authentication based on email.
    """
    def authenticate(self, email=None, password=None, **kwargs):
        """
        Method responsible for authenticate an user.
        """
        UserModel = get_user_model()

        if email is None:
            email = kwargs.get(UserModel.USERNAME_FIELD)

        try:
            user = UserModel.objects.get(email=email)
        except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned):
            return None

        if not user.check_password(password):
            return None

        return user

    def get_user(self, user_id):
        """
        Method to return the user object.
        """
        try:
            UserModel = get_user_model()
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
