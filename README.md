# slds-maquettes-salesforce

Skill pour Claude qui génère des maquettes HTML fidèles à l'interface standard de Salesforce Lightning (record page, vue liste, formulaire, modale, console, tableau de bord), avec uniquement les classes officielles du Salesforce Lightning Design System (SLDS 2.264.1, embarqué).

Chaque maquette sort en un seul fichier HTML autonome, qui s'ouvre hors ligne dans un navigateur.

## Installation

Claude Code, comme plug-in (marketplace) :

```
/plugin marketplace add hugodevweb/slds-maquettes-salesforce
/plugin install slds-maquettes-salesforce@slds-maquettes-salesforce
```

Depuis Claude Code 2.1.275, une seule ligne suffit :

```
/plugin install slds-maquettes-salesforce --marketplace hugodevweb/slds-maquettes-salesforce
```

Claude.ai ou Claude Desktop : téléchargez le dossier `skills/slds-maquettes-salesforce` en ZIP, puis importez-le dans Réglages > Capacités > Skills.

## Utilisation

Demandez simplement une maquette Salesforce, par exemple : « Fais-moi une maquette de la page Opportunité avec un nouveau bouton Générer le devis ». Le skill choisit le patron de page, écrit le HTML puis l'assemble avec :

```bash
python3 scripts/build_mockup.py maquette.html maquette_final.html
```

## Contenu

Le skill est dans `skills/slds-maquettes-salesforce/` :

- `SKILL.md` : règles et procédure suivies par Claude.
- `references/` : patrons de pages et markup des composants courants.
- `assets/gabarit.html` : coquille d'application Lightning à compléter.
- `assets/slds.min.css`, `assets/icons/`, `assets/avatar*.jpg` : fichiers officiels du SLDS, non modifiés.
- `scripts/build_mockup.py` : assemblage du fichier final autonome (Python 3, sans dépendance).

## Licences

Le code de ce skill (SKILL.md, références, gabarit, script) est sous licence MIT.

Les fichiers du Salesforce Lightning Design System viennent de https://github.com/salesforce-ux/design-system et gardent leur licence : le CSS sous licence BSD 3-Clause, les icônes et images sous Creative Commons Attribution-NoDerivatives 4.0. Voir `NOTICE.md`.

Ce projet n'est ni affilié à Salesforce ni approuvé par Salesforce. Salesforce et Lightning sont des marques de Salesforce, Inc.
