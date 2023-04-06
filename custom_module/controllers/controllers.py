# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class CustomModule(http.Controller):
    @http.route('/contactus', auth='public', website=True)
    def contactus(self, **kw):
        countries = request.env['res.country'].sudo().search([])
        return http.request.render('custom_module.custom_contactus_form', {
            'countries': countries
        })
