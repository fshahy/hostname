import platform
from odoo import fields, models


class Host(models.Model):
    _name = "hostname"

    name = fields.Char(default=lambda self: platform.node())
