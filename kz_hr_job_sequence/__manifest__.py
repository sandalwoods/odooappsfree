# -*- coding: utf-8 -*-
{
    'name': "Generate ID for Job Position",
    'summary': """
        Generate Sequence Number (unique id) for Job Position
    """,
    'description': """
        Auto Generate Sequence Number (unique id) for Job Position
    """,
    "version": "12.0.0.1.1",
    "category": "Extra Tools",
    'author': "Kevin Zhang",
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    "depends": ['base','hr',],
    "data": [
        'data/sequence.xml',
        'views/hr_job_view.xml',
    ],
    "application": False,
    'installable': True,
}
