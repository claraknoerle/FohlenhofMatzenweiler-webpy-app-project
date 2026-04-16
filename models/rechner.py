#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RechnerModel:
    def __init__(self, alter, dauer):
        self.alter = alter
        self.dauer = dauer
        self.preis_pro_monat = 300.0

    def berechne_zukunftsalter(self):
        """Berechne das Alter nach der Aufzucht"""
        return self.alter + self.dauer

    def berechne_gesamtkosten(self):
        """Berechne Gesamtkosten: Dauer in Jahren * 12 Monate * Preis pro Monat"""
        return self.dauer * 12 * self.preis_pro_monat