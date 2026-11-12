#!/usr/bin/env python3
"""Transforme une maquette HTML (classes slds-*) en fichier autonome.

Usage : python3 build_mockup.py maquette.html [sortie.html]

Ce que fait le script :
  - injecte le CSS officiel du SLDS dans une balise <style> ;
  - injecte les sprites d'icônes (utility, standard, action, custom) dans la page,
    avec des identifiants préfixés : #utility-search, #standard-account, etc. ;
  - réécrit les références d'icônes au format officiel
    (/assets/icons/utility-sprite/svg/symbols.svg#search) vers les identifiants préfixés ;
  - remplace les chemins d'avatars /assets/images/avatarN.jpg par des images embarquées.

Le fichier produit s'ouvre hors ligne dans n'importe quel navigateur.
"""
import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SPRITES = ["utility", "standard", "action", "custom"]


def load_sprite(kind: str) -> str:
    """Retourne les <symbol> du sprite avec des ids préfixés par le type."""
    raw = (ASSETS / "icons" / f"{kind}.svg").read_text(encoding="utf-8")
    inner = re.search(r"<svg[^>]*>(.*)</svg>", raw, re.S).group(1)
    return re.sub(r'(<symbol[^>]*?\sid=")([^"]+)(")', rf"\1{kind}-\2\3", inner)


def data_uri(path: Path) -> str:
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()


def build(src: Path, dst: Path) -> None:
    html = src.read_text(encoding="utf-8")

    # 1) Références d'icônes au format officiel -> ids préfixés
    def fix_icon(m):
        return f'href="#{m.group(1)}-{m.group(2)}"'

    html = re.sub(
        r'(?:xlink:)?href="[^"]*?/icons/(utility|standard|action|custom)-sprite/svg/symbols\.svg#([\w-]+)"',
        fix_icon,
        html,
    )

    # 2) Avatars
    for n in (1, 2):
        html = re.sub(
            rf'src="[^"]*avatar{n}\.jpg"', f'src="{data_uri(ASSETS / f"avatar{n}.jpg")}"', html
        )

    # 3) CSS inline
    css = (ASSETS / "slds.min.css").read_text(encoding="utf-8")
    style = f"<style>/* SLDS officiel */\n{css}\n</style>"
    if "<!-- SLDS-CSS -->" in html:
        html = html.replace("<!-- SLDS-CSS -->", style)
    else:
        html = html.replace("</head>", style + "\n</head>", 1)

    # 4) Sprites inline
    sprites = "".join(load_sprite(k) for k in SPRITES)
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">{sprites}</svg>'
    if "<!-- SLDS-ICONS -->" in html:
        html = html.replace("<!-- SLDS-ICONS -->", svg)
    else:
        html = re.sub(r"(<body[^>]*>)", r"\1\n" + svg.replace("\\", r"\\"), html, count=1)

    dst.write_text(html, encoding="utf-8")
    print(f"OK -> {dst} ({dst.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_name(src.stem + "_final.html")
    build(src, dst)
