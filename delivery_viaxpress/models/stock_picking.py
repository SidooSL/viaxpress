###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import _, fields, models, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    viaxpress_public_tracking_ref = fields.Char(
        string="ViaXpress Barcode",
        readonly=True,
        copy=False,
    )

    is_allowed_intraday = fields.Boolean(
        string="Is allowed intraday",
        readonly=True,
        related='company_id.viaxpress_intraday',
    )

    is_viaxpress_delivery = fields.Boolean(
        string="Is ViaXpress Delivery",
        readonly=True,
        compute='_compute_is_viaxpress_delivery',
        store=True,
    )

    is_intraday = fields.Boolean(
        string="Intraday",
        copy=False,
    )

    @api.depends('carrier_id', 'carrier_id.delivery_type')
    def _compute_is_viaxpress_delivery(self):
        for record in self:
            is_viaxpress_delivery = record.carrier_id.delivery_type == 'viaxpress'

            if not is_viaxpress_delivery:
                record.is_intraday = False

            record.is_viaxpress_delivery = is_viaxpress_delivery

    def _viaxpress_get_label(self, tracking_ref):
        pdf = self.carrier_id.viaxpress_get_label(tracking_ref)
        label_name = "viaxpress_{}.pdf".format(tracking_ref)

        return (label_name, pdf)

    def send_to_shipper(self):
        self.ensure_one()
        res = self.carrier_id.send_shipping(self)[0]
        ammount_total = self.sale_id._compute_amount_total_without_delivery()

        if (self.carrier_id.free_over
                and self.sale_id
                and ammount_total >= self.carrier_id.amount):

            res['exact_price'] = 0.0
        self.carrier_price = res['exact_price']
        if res['tracking_number']:
            self.carrier_tracking_ref = res['tracking_number']
        order_currency = self.sale_id.currency_id or self.company_id.currency_id
        msg = _(
            "Shipment sent to carrier %s for shipping with tracking number %s<br/>Cost: %.2f %s"
        ) % (
            self.carrier_id.name,
            self.carrier_tracking_ref,
            self.carrier_price,
            order_currency.name
        )

        att = []
        att.append(self._viaxpress_get_label(self.viaxpress_public_tracking_ref))

        self.message_post(body=msg, attachments=att)
