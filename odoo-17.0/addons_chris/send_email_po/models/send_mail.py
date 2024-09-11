from odoo import api,models
from datetime import datetime

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def enviar_email(self):
        po = self.env['purchase.order'].search([('state','=','draft')])
        for p in po:
            print(p,"  ",p.name,"  ",p.state)

        print("------------------------")
