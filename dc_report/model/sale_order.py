from odoo import api, fields, models, _

class Salefield(models.Model):
    _inherit = "sale.order"

    consignee_name = fields.Many2one(comodel_name='res.partner',
                                     string='Consignee Name', store=True)
    mode_of_transport = fields.Char(string='Mode Of Transport')
    vehical_no = fields.Char(string='Vehical No')

    def _prepare_invoice(self):
        res = super(Salefield, self)._prepare_invoice()

        res.update({
            'consignee_name': self.consignee_name.id,
            # e-waybill fields
            'delivery_no': self.picking_ids.name,
            'veh_no': self.picking_ids.veh_no,
            'veh_type': self.picking_ids.veh_type,
            'trans_id': self.picking_ids.trans_id,
            'trans_name': self.picking_ids.trans_name,
            'distance': self.picking_ids.distance,
            'transMode': self.picking_ids.transMode,
            'transporter_docno': self.picking_ids.transporter_docno,
            'transporter_docdt' : self.picking_ids.transporter_docdt,
            'trans_gstin_no': self.picking_ids.trans_gstin_no,
            'documents_any' : self.picking_ids.documents_any,
            'pay_terms': self.picking_ids.pay_terms,
            'time_preparation': self.picking_ids.time_preparation,
            'time_removal': self.picking_ids.time_removal,
            'llr_no': self.picking_ids.llr_no,
            'ic_no': self.picking_ids.ic_no,
            'ic_date': self.picking_ids.ic_date,
            'serial_no': self.picking_ids.serial_no,
            'insurance_no' : self.picking_ids.insurance_no
        })
        return res


class partener(models.Model):
    _inherit = "res.partner"

    def name_get(self):
        result = []
        for record in self:
            name = record.name
            if self.env.context.get('consigne_name', False):
                result.append((record.id, "{}".format(name)))
                print(name)
            else:
                return super(partener, self).name_get()
        return result

    def name_get(self):
        result = []
        for record in self:
            name = record.name
            if self.env.context.get('custom_field', False):
                result.append((record.id, "{}".format(name)))
                print(name)
            else:
                return super(partener, self).name_get()
        return result


class picking(models.Model):
    _inherit = "stock.picking"

    sale_id = fields.Many2one('sale.order', string='Sale Order')
    consignee_name = fields.Many2one(comodel_name='res.partner',
                                     string='Consignee Name', compute='_compute_ss', readonly=False, store=True)

    done_qty = fields.Float(string='Done Quantity', compute='_compute_done_qty', store=True)

    @api.depends('move_line_ids.qty_done')
    def _compute_done_qty(self):
        for picking in self:
            picking.done_qty = sum(picking.move_line_ids.filtered(lambda line: line.qty_done).mapped('qty_done'))

    @api.depends('sale_id.consignee_name')
    def _compute_ss(self):
        for delivery in self:
            delivery.consignee_name = delivery.sale_id.consignee_name

    def write(self, vals):
        if 'consignee_name' in vals:
            new_ss = vals.get('consignee_name')
            for delivery in self:
                # Check if the delivery order is a backorder
                if delivery.backorder_id:
                    # Create a new delivery order for the backorder
                    new_delivery = delivery.copy({'backorder_id': False})
                    # Update the value of the consignee_name field in the new delivery order
                    new_delivery.write({'consignee_name': new_ss})
                else:
                    # Update the value of the consignee field in the current delivery order
                    delivery.sale_id.write({'consignee_name': new_ss})
                    delivery = super(picking, delivery).write({'consignee_name': new_ss})
        else:
            delivery = super(picking, self).write(vals)
        return delivery
