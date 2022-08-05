# -*- coding: utf-8 -*-
# from odoo import http


# class Deposit(http.Controller):
#     @http.route('/deposit/deposit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/deposit/deposit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('deposit.listing', {
#             'root': '/deposit/deposit',
#             'objects': http.request.env['deposit.deposit'].search([]),
#         })

#     @http.route('/deposit/deposit/objects/<model("deposit.deposit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('deposit.object', {
#             'object': obj
#         })
