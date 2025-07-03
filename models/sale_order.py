# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.returns('account.move')
    def _create_invoices(self, grouped=False, final=False, date=None):
        """ 
        SOBRESCRITURA (Odoo 17): Modificado el método _create_invoices del módulo sale_subscription.
        
        Objetivo: Eliminar la validación que impide la creación de nuevas facturas
        si ya existen facturas en borrador para la misma orden de suscripción recurrente.
        
        Cómo funciona: Al llamar directamente a super(), estamos saltando el bloque
        de validación específico que el módulo sale_subscription añadió a este método,
        permitiendo que el proceso de facturación continúe sin el error.
        """
        
        # Llama al método _create_invoices de la clase padre (el original de sale, o el siguiente en la cadena de herencia).
        # Esto efectivamente omite la validación específica del módulo sale_subscription
        # que estaba causando el error.
        invoices = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final, date=date)
        
        return invoices