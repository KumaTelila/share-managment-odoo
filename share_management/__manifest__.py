{
    'name': "Share Management",
    'summary': "Manage shareholders",
    'version': '1.0',
    'depends': ['base', 'mail'], 
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/share_transaction_views.xml',
        'views/share_dividend_views.xml',
        'views/shareholder_views.xml',
        'views/menu.xml',
        'data/cron.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}