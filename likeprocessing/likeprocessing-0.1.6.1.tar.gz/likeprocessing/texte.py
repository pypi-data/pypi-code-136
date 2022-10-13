import likeprocessing.processing as processing
import pygame
from pygame.colordict import THECOLORS as COLORS
from likeprocessing.pyDialog import Label


def textFont(police=None, taille=None) -> tuple:
    """change la police et la taille texte
    retourne la police et la taille du texte courante si aucun paramètre est passé"""
    if police is not None:
        processing.set_font(police)
    if taille is not None:
        processing.set_font_size(taille)
    return processing.get_font(), processing.get_font_size()


def textSize(taille: int = None):
    """change la taille texte
    retourne la taille du texte courante si aucun paramètre est passé"""
    if taille is not None:
        processing.set_font_size(taille)
    return processing.get_font_size()


def textCouleurCadre(couleur=None):
    """change la couleur du cadre du texte
    retourne la couleur du cadre du texte courante si aucun paramètre est passé"""
    if couleur is not None:
        processing.set_couleur_cadre_texte(couleur)
    return processing.get_couleur_bord_cadre_texte()


def text(texte: str, x, y, largeur=0, hauteur=0, **kwargs):
    """Ecrit le texte à la position x,y en fonction du style et de alignement courant"""
    fill = kwargs.get("fill", processing.get_fill_color())
    no_fill = kwargs.get("no_fill", processing.__no_fill)
    stroke = kwargs.get("stroke", processing.__border_color)
    stroke_weight = kwargs.get("stroke_weight", processing.__border_width)
    fill_mouse_on = kwargs.get("fill_mouse_on", processing.__fill_color_mouse_on)
    angle = kwargs.get("angle", 0)
    no_stroke = kwargs.get("no_stroke", False)
    if no_stroke is True:
        stroke_weight = 0

    # if processing.__rect_center_mode:
    #     x -= largeur / 2
    #     y -= hauteur / 2

    if textStyle() == "BOLD":
        b = True
        i = False
    elif textStyle() == "ITALIC":
        b = False
        i = True
    elif textStyle() == "BOLDITALIC":
        b = True
        i = True
    else:
        b = False
        i = False
    h, v = align_h = textAlign()
    kwargs["allign_h"] = kwargs.get("allign_h", h)
    kwargs["allign_v"] = kwargs.get("allign_v", v)
    # if no_fill:
    #     couleur = None
    # else:
    #     couleur = fill
    #     points = [[x, y],
    #               [x + largeur, y],
    #               [x + largeur, y + hauteur],
    #               [x, y + hauteur]]
    police, size = textFont()
    ps = pygame.font.SysFont(police, size, bold=b, italic=i)
    if largeur == 0 and hauteur == 0:
        largeur, hauteur = ps.size(texte)
        largeur += 4
        hauteur += 4
    text_bitmap = ps.render(texte, True, (0, 0, 0))
    processing.rect(x, y, largeur, hauteur, image=text_bitmap,**kwargs)
    #     if fill_mouse_on is not None and processing.in_polygone(*processing.mouseXY(), points):
    #         couleur = fill_mouse_on
    # pos = processing.transformation([[x,y]])
    # angle = angle + processing.degrees(processing.get_rotation())
    # t = Label(None, (*pos[0], largeur, hauteur), texte, angle, police=police, size=size,
    #           couleurFond=couleur,
    #           couleurBord=stroke, largeurBord=stroke_weight, bold=b, italic=i,
    #           align_h=h, align_v=v)
    # t.draw()


__border_width = 1
__fill_color = (255, 255, 255)
__border_color = (0, 0, 0)


def textWidth(chaine: str) -> int:
    """retourne la largeur en pixels de l'affichage de chaine,
     dans la police et taille actuelles"""
    f = pygame.font.SysFont(*textFont())
    return f.size(chaine)[0]


def textStyle(style: str = None) -> str:
    """change le style du texte
    NORMAL BOLD ITALIC BOLDITALIC
    retourne le style courant si aucun paramètre est passé"""
    if style is not None:
        processing.set_text_style(style.upper())
    return processing.get_text_style()


def textAlign(horizontal: str = None, vertical: str = None) -> tuple:
    """change l'alignment du texte
    horizontal : LEFT CENTER RIGHT
    veritcal : TOP CENTER BOTTOM
    retourne l'alignement courant si aucun paramètre est passé"""
    if horizontal is not None:
        processing.set_text_align_h(horizontal)
    if vertical is not None:
        processing.set_text_align_v(vertical)
    return processing.get_text_align_h(), processing.get_text_align_v()
