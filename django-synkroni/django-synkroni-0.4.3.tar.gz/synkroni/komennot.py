# -*- coding: utf-8 -*-

''' Tilapäinen taaksepäin yhteensopivuus. '''

from .toiminnot import toiminto, muuttaa_tietoja, Toiminnot

_komento = toiminto
_datapaivitys = muuttaa_tietoja
Komennot = Toiminnot
Komennot.suorita_komento = Komennot.suorita_toiminto
