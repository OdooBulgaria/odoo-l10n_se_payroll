# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Swedish - Payroll',
    'category': 'Localization',
    'author': 'Vertel AB',
    #~ 'depends': ['hr_payroll', 'hr_payroll_account',],
    'depends': ['hr_payroll',],
    'version': '1.0',
    'description': """
Swedish Payroll Rules.
======================

    * Employee Details
    * Employee Contracts
    * Allowances/Deductions
    * Allow to configure Basic/Gross/Net Salary
    * Employee Payslip
    * Monthly Payroll Register
    * Integrated with Holiday Management
    """,

    'auto_install': False,
    'website': 'https://www.odoo.com/page/accounting',
    'data':[
        'l10n_se_hr_payroll_view.xml',
        'l10n_se_hr_salary_rule_category_data.xml', # hr.salary.rule.category # Leif
        'l10n_se_hr_salary_rule_data.xml', # hr.salary.rule, hr.rule.input # Leif
        'l10n_se_hr_payroll_stucture_simple_data.xml', # Leif
        'l10n_se_hr_payroll_payslip_report.xml', # Leif
        #~ 'l10n_se_hr_payroll_data.xml',
		'l10n_se_hr_payroll_demo.xml', # Leif ska flyttas
        #'l10n_se_hr_payroll_data.xml',
        #~ 'data/hr.salary.rule.csv',
    ],
	'demo':[
		#~ 'l10n_se_hr_payroll_demo.xml',
	],
    'installable': True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
