#!/usr/bin/python3
# -*- coding: utf-8 -*-
# (c) Philippe Verbeke 2015

import OCC.Display.SimpleGui as SimpleGui
from miniitx.content import *
from miniitx.box import *


def init_affichage():
    """Initialisation d'une fenêtre 3D"""
    display, start_display, add_menu, add_function_to_menu = SimpleGui.init_display()
    return display, start_display, add_menu, add_function_to_menu
    

def affiche(obj, display, color=None, transparency=None):
    """Affiche un forme dans une fenêtre 3D.
    
    Les noms de couleur sont ceux du système X11. La transparence s'exprime de 0.0 à 1.0.
    """
    display.DisplayShape(obj.shape, update=True, color=color, transparency=transparency)
    
    
def affiche_tout():
    cm = cartemère()
    io = ioplate() - iocon()
    ko_cm = garde_cm()
    ko_io = garde_io()
    sup = supports()
    boite = boitier()
    pci = pci_cutout()
    d, start_display, add_menu, add_function_to_menu = init_affichage()
    affiche(cm, d, 'DarkGreen', 0.9)
    affiche(io, d, 'SlateGray', 0.9)
    affiche(ko_cm, d, 'Violet', 0.9)
    affiche(ko_io, d, 'Red')
    affiche(sup, d)
    affiche(boite, d)
    affiche(pci, d)
    start_display()


if __name__ == '__main__':
    affiche_tout()
