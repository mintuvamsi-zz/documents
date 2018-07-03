# -*- coding: utf-8 -*-

from odoo import models, fields, api

class chartofaccountshierarchy(models.Model):
    _inherit = 'account.account'

    parent_account = fields.Many2one('account.group',string='Parent')

    @api.one
    @api.onchange('parent_id')
    def on_change_from_company_id(self):
      if self.parent_id: # and self.parent_account:
        # pdb.set_trace()
        self.parent_account=self.parent_id

 #    user_type = fields.Selection(
 #    	[('Receivable','Receivable'),('Payable','Payable'),
 #    	('Bank and Cash','Bank and Cash'),('Credit Card','Credit Card'),('Current Assets','Current Assets'),
 #    	('Non-current Assets','Non-current Assets'),('Prepayments','Prepayments'),('Fixed Assets','Fixed Assets'),
 #    	('Current Liabilities','Current Liabilities'),('Non-current Liabilities','Non-current Liabilities'),
 #    	('Equity','Equity'),('Current Year Earnings','Current Year Earnings'),('Other Income','Other Income'),
 #    	('Income','Income'),('Depreciation','Depreciation'),('Expenses','Expenses'),('Cost of Revenue','Cost of Revenue'),
 #    	('Global','Global')], default="Global")
 #########################################################################################################################################

# class accounthierarchy(models.Model):
# 	_name = 'account.hierarchy'
# 	_rec_name = 'parent_account'

# 	parent_account = fields.Char(string="Parent")
# 	code_hierar = fields.Char(string="Code")
