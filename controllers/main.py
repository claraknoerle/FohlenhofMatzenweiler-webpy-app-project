#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from models.rechner import RechnerModel

class MainController:
    def GET(self):
        # Route basierend auf Pfad bestimmen
        path = web.ctx.path

        if path == '/':
            return self.home()
        elif path == '/rechner':
            return self.rechner_form()
        elif path == '/galerie':
            return self.galerie()
        elif path == '/impressum':
            return self.impressum()
        elif path == '/datenschutz':
            return self.datenschutz()
        else:
            return self.home()

    def POST(self):
        path = web.ctx.path

        if path == '/rechner':
            return self.rechner_calc()
        else:
            return self.home()

    def home(self):
        return render.home()

    def rechner_form(self):
        return render.rechner()

    def rechner_calc(self):
        data = web.input()
        alter = float(data.get('alter', 0))
        dauer = float(data.get('dauer', 0))

        model = RechnerModel(alter, dauer)
        zukunftsalter = model.berechne_zukunftsalter()
        gesamtkosten = model.berechne_gesamtkosten()

        return render.rechner(alter=alter, dauer=dauer,
                            zukunftsalter=zukunftsalter,
                            gesamtkosten=gesamtkosten)

    def galerie(self):
        return render.galerie()

    def impressum(self):
        return render.impressum()

    def datenschutz(self):
        return render.datenschutz()