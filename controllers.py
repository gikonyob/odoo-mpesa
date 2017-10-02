# -*- coding: utf-8 -*-

import string
import random
from odoo import api 
from odoo import http
from datetime import datetime
from odoo.http import request



def generate_random():
	min_char = 5
	max_char = 13
	all_chars = string.ascii_uppercase + string.digits
	random_string = "".join(random.choice(all_chars) for x in range(random.randint(min_char, max_char)))
	return random_string

class MPaymentController(http.Controller):

	@http.route('/web/mpesa/account_no', auth='public')
	def get_accountno(self, **args):
		today_date = datetime.today().strftime('%Y-%m-%d')
		mpayment_obj = request.env['mpayment.account_numbers'].sudo() 
		account_nos_recordset = mpayment_obj.search([])
		used_account_nos = [no.account_no for no in account_nos_recordset if no.create_date.count(today_date)>0]
		while True:
			random_string = generate_random()
			if random_string in used_account_nos:
				continue
			else:
				mpayment_obj.create({'account_no': random_string})
				break
		return random_string

	@http.route('/web/mpesa/payload', type='json', auth='public', methods=['POST'], website=True)
	def consume_payload(self, **args):
		mpayment_obj = request.env['mpayment.account_numbers'].sudo()
		amount = args.get('amount', False)
		account_no = args.get('accountNo', False)
		msisdn = args.get('msisdn', False)
		receive_date = args.get('datetime', False)
		sender_name = args.get('senderName', False)
		check_record = mpayment_obj.search([('account_no', '=', account_no)])
		check_record.write({'amount': amount, 'msisdn': msisdn, 'receive_date': receive_date, 'sender_name': sender_name, 'status': 'True'})


	@http.route('/web/mpesa/payment', auth='public')
	def check_payment_status(self, **args):
		mpayment_obj = request.env['mpayment.account_numbers'].sudo()
		account_no = args[u'account_no']
		payment_record = mpayment_obj.search([('account_no', '=', account_no)])
		if str(payment_record.status) == 'True':
			return str(payment_record.amount)
		else:
			return 'False'


