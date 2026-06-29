# ADR-003 — BaseModule

## Statut

Proposé

## Contexte

OPG v3 possède maintenant un ModuleManager capable d'enregistrer, initialiser, démarrer et arrêter des modules.

Actuellement, le ModuleManager accepte n'importe quel objet Python, à condition que celui-ci expose éventuellement les méthodes initialize(), start() ou stop().

Cette approche fonctionne, mais elle laisse trop de liberté aux futurs modules.

## Décision

Créer une classe officielle BaseModule dans le Core.

Cette classe définira le contrat commun de tous les modules OPG.

Chaque module OPG devra hériter de BaseModule.

## Conséquences positives

- Contrat clair pour tous les modules.
- Code plus maintenable.
- Typage plus propre.
- Meilleure cohérence entre modules.
- Préparation des futurs modules catalog, render, builders, export, ui, ai.

## Conséquences négatives

- Les modules devront respecter une structure obligatoire.
- Le ModuleManager devra évoluer pour manipuler BaseModule.

## Décision finale

À valider.