#!/usr/bin/python3
# -*- coding: utf-8 -*-
# (c) Philippe Verbeke 2015

import ccad.model as cm
from .specs import *

def cartemère(profondeur=dx_max_mb, largeur=dy_max_mb, épaisseur=dz_std):
    """Carte-mère Mini-ITX vue de devant, avec le panneau des E/S à l'arrière.

    Trous de fixation: C (arrière gauche), F (arrière droite), 
                       H (avant gauche), J (avant droite)
    Bords: BG (bord gauche), BA (bord arrière)
    Zone IO: IOG (limite gauche)
    Point de référence au centre du trou C: (0, 0)
    Axe x de l'arrière vers l'avant, axe y de la gauche vers la droite, 
    axe z vers le haut
    """
    pcb = cm.box(profondeur, largeur, épaisseur)
    trouC = cm.cylinder(dia_trous/2, épaisseur+1)
    trouC.translate((dx_BA_C, dy_BG_C, -0.5))
    trouF = cm.translated(trouC, (dx_CF, dy_HJ, 0.0))
    trouH = cm.translated(trouC, (dx_CH, 0.0, 0.0))
    trouJ = cm.translated(trouH, (0.0, dy_HJ, 0.0))
    
    return pcb - trouC - trouF - trouH - trouJ


def garde_cm(profondeur=dx_max_mb, largeur=dy_max_mb, épaisseur_cm=dz_std):
    """Hauteurs maximales y compris l'épaisseur du circuit imprimé.

    Zones: A (centre droit), B (gauche), C (avant droite) et D (arrière droite)
    Point de référence au coin arrière gauche de la carte
    """
    #dz_IO_facesup = 3.81 - dz_std + épaisseur_cm
                     # distance de la face supérieure du PCB au bas du panneau I/O
    
    zoneA = cm.box(profondeur - dx_C - dx_D, largeur - dy_B, dz_A - épaisseur_cm)
    zoneA.translate((dx_D, dy_B, épaisseur_cm))
    zoneB = cm.box(profondeur, dy_B, dz_B - épaisseur_cm)
    zoneB.translate((0.0, 0.0, épaisseur_cm))
    zoneC = cm.box(dx_C, largeur - dy_B, dz_C - épaisseur_cm)
    zoneC.translate((profondeur - dx_C, dy_B, épaisseur_cm))
    zoneD = cm.box(dx_D, largeur - dy_B, dz_D - épaisseur_cm)
    zoneD.translate((0.0, dy_B, épaisseur_cm))
    
    return zoneA + zoneB + zoneC + zoneD 


def iocon(épaisseur=dx_IO_max):
    """Zone des connecteurs au sein du panneau I/O (IOcon)."""
    iocon = cm.box(épaisseur, dy_C_IOconD - dy_C_IOconG, dz_facesup_IOconH)
    iocon.translate((dx_BA_C - dx_C_IO - épaisseur, dy_BG_C + dy_C_IOconG, dz_std))
    
    return iocon

def ioplate(épaisseur=dx_IO_max):
    """Panneau d'entrées/sorties (IO)."""
    ioplate = cm.box(épaisseur, dy_IO, dz_IO)
    ioplate.translate((dx_BA_C - dx_C_IO - épaisseur, dy_BG_C + dy_C_IOG, -dz_IO_faceinf))
    
    return ioplate


def garde_io(épaisseur=dx_IO_max):
    """Zone à garder libre autour du panneau d'entrées/sorties (IO)."""
    garde = cm.box(épaisseur, dy_IO + 2 * keepout_min, dz_IO + 2 * keepout_min)
    garde.translate((dx_BA_C - dx_C_IO - épaisseur, 
                     dy_BG_C + dy_C_IOG - keepout_min, 
                     -dz_IO_faceinf - keepout_min))
    
    return garde - ioplate()
    
    
def pci_cutout():
    """Emplacement pour carte PCI."""
    cutout = cm.box(dx_pci_bracket, dy_pci, dz_pci)
    cutout.translate(( (2 * -dx_pci_bracket) - dx_bracket_case,
                      -dy_pci /2 + dy_BG_pcicenter,
                       dz_faceinf_pci))
    slot = cm.box(dx_pcislot, dy_pcislot, 5.0)
    slot.translate((-(dx_pcislot / 2) - dx_pcislotctr_BA,
                    -dy_pcislot / 2 + dy_BG_pcicenter,
                    -5.0))
    
    return cutout + slot
    
    
def supportC(longueur=long_support, largeur=largeur_sup):
    """Support C de la carte-mère."""
    support = cm.cylinder(largeur / 2, longueur)
    support.translate((dx_BA_C, dy_BG_C, -longueur))
    trou = cm.cylinder((dia_vis_6_32 - (coef_pas * pas_vis_6_32)) / 2, 
                       long_vis_6_32 + 0.15)
    trou.translate((dx_BA_C, dy_BG_C, -long_vis_6_32 + 0.15))
    
    return support - trou
    
    
def supports(longueur=long_support, largeur=largeur_sup):
    """Supports C, F, H et J de la carte-mère."""
    supC = supportC(longueur, largeur)
    supF = cm.translated(supC, (dx_CF, dy_HJ, 0.0))
    supH = cm.translated(supC, (dx_CH, 0.0, 0.0))
    supJ = cm.translated(supH, (0.0, dy_HJ, 0.0))
    
    return supC + supF + supH + supJ
