from odoo import models, fields

class ShareDividend(models.Model):
    _name = 'share.dividend'
    _description = 'Share Dividend'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'shareholder_id'
    _order = 'create_date desc'
    _check_company_auto = True

    shareholder_id = fields.Many2one('shareholder', string="Shareholder", required=True, tracking=True)
    amount = fields.Float(required=True, tracking=True)
    date = fields.Date(default=fields.Date.today, tracking=True)