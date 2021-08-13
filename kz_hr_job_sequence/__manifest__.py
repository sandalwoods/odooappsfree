# -*- coding: utf-8 -*-
{
    'name': "Generate Sequence Number for HR Position",
    'summary': """
        Generate Sequence Number (unique id) for HR Position
    """,
    'description': """
        Auto Generate Sequence Number (unique id) for HR Position
    """,
    "version": "12.0.0.1.0",
    "category": "Extra Tools",
    'author': "Kevin Zhang",
    'license': 'LGPL-3',
    "depends": ['base','hr',],
    "data": [
        'data/sequence.xml',
        'views/hr_job_view.xml',
    ],
    "application": False,
    'installable': True,
}
