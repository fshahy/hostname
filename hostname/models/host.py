import os
import platform
from odoo import fields, models


class Host(models.Model):
    _name = "hostname"

    name = fields.Char(default=lambda self: platform.node(), string='Hostname')
    pid = fields.Char(default=lambda self: os.getpid(), string='Prcoess ID')
