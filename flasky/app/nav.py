from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import *


topbar = Navbar('',
    View('Smarttrack', 'main.index'),
    View('Home', 'main.index'),

)
nav = Nav()
# nav.register_element(
#     'top',
#     Navbar(
#         View('Widgits, Inc.', 'main.index'),
#         # View('Our Mission', 'about'),
#         Subgroup('Products',
#                  View('Wg240-Series',
#                       'main.index',
#                       product='wg240'),
#                  View('Wg250-Series',
#                       'products',
#                       product='wg250'),
#                  Separator(),
#                  Text('Discontinued Products'),
#                  View('Wg10X',
#                       'products',
#                       product='wg10x'), ),
#         Link('Tech Support', 'http://techsupport.invalid/widgits_inc'), ))
# nav = Nav()
nav.register_element('top', topbar)