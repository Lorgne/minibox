#!/usr/bin/python3
# -*- coding: utf-8 -*-
# (c) Philippe Verbeke 2015

# Modélisation d'une carte-mère Mini-ITX
# Dimensions maximales et minimales et épaisseur standard en millimètres
dx_max_mb = 170.0 # Profondeur maximale
dy_max_mb = 170.0 # Largeur maximale
dz_std = 1.57     # Epaisseur standard du PCB
dx_IO_min = 0.94  # épaisseur minimale du panneau I/O
dx_IO_max = 1.32  # épaisseur maximale du panneau I/O

# Cotes du PCB de la carte-mère
dia_trous = 3.96  # diamètre des trous de fixation
dx_BA_C = 10.16   # distance x du bord arrière de la carte au centre du trou C
dy_BG_C = 6.35    # distance y du bord gauche de la carte au centre du trou C
dx_CF = 22.86     # distance sur l'axe x du trou C au trou F
dx_CH = 154.94    # distance sur l'axe x du trou C au trou H
dy_HJ = 157.48    # distance sur l'axe y du trou H au trou J

# Cotes d'encombrement maximum des composants de la carte-mère
dz_A = 57.0       # hauteur de la zone A
dz_B = 16.0       # hauteur de la zone B
dy_B = 15.0       # Largeur de la zone B
dz_C = 38.0       # hauteur de la zone C
dx_C = 30.0       # Profondeur de la zone C
dz_D = 39.0       # hauteur de la zone D
dx_D = 27.0       # Profondeur de la zone D
d_autour = 6.35   # Zone libre minimale autour de la CM

# Cotes des supports de la carte-mère
dia_vis_6_32 = 3.5052     # Diamètre extérieur d'une vis 6-32
pas_vis_6_32 = 0.79375    # Pas d'une vis 6-32
coef_pas = 1.082532       # Rapport du pas de vis à 2 fois la profondeur du filet
long_vis_6_32 = 6.35      # Longeur max. d'une vis 6-32
long_min_support = 6.35   # Longueur minimale des supports
largeur_max_sup = 10.16   # Largeur maximale de la section des supports

# Cotes de la zone des connecteurs du panneau I/O
dx_C_IO = 12.27            # distance x du trou C à la face intérieure du panneau I/O
dy_C_IOconG = 10.82        # distance y du trou C au bord gauche de la zone des connecteurs
dy_C_IOconD = 162.97       # distance y du trou C au bord droit de la zone des connecteurs
dz_facesup_IOconH = 37.34  # dist. z de la face sup. du PCB au haut de la zone des connecteurs
# dx_BA_C, dy_BG_C, dz_std

# Cotes du panneau I/O 
dy_IO = 158.75        # Largeur du panneau I/O
dz_IO = 44.45         # Hauteur du panneau I/O
dy_C_IOG = 7.52       # distance y du trou C au bord gauche du panneau I/O
dz_IO_faceinf = 2.24  # distance de la face inférieure du PCB au bas du panneau I/O
R_max_coin_IO = 0.99  # Rayon maximum des coins du panneau I/O
# dx_C_IO, dx_BA_C, dy_BG_C

# Cotes de la zone libre entourant le panneau I/O
keepout_min = 2.54    # Zone libre entourant le panneau I/O
# dy_IO, dz_IO, dx_C_IO, dy_C_IOG, dy_BG_C, dx_BA_C, dz_IO, dz_IO_faceinf

# Cotes emplacement 2,5 pouces SSD
dx_ssd = 100.20       # Longueur SSD
dy_ssd = 69.85        # Largeur SSD
dz_ssd_max = 19.05    # Hauteur max. SSD

# Cotes découpe pour carte PCI (pci). Vis 6-32.
dz_pci = 93.675          # Hauteur de la découpe pour carte PCI en face arrière
dy_pci = 15.875          # Largeur de la découpe pour carte PCI en face arrière
dy_BG_pcicenter = 1.295  # Distance du centre de la découpe PCI au bord gauche de la CM
dz_faceinf_pci = 8.052   # Distance de bas du PCB au bas de la découpe PCI
dz_pcibracket = 110.62   # Distance du bas du PCB au haut de l'attache PCI
dx_pci_bracket = 1.143   # Distance du bord arr. de la CM à la face extérieure de l'attache PCI
dx_bracket_case = 0.508  # Dist. de la face ext. de l'attache PCI à la face intérieure du boîtier
dx_vispci_BA = 6.223     # Dist. du bord arrière de la CM au centre de la vis de fixation PCI
dy_BG_vispci = 9.601     # Dist. du bord gauche de la CM au centre de la vis de fixation PCI
dia_trouvis = 2.71       # Vis 6-32
dx_pcislot = 1.372       # longueur de l'encoche de maintien de l'attache PCI
dy_pcislot = 10.643      # largeur de l'encoche de maintien de l'attache PCI
dx_pcislotctr_BA = 0.686 # Dist. du centre de la découpe PCI au bord arrière de la CM

# Cotes modifiées
long_support = long_min_support + 1.15 # Longueur des supports
largeur_sup = largeur_max_sup-1.16     # Largeur des supports
dx_baie_SSD = dx_ssd + 30.0            # Longueur baie SSD
