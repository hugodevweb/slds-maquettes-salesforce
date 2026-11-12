# Patrons de pages Salesforce Lightning

Chaque patron se place dans `<main class="app-body">` du gabarit. Les composants internes (cartes, tableaux, formulaires...) sont décrits dans `composants.md`.

## 1. Page d'enregistrement (record page)

Structure standard, de haut en bas :

1. **En-tête de page record** (`slds-page-header slds-page-header_record-home`) : icône d'objet, type d'objet en petit, nom de l'enregistrement en titre, boutons d'action à droite, puis ligne de « points forts » (3 à 6 champs clés).
2. **Chemin** (`slds-path`) si l'objet a un cycle de vie (Opportunité, Requête, Piste).
3. **Corps en deux ou trois colonnes** (`slds-grid slds-gutters`) :
   - colonne gauche (≈ 3/12) : listes associées compactes ou carte « Détails rapides » ;
   - colonne centrale (≈ 6/12) : onglets **Détails** / **Activité** / **Chatter** ;
   - colonne droite (≈ 3/12) : composants contextuels (activités à venir, produits, contacts, composants personnalisés).

```html
<div class="slds-page-header slds-page-header_record-home">
  <div class="slds-page-header__row">
    <div class="slds-page-header__col-title">
      <div class="slds-media">
        <div class="slds-media__figure">
          <span class="slds-icon_container slds-icon-standard-opportunity">
            <svg class="slds-icon slds-page-header__icon" aria-hidden="true"><use href="#standard-opportunity"></use></svg>
          </span>
        </div>
        <div class="slds-media__body">
          <div class="slds-page-header__name">
            <div class="slds-page-header__name-title">
              <h1>
                <span>Opportunité</span>
                <span class="slds-page-header__title slds-truncate" title="Acme - Renouvellement 2027">Acme - Renouvellement 2027</span>
              </h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="slds-page-header__col-actions">
      <div class="slds-page-header__controls">
        <div class="slds-page-header__control">
          <ul class="slds-button-group-list">
            <li><button class="slds-button slds-button_neutral">Modifier</button></li>
            <li><button class="slds-button slds-button_neutral">Cloner</button></li>
            <li><button class="slds-button slds-button_neutral">Supprimer</button></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="slds-page-header__row slds-page-header__row_gutters">
    <div class="slds-page-header__col-details">
      <ul class="slds-page-header__detail-row">
        <li class="slds-page-header__detail-block">
          <div class="slds-text-title slds-truncate" title="Compte">Compte</div>
          <div class="slds-truncate"><a href="#">Acme SA</a></div>
        </li>
        <li class="slds-page-header__detail-block">
          <div class="slds-text-title slds-truncate" title="Montant">Montant</div>
          <div class="slds-truncate">48 000,00 €</div>
        </li>
        <li class="slds-page-header__detail-block">
          <div class="slds-text-title slds-truncate" title="Date de clôture">Date de clôture</div>
          <div class="slds-truncate">15/12/2026</div>
        </li>
        <li class="slds-page-header__detail-block">
          <div class="slds-text-title slds-truncate" title="Propriétaire">Propriétaire</div>
          <div class="slds-truncate"><a href="#">Camille Martin</a></div>
        </li>
      </ul>
    </div>
  </div>
</div>

<div class="slds-grid slds-gutters slds-m-top_small">
  <div class="slds-col slds-size_3-of-12"> <!-- cartes associées --> </div>
  <div class="slds-col slds-size_6-of-12">
    <div class="slds-card slds-p-around_small"> <!-- onglets Détails / Activité --> </div>
  </div>
  <div class="slds-col slds-size_3-of-12"> <!-- composants contextuels --> </div>
</div>
```

La section « Détails » reprend le formulaire en lecture : libellé (`slds-form-element__label`) au-dessus de la valeur (`slds-form-element__static`), sur deux colonnes, avec un titre de section (`slds-section__title`) pliable.

## 2. Vue liste (liste d'objets)

1. En-tête de page de liste (`slds-page-header`) : icône d'objet, nom de la vue (ex. « Toutes les opportunités ») avec chevron, compteur « 25 éléments • Triés par Date de clôture », boutons **Nouveau** / **Importer**.
2. Barre d'outils : recherche dans la liste, boutons de vue (tableau/kanban), filtres, icône d'engrenage.
3. Tableau (`slds-table slds-table_bordered slds-table_cell-buffer`) avec cases à cocher en première colonne, lien sur la première colonne, menu d'actions en dernière colonne.

## 3. Formulaire de création / modification

Modale `slds-modal_medium` intitulée « Nouveau(elle) <Objet> » :

- sections avec `slds-section` et `slds-section__title` ;
- champs sur deux colonnes (`slds-grid slds-gutters slds-wrap` + `slds-size_1-of-2`) ;
- champs obligatoires marqués d'un astérisque rouge (`abbr.slds-required`) ;
- pied avec **Annuler** (neutre), **Enregistrer et nouveau** (neutre), **Enregistrer** (brand).

## 4. Console (onglets d'enregistrements et sous-onglets)

Barre d'application console avec `slds-context-bar` et onglets (`slds-context-bar__item slds-has-flexi-truncate`), puis barre de sous-onglets (`slds-tabs_scoped`), et utilitaire de bas de page (`slds-utility-bar_container`) pour Notes, Historique, Softphone.

## 5. Page d'accueil

Grille de cartes (`slds-card`) : « Objectifs », « Activités du jour », « Opportunités à clôturer », « Éléments à approuver », graphique de performance. Mise en page `slds-grid slds-gutters slds-wrap` avec colonnes `slds-size_1-of-2`.

## 6. Assistant multi-étapes (Flow écran)

Carte centrée (`slds-card` largeur ≈ 640 px) avec indicateur de progression (`slds-progress`), titre d'étape, champs, et pied **Précédent** / **Suivant** / **Terminer**.

## 7. Composant personnalisé (nouvelle fonctionnalité)

Quand la fonctionnalité demande un composant qui n'existe pas en standard :

1. Le construire à partir de composants SLDS (carte, tableau, grille, boutons) ;
2. Ne rien ajouter qui sorte de la palette SLDS ;
3. Le repérer avec une annotation numérotée et le décrire dans la légende (voir SKILL.md) ;
4. Si du CSS spécifique est indispensable, le regrouper dans le bloc `/* NOUVEAU COMPOSANT */` du gabarit.
