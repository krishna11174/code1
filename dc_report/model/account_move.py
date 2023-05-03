from odoo import api, fields, models, _
from num2words import num2words

class AccountFields(models.Model):
    _inherit = "account.move"

    sale_id = fields.Many2one('sale.order', string='Sale Order')
    consignee_name = fields.Many2one(comodel_name='res.partner',
                                     string='Consignee Name', store=True)

    number_to_words_tax = fields.Char('Number in words', compute='_compute_number_in_words')
    number_to_words_amount_total = fields.Char('Number in Words Of Total Amount', compute='_compute_number_in_words')
    tax = fields.Char(string='Combined Taxes' , compute='_compute_tax')

    done_qty = fields.Float(string='done_qty', compute='_compute_qty_done')

    @api.depends('line_ids.quantity')
    def _compute_qty_done(self):
        for picking in self:
            picking.done_qty = sum(picking.line_ids.filtered(lambda line: line.quantity).mapped('quantity'))


    def _compute_number_in_words(self):
        for record in self:
            record.number_to_words_tax = num2words(record.amount_tax) + ' Rupee only.'
            record.number_to_words_amount_total = num2words(record.amount_total) + ' Rupee only.'

    def _compute_tax(self):
       self.tax = ','.join([tax.name for tax in self.invoice_line_ids.tax_ids])

    # @api.depends('sale_id.consignee_name')
    # def _compute_ss(self):
    #     for delivery in self:
    #         delivery.consignee_name = delivery.sale_id.consignee_name.name
    #     print(delivery.consignee_name ,"##################################")