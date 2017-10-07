# -*- coding: utf-8 -*-


from odoo import models, fields, api


class JournalModification(models.Model):
    _inherit = 'account.journal'
	
    mpesa_payment = fields.Boolean('MPESA Payment', help="Check if this button journal uses MPESA payment")
    mpesa_payment_type = fields.Selection([('paybill', 'Paybill'), ('till', 'Till')], string='Payment Type', default='paybill', required=True)