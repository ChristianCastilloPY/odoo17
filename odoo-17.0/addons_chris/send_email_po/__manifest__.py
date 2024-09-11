# -*- coding: utf-8 -*-
{
    "name" : "Enviar Ordenes de Compra",
    "summary" : """
        Curso de programacion Odoo14, funcionalidades
    """,
    "suthor" : "Christian Castillo",
    "category" : "General",
    "version" : "1.1.1",
    'depends': ['mail', 'purchase','contacts', 'sale_management'],
    "data": [
        'data/email_template.xml',
        'views/send_mail.xml'
    ]
}
