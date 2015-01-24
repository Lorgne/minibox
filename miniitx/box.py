#!/usr/bin/python3
# -*- coding: utf-8 -*-
# (c) Philippe Verbeke 2015

import ccad.model as cm
from .specs import *

def boitier(profondeur=200, largeur=200):
    """Boîtier Mini-ITX"""
    fond = cm.box(profondeur, largeur, dz_ssd_max + 2.95)
    fond.translate(((dx_max_mb - profondeur) / 2, 
                    (dy_max_mb - largeur) / 2, 
                    -(dz_ssd_max + 2.95) - long_min_support))
    ssd1 = cm.box(dx_baie_SSD, dy_ssd, dz_ssd_max + 0.1)
    ssd1.translate(((dx_max_mb - profondeur) / 2 + profondeur - dx_baie_SSD - 10.0, 
                   (dy_max_mb / 2) - dy_ssd - 2.50, 
                   -dz_ssd_max - long_min_support))
    ssd2 = cm.translated(ssd1, (0.0, dy_ssd + 5.00, 0.0))

    return fond - ssd1 - ssd2
