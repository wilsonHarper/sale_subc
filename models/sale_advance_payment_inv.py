from odoo import models, api

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    @api.multi
    def create_invoices(self):
        # Obtener pedidos seleccionados
        sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
        new_invoices = self.env['account.move']

        for order in sale_orders:
            # Creamos factura sin validar si hay borradores
            invoice = order._create_invoices(final=False)  # factura en borrador
            new_invoices |= invoice

        return {
            'name': 'Facturas Borrador',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', new_invoices.ids)],
        }
    