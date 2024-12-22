# -*- coding: utf-8 -*-
from odoo import models, fields

class MyUser(models.Model):
    _inherit = 'res.users'

    def create_my_user(self, name,login, email):
            return self.create({
                'name': name,
                'email': email,
                'login': login,
            })