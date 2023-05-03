from odoo import api, fields, models, _


class ewaybill_fields_account(models.Model):
    _inherit = 'account.move'

    trans_gstin_no = fields.Char(string='Transporter GSTIN No')
    pay_terms = fields.Char(string='Payment Terms')
    time_preparation = fields.Datetime(string='Date/Time of Preparation')
    time_removal = fields.Datetime(string='Date/Time of Removal of goods')
    llr_no = fields.Char(string='LR / RR No')
    documents_any = fields.Char(string='Document (If any)')
    delivery_no = fields.Char('Delivery No')
    llr_no = fields.Char(string='LR / RR No')


    ic_no = fields.Char('IC No.')
    ic_date = fields.Date('IC Date')
    serial_no = fields.Char('Serial No.')
    insurance_no = fields.Char('Insurance No.')


class ewaybill_fields_stock(models.Model):
    _inherit = 'stock.picking'

    trans_gstin_no = fields.Char(string='Transporter GSTIN No')
    pay_terms = fields.Char(string='Payment Terms')
    time_preparation = fields.Datetime(string='Date/Time of Preparation')
    time_removal = fields.Datetime(string='Date/Time of Removal of goods')
    llr_no = fields.Char(string='LR / RR No')
    documents_any = fields.Char(string='Documents (if any)')

    # def action_create_sale_invoice(self):
    #     # res = super(ewaybill_fields_stock, self).action_create_sale_invoice()
    #     invoice_vals = []
    #
    #     invoice_vals.append({
    #         'consignee_name': self.consignee_name.id,
    #                 'trans_gstin_no': self.trans_gstin_no,
    #                 'pay_terms': self.pay_terms,
    #                 'time_preparation': self.time_preparation,
    #                 'time_removal':self.time_removal,
    #                 'llr_no' : self.llr_no,
    #                 'documents_any' : self.documents_any,
    #     })
    #     res = super(ewaybill_fields_stock, self).action_create_sale_invoice()
    # invoice_list.append(invoice_vals)

        #
        # return res
