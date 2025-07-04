from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Shareholder(models.Model):
    _name = 'shareholder'
    _description = 'Shareholder'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'
    _check_company_auto = True

    name = fields.Char("Name", required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string="Partner", tracking=True)
    total_shares = fields.Float(compute='_compute_totals', store=True, readonly=True, tracking=True)
    total_invested = fields.Float(compute='_compute_totals', store=True, readonly=True, tracking=True)
    share_percent = fields.Float(compute='_compute_share_percent', store=True, readonly=True, tracking=True)
    dividend_received = fields.Float(compute='_compute_dividend', store=True, readonly=True, tracking=True)
    transaction_ids = fields.One2many('share.transaction', 'shareholder_id', string="Transactions", tracking=True)
    dividend_ids = fields.One2many('share.dividend', 'shareholder_id', string="Dividends", tracking=True)


    @api.depends('total_shares')
    def _compute_share_percent(self):
        shareholders = self.env['shareholder'].search([])
        total_company_shares = sum(shareholders.mapped('total_shares'))
        for shareholder in shareholders:
            shareholder.share_percent = (shareholder.total_shares / total_company_shares * 100) if total_company_shares > 0 else 0.0

    @api.depends('dividend_ids.amount')
    def _compute_dividend(self):
        for record in self:
            record.dividend_received = sum(record.dividend_ids.mapped('amount'))


    def action_get_share_transactions(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Share Transactions',
            'view_mode': 'list',
            'res_model': 'share.transaction',
            'domain': [('shareholder_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def action_get_share_dividends(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Share Dividends',
            'view_mode': 'list',
            'res_model': 'share.dividend',
            'domain': [('shareholder_id', '=', self.id)],
            'context': "{'create': False}"
        }   