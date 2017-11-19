# -*- coding: utf-8 -*-
from odoo import api 
from odoo import http
from odoo.http import request


class MPaymentController(http.Controller):

	@http.route('/web/mpesa/paybill/account_no', auth='public')
	def get_accountno(self, **args):
		mpayment_obj = request.env['mpayment.account_paybill'].sudo()
		account_no = args[u'code'] 
		mpayment_obj.create({'account_no': account_no})
		return "OK"

	@http.route('/web/mpesa/paybill', type='json', auth='public', methods=['POST'], website=True)
	def consume_paybill_payload(self, **args):
		mpayment_obj = request.env['mpayment.account_paybill'].sudo()
		amount = args.get('amount', False)
		account_no = args.get('accountNo', False)
		msisdn = args.get('msisdn', False)
		receive_date = args.get('datetime', False)
		sender_name = args.get('senderName', False)
		check_record = mpayment_obj.search([])
		check_record.create({'account_no': account_no, 'amount': amount, 'msisdn': msisdn, 'receive_date': receive_date, 'sender_name': sender_name, 'status': 'True'})
		return {'status' : "OK"}

	@http.route('/web/mpesa/paybill/payment', auth='public')
	def check_paybill_payment_status(self, **args):
		mpayment_obj = request.env['mpayment.account_paybill'].sudo()
		acc = u'account_no'
		msi = u'msisdn'
		if acc in args.keys():
			account_no = args[u'account_no']
			payment_record = mpayment_obj.search([('account_no', '=', account_no)], limit=1, order='id desc')
			if str(payment_record.status) == 'True' and str(payment_record.confirmed) == 'False':
				payment_record.write({'confirmed': True})
				return str(payment_record.amount)
			else:
				return 'False'
		elif msi in args.keys():
			msisdn = args[u'msisdn']
			payment_record = mpayment_obj.search([('msisdn', '=', msisdn)], limit=1, order='id desc')
			if str(payment_record.status) == 'True' and str(payment_record.confirmed) == 'False':
				payment_record.write({'confirmed': True})
				return str(payment_record.sender_name) + "|" + str(msisdn) + "|" + str(payment_record.amount)
			else:
				return 'False'

	@http.route('/web/mpesa/paybill/payment/confirm', auth='public')
	def paybill_payment_confirmation(self, **args):
		mpayment_obj = request.env['mpayment.account_paybill'].sudo()
		msisdn = args[u'msisdn']
		payment_record = mpayment_obj.search([('msisdn', '=', msisdn), ('confirmed', '=', False)], limit=1, order='receive_date desc')
		payment_record_count = mpayment_obj.search_count([('msisdn', '=', msisdn), ('confirmed', '=', False)])
		if payment_record_count > 0:
			payment_record.write({'confirmed': True})
			return str(payment_record.amount)
		else:
			return 'False'

	@http.route('/web/mpesa/till', type='json', auth='public', methods=['POST'], website=True)
	def consume_till_payload(self, **args):
		mpayment_obj = request.env['mpayment.account_till'].sudo()
		amount = args.get('amount', False)
		msisdn = args.get('msisdn', False)
		receive_date = args.get('datetime', False)
		sender_name = args.get('senderName', False)
		payment_record = mpayment_obj.search([])
		payment_record.create({'amount': amount, 'msisdn': msisdn, 'receive_date': receive_date, 'sender_name': sender_name})
		return {'status': "OK"}

	@http.route('/web/mpesa/till/payment', auth='public')
	def check_till_payment_status(self, **args):
		mpayment_obj = request.env['mpayment.account_till'].sudo()
		msisdn = args[u'msisdn']
		payment_record = mpayment_obj.search([('msisdn', '=', msisdn), ('confirmed', '=', False)], limit=1, order='receive_date desc')
		payment_record_count = mpayment_obj.search_count([('msisdn', '=', msisdn), ('confirmed', '=', False)])
		if payment_record_count > 0:
			return str(payment_record.sender_name) + "|" + str(msisdn) + "|" + str(payment_record.amount)
		else:
			return 'False'

	@http.route('/web/mpesa/till/payment/confirm', auth='public')
	def till_payment_confirmation(self, **args):
		mpayment_obj = request.env['mpayment.account_till'].sudo()
		msisdn = args[u'msisdn']
		payment_record = mpayment_obj.search([('msisdn', '=', msisdn), ('confirmed', '=', False)], limit=1, order='receive_date desc')
		payment_record_count = mpayment_obj.search_count([('msisdn', '=', msisdn), ('confirmed', '=', False)])
		if payment_record_count > 0:
			payment_record.write({'confirmed': True})
			return str(payment_record.amount)
		else:
			return 'False'
