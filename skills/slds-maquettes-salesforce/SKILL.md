---
name: slds-maquettes-salesforce
description: Génère des maquettes HTML fidèles à l'interface standard de Salesforce (Lightning Experience, back office) avec le Lightning Design System officiel. À utiliser dès qu'on demande une maquette, un mockup, un wireframe haute fidélité ou un écran Salesforce (record page, liste, formulaire, modale, console, tableau de bord) pour cadrer une nouvelle fonctionnalité.
---

# Maquettes Salesforce conformes au SLDS

Objectif : produire des maquettes qui ressemblent à du vrai Salesforce Lightning, pas à une imitation approximative. Pour cela, on n'invente jamais de style : on utilise uniquement les classes `slds-*` du Lightning Design System officiel (version 2.264, embarquée dans ce skill).

## Règles impératives

1. **Uniquement des classes SLDS** pour tout ce qui existe dans Salesforce (boutons, cartes, tables, formulaires, onglets, badges, modales, fils d'Ariane, etc.). Pas de CSS maison pour reproduire un composant standard.
2. **Jamais de couleurs, polices ou arrondis codés en dur** pour les éléments standards. Les couleurs viennent des classes SLDS (`slds-button_brand`, `slds-theme_success`, `slds-text-color_weak`...).
3. **Du CSS personnalisé n'est autorisé que pour la nouvelle fonctionnalité** (un composant qui n'existe pas dans le standard). Dans ce cas, le placer dans un bloc `<style>` repéré par un commentaire `/* NOUVEAU COMPOSANT : nom */` et utiliser les variables et espacements SLDS (`slds-p-around_medium`, `slds-m-bottom_small`...) pour rester cohérent.
4. **Icônes** : toujours via le sprite SLDS, jamais d'emoji ni d'icône d'une autre bibliothèque.
5. **Textes en français** par défaut (libellés Salesforce FR : « Nouveau », « Enregistrer », « Annuler », « Modifier », « Associé », « Détails », « Activité »), sauf demande contraire.
6. **Données réalistes** : noms, montants, dates et statuts plausibles, pas de « Lorem ipsum » ni de « Texte ici ».
7. **Mettre en évidence ce qui est nouveau** : si la maquette sert à cadrer une fonctionnalité, repérer clairement les éléments ajoutés par rapport au standard (voir la section « Annotations »).

## Procédure

1. **Clarifier le besoin** en une ou deux questions maximum si c'est flou : quel objet (Compte, Opportunité, objet custom...), quel type d'écran (record page, liste, formulaire, modale, assistant/flow, console), quelle fonctionnalité nouvelle. Si la demande est claire, ne pas poser de questions et partir sur des hypothèses explicites.
2. **Choisir le bon patron de page** dans `references/patterns.md` (record page, vue liste, formulaire de création, modale, console avec sous-onglets, page d'accueil, flow/assistant). Reprendre sa structure telle quelle.
3. **Vérifier les composants** dans `references/composants.md` pour reprendre le bon markup (classes exactes) plutôt que de le deviner.
4. **Partir de `assets/gabarit.html`** : il contient la coquille Lightning (barre globale, navigation d'application, zone de contenu) prête à remplir.
5. **Écrire la maquette** dans un fichier `.html` (par exemple `maquette_opportunite.html`).
6. **Assembler le fichier final** :
   ```bash
   python3 scripts/build_mockup.py maquette_opportunite.html maquette_opportunite_final.html
   ```
   Le script injecte le CSS SLDS et les icônes pour obtenir un fichier autonome, qui s'ouvre hors ligne dans un navigateur.
7. **Contrôler le rendu** (capture d'écran avec un navigateur headless si disponible) puis livrer le fichier final.

## Icônes

Dans le HTML source, référencer les icônes avec l'identifiant préfixé par le sprite :

```html
<svg class="slds-icon slds-icon-text-default slds-icon_x-small" aria-hidden="true">
  <use href="#utility-search"></use>
</svg>
```

Préfixes disponibles : `utility-` (interface : search, add, down, edit, close...), `standard-` (icônes d'objets : account, opportunity, contact, case, lead...), `action-` (actions rapides), `custom-` (custom1 à custom113 pour les objets personnalisés).

Le format officiel Salesforce (`/assets/icons/utility-sprite/svg/symbols.svg#search`) est aussi accepté : le script le convertit.

## Annotations (maquettes de cadrage)

Pour indiquer ce qui change par rapport au standard, utiliser un repère discret :

- un badge numéroté (`<span class="slds-badge slds-theme_warning">1</span>`) à côté de l'élément nouveau ;
- une légende en bas de page : « 1. Nouveau bouton « Générer le devis » : ouvre la modale de sélection des produits. »

Ne pas surcharger : une maquette de cadrage doit rester lisible par un client ou un développeur.

## À ne pas faire

- Ne pas reproduire un composant standard « de mémoire » avec du CSS maison : utiliser la classe SLDS correspondante.
- Ne pas mélanger un autre framework (Bootstrap, Tailwind, Material) avec le SLDS.
- Ne pas utiliser de logos ou marques tierces.
- Ne pas promettre qu'un composant existe en standard s'il n'est pas dans `references/composants.md` : le signaler comme composant personnalisé.

## Fichiers du skill

- `assets/slds.min.css` : CSS officiel du SLDS.
- `assets/icons/` : sprites d'icônes officiels.
- `assets/gabarit.html` : coquille d'application Lightning à compléter.
- `references/patterns.md` : structures de pages standards.
- `references/composants.md` : markup des composants les plus courants.
- `scripts/build_mockup.py` : assemblage du fichier final autonome.
