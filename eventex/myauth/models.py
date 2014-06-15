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

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    """
    Class to implement custom user manager.
    """
    def create_user(self, cpf, name=None, password=None):
        """
        Method to create new custom user.
        """
        user = self.model(cpf=cpf, name=name)
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self, **credentials):
        """
        Method to define new custom super user.
        """
        return self.create_user(**credentials)

class User(AbstractBaseUser):
    """
    Class to crate a custom user model.
    """
    cpf = models.CharField(max_length=11, unique=True, db_index=True)
    name = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = 'cpf'

    objects = UserManager()

    @property
    def is_staff(self):
        """
        Required method to work with admin.
        """
        return True

    def has_module_perms(self, app_label):
        """
        Required method to work with admin.
        """
        return True

    def has_perm(self, perm, obj=None):
        """
        Required method to work with admin.
        """
        return True

    def get_short_name(self):
        """
        Required method to work with admin.
        """
        return self.name

    def get_full_name(self):
        """
        Required method to work with admin.
        """
        return  self.name
