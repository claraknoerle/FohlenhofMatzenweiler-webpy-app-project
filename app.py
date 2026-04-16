#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from controllers.main import MainController

# URL-Routing
urls = (
    '/', 'MainController',
    '/rechner', 'MainController',
    '/galerie', 'MainController',
    '/impressum', 'MainController',
    '/datenschutz', 'MainController',
)

# Anwendung initialisieren
app = web.application(urls, globals())

# Templates konfigurieren
render = web.template.render('views/', base='base')

if __name__ == "__main__":
    app.run()