{
    'name' : 'tour',
    'version' : '1.0',
    'summary' : 'tour management by floweazy',
    'sequence' : -1000,
    'description' : """A tour management software which helps you to build tour bookings and everything online""",
    'category' : 'Education',
    'website' : 'https://www.odoomates.tech',
    'Licence' : 'LGPL-3',
    'depends' : ['sale','account','purchase'],
    'data' : [
        'views/tour_package.xml',
        'views/tour_inquiry_table.xml',
        'data/customer_inquiry_sequence.xml',
        'views/tour_details.xml',
        'views/tour_program.xml',
        'views/notes_vendor.xml'
    ],
    'demo' : [],
    'qweb' : [],
    'installation' : True,
    'application' : True,
    'auto_install' : False,
}
