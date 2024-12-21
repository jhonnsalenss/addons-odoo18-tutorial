from odoo import fields, models

class Student(models.Model):
    _name = 'student'
    _description = "Information about student"
    name = fields.Char(string="Student Name", required=True)
