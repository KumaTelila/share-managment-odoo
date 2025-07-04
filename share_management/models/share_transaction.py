from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ShareTransaction(models.Model):
    _name = 'share.transaction'
    _description = 'Share Transaction'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'shareholder_id'
    _order = 'create_date desc'


    shareholder_id = fields.Many2one('shareholder', string="Shareholder", required=True, tracking=True, ondelete="cascade")
    type = fields.Selection([('buy', 'Buy'), ('sell', 'Sell'), ('transfer', 'Transfer')], required=True, tracking=True)
    quantity = fields.Float(required=True, tracking=True)
    price_per_share = fields.Float(tracking=True)
    amount = fields.Float(compute='_compute_amount', store=True, readonly=True, tracking=True)
    receiver_id = fields.Many2one('shareholder', string="Receiver", tracking=True, domain="[('id', '!=', shareholder_id)]", ondelete="cascade")
    date = fields.Date(default=fields.Date.today, tracking=True)

    @api.depends('quantity', 'price_per_share')
    def _compute_amount(self):
        for record in self:
            record.amount = record.quantity * record.price_per_share if record.type in ['buy', 'sell'] else 0.0
        
    
    @api.model
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.type == 'buy':
                record.shareholder_id.total_shares += record.quantity
                record.shareholder_id.total_invested += record.amount
            elif record.type == 'sell':
                if record.quantity > record.shareholder_id.total_shares:
                    raise ValidationError("Insufficient shares to sell.")
                record.shareholder_id.total_shares -= record.quantity
                record.shareholder_id.total_invested -= record.amount            
            elif record.type == 'transfer':
                if record.quantity > record.shareholder_id.total_shares:
                    raise ValidationError("Insufficient shares to transfer.")
                record.shareholder_id.total_shares -= record.quantity
                if record.receiver_id:
                    record.receiver_id.total_shares += record.quantity
        return records


