# Composants SLDS : markup de référence

Tous les exemples utilisent des classes SLDS officielles. Les icônes se référencent avec `href="#utility-xxx"` (voir SKILL.md).

## Boutons

```html
<button class="slds-button slds-button_neutral">Annuler</button>
<button class="slds-button slds-button_brand">Enregistrer</button>
<button class="slds-button slds-button_outline-brand">Modifier</button>
<button class="slds-button slds-button_destructive">Supprimer</button>
<button class="slds-button slds-button_success">Convertir</button>
<button class="slds-button slds-button_text-destructive">Retirer</button>

<!-- Bouton avec icône -->
<button class="slds-button slds-button_neutral">
  <svg class="slds-button__icon slds-button__icon_left" aria-hidden="true"><use href="#utility-add"></use></svg>
  Nouveau
</button>

<!-- Bouton icône seule -->
<button class="slds-button slds-button_icon slds-button_icon-border-filled" title="Plus d'actions">
  <svg class="slds-button__icon" aria-hidden="true"><use href="#utility-down"></use></svg>
</button>

<!-- Groupe de boutons -->
<ul class="slds-button-group-list">
  <li><button class="slds-button slds-button_neutral">Modifier</button></li>
  <li><button class="slds-button slds-button_neutral">Cloner</button></li>
  <li><button class="slds-button slds-button_icon slds-button_icon-border-filled"><svg class="slds-button__icon" aria-hidden="true"><use href="#utility-down"></use></svg></button></li>
</ul>
```

## Badges, pastilles, étiquettes

```html
<span class="slds-badge">Brouillon</span>
<span class="slds-badge slds-theme_success">Gagné</span>
<span class="slds-badge slds-theme_warning">À valider</span>
<span class="slds-badge slds-theme_error">Refusé</span>
<span class="slds-badge slds-badge_lightest">Info</span>

<!-- Pill (valeur sélectionnée) -->
<span class="slds-pill">
  <span class="slds-pill__label">Acme SA</span>
  <button class="slds-button slds-button_icon slds-pill__remove" title="Retirer">
    <svg class="slds-button__icon" aria-hidden="true"><use href="#utility-close"></use></svg>
  </button>
</span>
```

## Carte

```html
<article class="slds-card">
  <div class="slds-card__header slds-grid">
    <header class="slds-media slds-media_center slds-has-flexi-truncate">
      <div class="slds-media__figure">
        <span class="slds-icon_container slds-icon-standard-contact">
          <svg class="slds-icon slds-icon_small" aria-hidden="true"><use href="#standard-contact"></use></svg>
        </span>
      </div>
      <div class="slds-media__body">
        <h2 class="slds-card__header-title"><span>Contacts (3)</span></h2>
      </div>
    </header>
    <div class="slds-no-flex"><button class="slds-button slds-button_neutral">Nouveau</button></div>
  </div>
  <div class="slds-card__body slds-card__body_inner">Contenu</div>
  <footer class="slds-card__footer"><a href="#">Tout afficher</a></footer>
</article>
```

## Tableau de données

```html
<table class="slds-table slds-table_cell-buffer slds-table_bordered">
  <thead>
    <tr class="slds-line-height_reset">
      <th scope="col"><div class="slds-truncate" title="Nom">Nom</div></th>
      <th scope="col"><div class="slds-truncate" title="Montant">Montant</div></th>
      <th scope="col"><div class="slds-truncate" title="Étape">Étape</div></th>
      <th scope="col"></th>
    </tr>
  </thead>
  <tbody>
    <tr class="slds-hint-parent">
      <th scope="row"><div class="slds-truncate"><a href="#">Acme - Renouvellement</a></div></th>
      <td><div class="slds-truncate">48 000,00 €</div></td>
      <td><div class="slds-truncate">Négociation</div></td>
      <td>
        <button class="slds-button slds-button_icon slds-button_icon-border-filled slds-button_icon-x-small">
          <svg class="slds-button__icon" aria-hidden="true"><use href="#utility-down"></use></svg>
        </button>
      </td>
    </tr>
  </tbody>
</table>
```

Variantes : `slds-table_striped`, `slds-table_col-bordered`, `slds-no-row-hover`.

## Formulaires

