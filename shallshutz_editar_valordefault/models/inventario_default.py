
# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api

class finventario_default(models.Model):
	_inherit='product.template'

	
	x_metros2=fields.Float(string="M2",)
	x_largo=fields.Float(string="Largo",)
	x_ancho=fields.Float(string="Ancho",)