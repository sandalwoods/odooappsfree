# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Job(models.Model):
    _inherit = 'hr.job'

    seq_number = fields.Char(string="Job ID", copy=False, readonly=True)

    @api.model
    def create(self, vals):
        seq_obj = self.env['ir.sequence']
        if 'company_id' in vals:
            vals['seq_number'] = seq_obj.with_context(force_company=vals['company_id']).next_by_code('kz.hr.job.sequence')
        else:
            vals['seq_number'] = seq_obj.next_by_code('kz.hr.job.sequence')
        return super(Job, self).create(vals)
