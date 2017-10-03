# -*- coding: utf-8 -*-


from odoo import models, fields, api

class MpesaAccountNumbers(models.Model):
	_name = 'mpayment.account_numbers'

	account_no = fields.Char('Account number', help='Random account number generated')
	msisdn = fields.Char('Mobile number', help='Mobile number of sender') 
	amount = fields.Integer('Amount', help='Amount received')
	receive_date = fields.Date('Received timestamp', help='Datetime amount was recieved')
	sender_name = fields.Char('Sender name', help='Name of sender')
	status = fields.Boolean('Receipt status', help='If amount is recieved or not')
	confirmed = fields.Boolean('POS confirmation', help='If amount is recieved in POS or not')