```html
<div class="slds-form-element">
  <label class="slds-form-element__label" for="nom">
    <abbr class="slds-required" title="obligatoire">*</abbr> Nom de l'opportunité
  </label>
  <div class="slds-form-element__control">
    <input type="text" id="nom" class="slds-input" placeholder="Saisir un nom" />
  </div>
</div>

<!-- Liste déroulante -->
<div class="slds-form-element">
  <label class="slds-form-element__label" for="etape">Étape</label>
  <div class="slds-form-element__control">
    <div class="slds-select_container">
      <select class="slds-select" id="etape">
        <option>--Aucun--</option><option>Qualification</option><option>Proposition</option>
      </select>
    </div>
  </div>
</div>

<!-- Zone de texte -->
<textarea class="slds-textarea" rows="3"></textarea>

<!-- Case à cocher -->
<div class="slds-form-element">
  <div class="slds-form-element__control">
    <span class="slds-checkbox">
      <input type="checkbox" id="c1" />
      <label class="slds-checkbox__label" for="c1">
        <span class="slds-checkbox_faux"></span>
        <span class="slds-form-element__label">Facturation récurrente</span>
      </label>
    </span>
  </div>
</div>

<!-- Interrupteur -->
<label class="slds-checkbox_toggle slds-grid">
  <span class="slds-form-element__label slds-m-bottom_none">Actif</span>
  <input type="checkbox" checked />
  <span class="slds-checkbox_faux_container"><span class="slds-checkbox_faux"></span></span>
</label>

<!-- Champ en erreur -->
<div class="slds-form-element slds-has-error">
  <label class="slds-form-element__label" for="e1">Montant</label>
  <div class="slds-form-element__control"><input class="slds-input" id="e1" /></div>
  <div class="slds-form-element__help">Renseignez ce champ.</div>
</div>
```

Disposition en deux colonnes : `<div class="slds-grid slds-gutters slds-wrap">` avec des `<div class="slds-col slds-size_1-of-2">`.

## Onglets

```html
<div class="slds-tabs_default">
  <ul class="slds-tabs_default__nav" role="tablist">
    <li class="slds-tabs_default__item slds-is-active" role="presentation">
      <a class="slds-tabs_default__link" href="#" role="tab">Détails</a>
    </li>
    <li class="slds-tabs_default__item" role="presentation">
      <a class="slds-tabs_default__link" href="#" role="tab">Activité</a>
    </li>
  </ul>
  <div class="slds-tabs_default__content slds-show" role="tabpanel">Contenu actif</div>
  <div class="slds-tabs_default__content slds-hide" role="tabpanel">Contenu masqué</div>
</div>
```

Variante « scoped » (sous-onglets) : `slds-tabs_scoped`, `slds-tabs_scoped__nav`, `slds-tabs_scoped__item`, `slds-tabs_scoped__link`, `slds-tabs_scoped__content`.

## Modale

```html
<section role="dialog" tabindex="-1" class="slds-modal slds-fade-in-open slds-modal_medium" aria-modal="true">
  <div class="slds-modal__container">
    <header class="slds-modal__header">
      <button class="slds-button slds-button_icon slds-modal__close slds-button_icon-inverse" title="Fermer">
        <svg class="slds-button__icon slds-button__icon_large" aria-hidden="true"><use href="#utility-close"></use></svg>
      </button>
      <h1 class="slds-modal__title slds-hyphenate">Nouvelle opportunité</h1>
    </header>
    <div class="slds-modal__content slds-p-around_medium">Contenu</div>
    <footer class="slds-modal__footer">
      <button class="slds-button slds-button_neutral">Annuler</button>
      <button class="slds-button slds-button_brand">Enregistrer</button>
    </footer>
  </div>
</section>
<div class="slds-backdrop slds-backdrop_open"></div>
```

À placer en fin de `<body>`, hors de `.slds-scope` si besoin d'un voile plein écran.

## Toast et messages

```html
<div class="slds-notify slds-notify_toast slds-theme_success" role="status">
  <span class="slds-icon_container slds-icon-utility-success slds-m-right_small">
    <svg class="slds-icon slds-icon_small slds-icon-text-default" aria-hidden="true"><use href="#utility-success"></use></svg>
  </span>
  <div class="slds-notify__content"><h2 class="slds-text-heading_small">Opportunité enregistrée.</h2></div>
</div>
```

Thèmes : `slds-theme_success`, `slds-theme_warning`, `slds-theme_error`, `slds-theme_info`. Bandeau d'alerte : `slds-notify_alert`.

