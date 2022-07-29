{
    'name': 'Odoo Hosts',
    'version': '15.0.0',
    'summary': 'Display Odoo hostname',
    'description': 'Create a new record with the Odoo hostname',
    'category': 'hidden',
    'author': 'fshahy',
    'depends': ['web',],
    'data': [
        'security/ir.model.access.csv',
        'views/host_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
