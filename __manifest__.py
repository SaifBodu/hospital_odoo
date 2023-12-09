# custom_addons/hospital_management/__manifest__.py

{
    'name': 'Hospital Management',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Abdishakur',
    'category': 'Health',
    'description': 'Hospital Management System Odoo Module',
    'data': [
        'views/patient_views.xml',
        'views/doctor_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/doctor_views.xml',
    ],
}
