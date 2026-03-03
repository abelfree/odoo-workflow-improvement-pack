from odoo import _, api, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.constrains("order_line")
    def _check_non_zero_lines(self):
        for order in self:
            for line in order.order_line:
                if line.product_uom_qty <= 0:
                    raise ValidationError(_("Line quantity must be greater than zero."))
