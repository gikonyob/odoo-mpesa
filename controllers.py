# -*- coding: utf-8 -*-

import string
import random
from odoo import api 
from odoo import http
from datetime import datetime
from odoo.http import request


class MPaymentController(http.Controller):

	@http.route('/web/mpesa/account_no', auth='public')
	def get_accountno(self, **args):
		mpayment_obj = request.env['mpayment.account_numbers'].sudo()
		account_no = args[u'code'] 
		mpayment_obj.create({'account_no': account_no})
		return "OK"

	@http.route('/web/mpesa/payload', type='json', auth='public', methods=['POST'], website=True)
	def consume_payload(self, **args):
		mpayment_obj = request.env['mpayment.account_numbers'].sudo()
		amount = args.get('amount', False)
		account_no = args.get('accountNo', False)
		msisdn = args.get('msisdn', False)
		receive_date = args.get('datetime', False)
		sender_name = args.get('senderName', False)
		check_record = mpayment_obj.search([('account_no', '=', account_no)])
		count_record = mpayment_obj.search_count([('account_no', '=', account_no)])
		if count_record == 1:
			check_record.write({'amount': amount, 'msisdn': msisdn, 'receive_date': receive_date, 'sender_name': sender_name, 'status': 'True'})
		else:
			check_record.create({'account_no': account_no, 'amount': amount, 'msisdn': msisdn, 'receive_date': receive_date, 'sender_name': sender_name, 'status': 'True'})
		return {'status': "OK"}

	@http.route('/web/mpesa/payment', auth='public')
	def check_payment_status(self, **args):
		mpayment_obj = request.env['mpayment.account_numbers'].sudo()
		account_no = args[u'account_no']
		payment_record = mpayment_obj.search([('account_no', '=', account_no)], limit=1, order='id desc')
		if str(payment_record.status) == 'True' and str(payment_record.confirmed) == 'False':
			payment_record.write({'confirmed': 'True'})
			return str(payment_record.amount)
		else:
			return 'False'


