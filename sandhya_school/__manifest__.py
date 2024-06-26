{
    'name' : 'school management',
    'version' : '1.0',
    'summary' : 'school management by floweazy',
    'sequence' : -1000,
    'description' : """A school management software which helps you to build admissions and everything online""",
    'category' : 'Education',
    'website' : 'https://www.odoomates.tech',
    'Licence' : 'LGPL-3',
    'depends' : ['contacts'],
    'data' : [
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/professors.xml',
        'views/registration.xml',
        'views/subject.xml',
        'views/parent.xml',
        'views/classes.xml',
        #'views/contact.xml'

    ],
    'demo' : [],
    'qweb' : [],
    'installation' : True,
    'application' : True,
    'auto_install' : False,
}
