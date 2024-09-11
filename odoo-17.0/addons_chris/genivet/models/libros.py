from odoo import models, fields, api

class Libros(models.Model):
    _name = "libros"
    
    name = fields.Char(string="Nombre del libro")
    editorial = fields.Char(string="Editorial")
    prueba = fields.Char(string="Prueba")
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo')
    ], string="Estado")
    
    @api.model
    def action_cambiar_estado(self):
        for r in self:
            r.write({'estado': 'activo'})
            
        print("Este es un mensaje informativo, entre en action cambiar_estado.")

    # notificar a rolando las aprobaciones
    # @api.onchange('request_status')
        # def _notify(self, user_ids, body):
        print("Este es un mensaje informativo, entre en _notify.")
        user_ids = [3,16,17]
        body = f"Aprovado {self.name}"
        notification_ids = []
        for user_id in user_ids:
            notification_ids.append((0, 0, {
                'res_partner_id': user_id,
                'notification_type': 'inbox'
        }))

        self.message_post(
            body=body,
            message_type='notification',
            author_id=self.env.user.partner_id.id,
            partner_ids=user_ids,
            notification_ids=notification_ids
        )