## Fil d'Ariane

```html
<nav role="navigation" aria-label="Fil d'Ariane">
  <ol class="slds-breadcrumb slds-list_horizontal slds-wrap">
    <li class="slds-breadcrumb__item"><a href="#">Opportunités</a></li>
    <li class="slds-breadcrumb__item"><a href="#">Acme - Renouvellement</a></li>
  </ol>
</nav>
```

## Chemin (path)

```html
<div class="slds-path">
  <div class="slds-grid slds-path__track">
    <div class="slds-grid slds-path__scroller-container">
      <div class="slds-path__scroller">
        <div class="slds-path__scroller_inner">
          <ul class="slds-path__nav" role="listbox">
            <li class="slds-path__item slds-is-complete" role="presentation"><a class="slds-path__link" href="#" role="option"><span class="slds-path__stage"><svg class="slds-icon slds-icon_x-small" aria-hidden="true"><use href="#utility-check"></use></svg></span><span class="slds-path__title">Qualification</span></a></li>
            <li class="slds-path__item slds-is-current slds-is-active" role="presentation"><a class="slds-path__link" href="#" role="option"><span class="slds-path__stage"><svg class="slds-icon slds-icon_x-small" aria-hidden="true"><use href="#utility-check"></use></svg></span><span class="slds-path__title">Proposition</span></a></li>
            <li class="slds-path__item slds-is-incomplete" role="presentation"><a class="slds-path__link" href="#" role="option"><span class="slds-path__stage"><svg class="slds-icon slds-icon_x-small" aria-hidden="true"><use href="#utility-check"></use></svg></span><span class="slds-path__title">Négociation</span></a></li>
            <li class="slds-path__item slds-is-incomplete" role="presentation"><a class="slds-path__link" href="#" role="option"><span class="slds-path__stage"><svg class="slds-icon slds-icon_x-small" aria-hidden="true"><use href="#utility-check"></use></svg></span><span class="slds-path__title">Clôture</span></a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="slds-grid slds-path__action">
      <button class="slds-button slds-button_brand slds-path__mark-complete">Marquer l'étape terminée</button>
    </div>
  </div>
</div>
```

## Barre de progression, avatar, vignette d'objet

```html
<div class="slds-progress-bar slds-progress-bar_medium" role="progressbar" aria-valuenow="60">
  <span class="slds-progress-bar__value" style="width:60%"></span>
</div>

<span class="slds-avatar slds-avatar_circle slds-avatar_medium">
  <img alt="" src="/assets/images/avatar1.jpg" title="Prénom Nom" />
</span>

<span class="slds-icon_container slds-icon-standard-account">
  <svg class="slds-icon slds-icon_small" aria-hidden="true"><use href="#standard-account"></use></svg>
</span>
```

Pour une icône d'objet, la classe du conteneur suit le nom : `slds-icon-standard-<objet>` (account, contact, opportunity, lead, case, task, quotes, orders, product...). Pour un objet personnalisé : `slds-icon-custom-custom<N>` avec `#custom-custom<N>`.

## Espacements et utilitaires les plus utiles

- Marges : `slds-m-top_small`, `slds-m-bottom_medium`, `slds-m-around_x-small`, `slds-m-horizontal_large`.
- Marges intérieures : `slds-p-around_medium`, `slds-p-horizontal_small`, `slds-p-vertical_x-small`.
- Tailles : `xxx-small`, `xx-small`, `x-small`, `small`, `medium`, `large`, `x-large`, `xx-large`.
- Grille : `slds-grid`, `slds-wrap`, `slds-gutters`, `slds-col`, `slds-size_1-of-3`, `slds-size_2-of-3`, `slds-grid_align-spread`, `slds-grid_vertical-align-center`.
- Texte : `slds-text-heading_large`, `slds-text-heading_medium`, `slds-text-heading_small`, `slds-text-title`, `slds-text-title_caps`, `slds-text-body_small`, `slds-text-color_weak`, `slds-text-color_error`, `slds-text-color_success`, `slds-truncate`.
- Fonds : `slds-theme_default`, `slds-theme_shade`, `slds-theme_alt-inverse`.
- Visibilité : `slds-show`, `slds-hide`, `slds-assistive-text`.
- Séparateurs : `slds-border_top`, `slds-border_bottom`, `slds-box`.
