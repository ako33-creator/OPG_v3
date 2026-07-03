# OPG Project Model Architecture (M-004)

Version : 1.0

Status : Draft

---

# Table of Contents

1. Introduction
2. Vision
3. Design Principles
4. Overall Architecture
...


# 1. Introduction

## 1.1 Purpose

Le **Project Model** constitue la représentation persistante et indépendante des technologies d'un projet OPG.

Il définit l'ensemble des données nécessaires pour décrire un projet de manière complète, cohérente et durable, sans dépendre d'un Runtime particulier ni d'un Driver spécifique.

Le Project Model représente la source officielle des données métier du projet. Toutes les opérations d'exécution, de synchronisation et de visualisation sont dérivées de cette représentation.

Aucune donnée Runtime ne doit être considérée comme persistante.

---

## 1.2 Scope

Cette spécification définit l'architecture complète du Project Model d'OPG v3.

Elle couvre notamment :

- les objets du domaine ;
- leur organisation hiérarchique ;
- leur identité ;
- leurs relations ;
- leur persistance ;
- leur sérialisation ;
- leur validation ;
- leur interaction avec le Runtime ;
- leur interaction avec les Drivers ;
- leur extensibilité ;
- leur évolution dans le temps.

Cette spécification ne décrit pas les algorithmes d'exécution du Runtime ni les implémentations propres aux Drivers.

---

## 1.3 Objectives

Le Project Model poursuit plusieurs objectifs fondamentaux.

### Source of Truth

Le Project Model constitue l'unique représentation persistante d'un projet.

Toutes les autres représentations sont reconstruites à partir de celui-ci.

---

### Technology Independence

Le modèle ne dépend d'aucune technologie particulière.

Il ne contient aucune référence à Blender, à une API graphique, à un moteur de rendu ou à un format de fichier spécifique.

---

### Deterministic Persistence

Deux projets identiques doivent produire une représentation persistante identique.

La sérialisation doit être déterministe afin de faciliter :

- les comparaisons ;
- les revues de code ;
- le contrôle de version ;
- les tests automatiques ;
- les outils de migration.

---

### Extensibility

Le modèle doit pouvoir évoluer sans remettre en cause les projets existants.

L'ajout de nouveaux objets ou composants ne doit pas casser les versions précédentes.

---

### Stability

Les identités des objets doivent rester stables pendant toute la durée de vie du projet.

Les références doivent rester valides indépendamment de l'organisation interne ou des opérations d'édition.

---

## 1.4 Non-Goals

Cette spécification ne décrit pas :

- l'algorithme du Runtime Scheduler ;
- le Runtime Graph ;
- le système d'événements Runtime ;
- les Drivers ;
- les interfaces utilisateur ;
- les formats propriétaires des logiciels tiers.

Ces éléments possèdent leur propre documentation architecturale.

---

## 1.5 Audience

Cette documentation s'adresse principalement à :

- Software Architects ;
- Core Developers ;
- Runtime Developers ;
- Driver Developers ;
- Plugin Developers ;
- QA Engineers ;
- Technical Writers.

Elle constitue la référence officielle pour toute évolution du Project Model.

---

## 1.6 Terminology

Les termes suivants sont utilisés dans l'ensemble de cette spécification.

| Terme | Définition |
|--------|------------|
| Project | Représentation persistante complète d'un projet OPG. |
| Project Model | Ensemble structuré des données persistantes du projet. |
| Runtime | Représentation reconstruite utilisée pour l'exécution. |
| Driver | Couche d'adaptation reliant le Runtime à une technologie externe. |
| Object | Élément persistant du Project Model. |
| Component | Ensemble de données décrivant une capacité d'un objet. |
| Asset | Ressource externe référencée par le projet. |
| Metadata | Données descriptives non fonctionnelles associées à un objet. |
| Extension | Élément ajouté par un plugin sans modifier le cœur du modèle. |

---

## 1.7 Architectural Position

L'architecture générale d'OPG repose sur une séparation stricte entre les responsabilités.

```text
                User

                  │

                  ▼

          Project Model
        (Persistent Truth)

                  │

                  ▼

         Runtime Builder

                  │

                  ▼

          Runtime Graph

                  │

                  ▼

        Runtime Execution

                  │

                  ▼

             Drivers

                  │

                  ▼

     Blender / USD / FBX / ...
```

Le Project Model ne dépend d'aucune couche située en dessous de lui.

Le Runtime est construit à partir du Project Model.

Les Drivers ne manipulent jamais directement les données persistantes. Ils interagissent exclusivement avec le Runtime, qui assure la cohérence entre l'état d'exécution et le modèle persistant.

---

## 1.8 Document Authority

Le présent document constitue la **Single Source of Truth** pour l'architecture du Project Model d'OPG v3.

Toute implémentation future de la série **M-004** devra être conforme aux règles, concepts et contraintes définis dans cette spécification.

En cas de divergence entre le code et cette documentation, la documentation fait foi jusqu'à ce qu'une révision architecturale officielle soit approuvée.


# 2. Vision

## 2.1 Overview

Le Project Model constitue le cœur fonctionnel d'OPG.

Il représente la totalité des données persistantes décrivant un projet indépendamment de toute technologie d'exécution, de tout environnement d'édition et de tout Driver.

Le Project Model est conçu pour survivre à l'évolution des moteurs d'exécution, des Drivers et des formats d'échange.

Il constitue la représentation la plus stable de l'ensemble du système.

---

## 2.2 The Persistent Truth

Le Project Model est l'unique source de vérité d'un projet.

Toutes les informations métier sont persistées exclusivement dans cette structure.

Le Runtime ne possède aucune donnée métier permanente.

Lorsqu'un Runtime est détruit, aucune information du projet ne doit être perdue.

Inversement, la reconstruction complète du Runtime doit toujours être possible à partir du seul Project Model.

Cette propriété garantit :

- la reproductibilité ;
- la stabilité ;
- la portabilité ;
- la pérennité des projets.

---

## 2.3 Separation of Responsibilities

L'architecture d'OPG repose sur une séparation stricte des responsabilités.

Chaque couche possède un rôle clairement défini.

Le Project Model décrit le projet.

Le Runtime interprète le projet.

Les Drivers synchronisent le Runtime avec les technologies externes.

Aucune couche ne doit assumer les responsabilités d'une autre.

Cette séparation réduit le couplage et facilite les évolutions futures.

---

## 2.4 Domain Before Technology

Le domaine métier constitue le centre de l'architecture.

Les technologies utilisées pour représenter ou exécuter ce domaine ne sont que des détails d'implémentation.

Le Project Model ne contient aucune dépendance vers :

- Blender ;
- Python ;
- OpenGL ;
- Vulkan ;
- DirectX ;
- USD ;
- FBX ;
- Unreal Engine ;
- Unity ;
- Godot ;
- ou toute autre technologie spécifique.

Cette indépendance garantit que le modèle restera exploitable indépendamment des technologies futures.

---

## 2.5 Blender is a Driver

Blender ne constitue pas le cœur d'OPG.

Blender est un Driver.

Son rôle consiste uniquement à :

- créer les objets Blender nécessaires ;
- appliquer les modifications provenant du Runtime ;
- synchroniser l'état du Runtime avec Blender ;
- transmettre les changements autorisés vers le Runtime.

Toute logique métier demeure exclusivement dans le Project Model et le Runtime.

---

## 2.6 Runtime as a Projection

Le Runtime est une projection temporaire du Project Model.

Il représente une structure optimisée pour l'exécution.

Le Runtime peut contenir :

- des caches ;
- des index ;
- des graphes ;
- des accélérateurs ;
- des états temporaires ;
- des ressources calculées.

Ces informations sont entièrement reconstructibles.

Elles ne doivent jamais être persistées.

---

## 2.7 Stable Identity

Chaque objet du Project Model possède une identité permanente.

Cette identité est indépendante :

- du nom de l'objet ;
- de sa position dans la hiérarchie ;
- de son propriétaire ;
- de son état Runtime ;
- de son ordre d'apparition.

Une identité ne change jamais pendant toute la durée de vie de l'objet.

Toutes les références utilisent exclusivement cette identité.

---

## 2.8 Composition Over Inheritance

Le Project Model privilégie la composition à l'héritage.

Les capacités d'un objet sont décrites par des composants spécialisés plutôt que par une hiérarchie profonde de classes.

Cette approche favorise :

- la modularité ;
- la réutilisation ;
- l'extensibilité ;
- les plugins ;
- la maintenance.

---

## 2.9 Explicit Relationships

Toutes les relations entre objets doivent être représentées explicitement.

Aucune relation ne doit être déduite :

- d'un nom ;
- d'un chemin ;
- d'une convention implicite ;
- d'un ordre dans une collection.

Chaque relation possède une représentation persistante clairement identifiée.

---

## 2.10 Deterministic Projects

Deux projets contenant exactement les mêmes données doivent produire exactement la même représentation persistante.

Cette propriété est indispensable pour :

- Git ;
- les revues de code ;
- les comparaisons automatiques ;
- les signatures numériques ;
- les tests automatisés ;
- les pipelines CI/CD.

La sérialisation devra donc être entièrement déterministe.

---

## 2.11 Long-Term Compatibility

Le Project Model est conçu pour évoluer pendant de nombreuses années.

L'ajout de nouvelles fonctionnalités ne doit pas invalider les projets existants.

Chaque évolution devra préserver :

- la compatibilité ascendante lorsque cela est possible ;
- une stratégie de migration documentée lorsque cela est nécessaire ;
- la stabilité des identités persistantes.

---

## 2.12 Architectural Vision

La philosophie générale d'OPG peut être résumée par le flux suivant.

```text
                 Project Model
              (Persistent Truth)

                       │

                       ▼

               Runtime Builder

                       │

                       ▼

                Runtime Graph

                       │

                       ▼

              Runtime Execution

                       │

                       ▼

                   Drivers

                       │

                       ▼

      Blender / USD / FBX / Future Drivers
```

Le Project Model est l'origine de toute information.

Le Runtime est une représentation optimisée.

Les Drivers sont des adaptateurs technologiques.

Aucune couche inférieure ne peut modifier directement les règles métier définies par le Project Model.


# 3. Design Principles

## 3.1 Overview

Les principes décrits dans ce chapitre constituent les règles fondamentales de conception du Project Model.

Ils sont indépendants des choix d'implémentation et demeurent applicables quelles que soient les technologies utilisées.

Toute évolution du Project Model devra respecter ces principes.

---

## 3.2 Architecture Before Implementation

Aucune implémentation ne doit précéder la définition complète de son architecture.

Chaque fonctionnalité doit être spécifiée avant d'être développée.

Les décisions architecturales précèdent systématiquement l'écriture du code.

Cette approche garantit :

- la cohérence globale ;
- la stabilité du système ;
- la réduction des refactorings ;
- une meilleure maintenabilité.

---

## 3.3 Specification Driven Engineering

La documentation constitue la référence officielle du projet.

Le code implémente la spécification.

Il ne la définit pas.

Chaque évolution du système suit le cycle suivant :

1. Rédaction de la spécification.
2. Validation architecturale.
3. Implémentation.
4. Tests.
5. Documentation de maintenance.

---

## 3.4 Single Source of Truth

Le Project Model représente l'unique vérité persistante du projet.

Aucune duplication des données métier ne doit exister dans :

- le Runtime ;
- les Drivers ;
- les interfaces utilisateur ;
- les caches.

Toutes les représentations dérivées sont reconstruites à partir du Project Model.

---

## 3.5 Technology Independence

Le domaine métier ne dépend d'aucune technologie.

Le Project Model ne possède aucune dépendance vers :

- Blender ;
- Python ;
- une API graphique ;
- un moteur de rendu ;
- un format d'échange.

Cette indépendance garantit la pérennité du modèle.

---

## 3.6 Stable Identity

Chaque objet possède une identité permanente.

Cette identité :

- ne change jamais ;
- ne dépend pas du nom ;
- ne dépend pas de la hiérarchie ;
- ne dépend pas du Runtime.

Toutes les références utilisent cette identité.

---

## 3.7 Explicit Ownership

Chaque objet appartient explicitement à un propriétaire.

Aucun objet ne peut appartenir implicitement à plusieurs propriétaires.

Les responsabilités sont toujours clairement définies.

---

## 3.8 Explicit Relationships

Toutes les relations sont persistées explicitement.

Aucune relation ne peut être reconstruite à partir :

- d'un nom ;
- d'un chemin ;
- d'une convention implicite.

Chaque relation possède une représentation persistante.

---

## 3.9 Composition Over Inheritance

Le comportement est construit par composition.

Les composants décrivent les capacités d'un objet.

L'héritage est limité aux abstractions fondamentales du modèle.

Cette approche favorise :

- la modularité ;
- l'extensibilité ;
- les plugins ;
- la maintenance.

---

## 3.10 Deterministic Serialization

Deux projets identiques doivent produire exactement la même sérialisation.

L'ordre des objets, des propriétés et des collections doit être déterministe.

Cette propriété facilite :

- Git ;
- les revues de code ;
- les tests automatisés ;
- les signatures numériques.

---

## 3.11 Forward Compatibility

Le Project Model doit pouvoir évoluer sans rendre les anciens projets inutilisables.

Les nouvelles versions doivent :

- préserver les données existantes ;
- documenter les migrations ;
- maintenir les identités persistantes.

---

## 3.12 Validation by Construction

Le modèle doit empêcher autant que possible la création d'états invalides.

Les règles métier sont appliquées dès la construction des objets.

La validation ne constitue pas une correction.

Elle vérifie qu'un modèle déjà construit respecte les contraintes définies par la spécification.

---

## 3.13 Extensibility

Le Project Model doit être extensible.

Les plugins doivent pouvoir ajouter :

- de nouveaux composants ;
- de nouveaux types d'objets ;
- des métadonnées ;
- des validateurs ;
- des extensions de sérialisation.

Sans modifier le cœur du système.

---

## 3.14 Separation of Concerns

Chaque couche possède une responsabilité unique.

Le Project Model décrit.

Le Runtime exécute.

Les Drivers synchronisent.

Les interfaces utilisateur présentent les données.

Aucune couche ne doit assumer les responsabilités d'une autre.

---

## 3.15 Predictability

Le comportement du système doit rester prévisible.

Une même opération appliquée au même Project Model doit toujours produire le même résultat.

Cette propriété garantit :

- la reproductibilité ;
- la stabilité ;
- la facilité de débogage ;
- la confiance des utilisateurs.

---

## 3.16 Summary

Les principes présentés dans ce chapitre constituent les fondations architecturales du Project Model.

Toutes les décisions futures relatives aux objets, aux composants, à la sérialisation, au Runtime, aux Drivers et aux extensions devront être compatibles avec ces principes.

Aucune exception ne pourra être introduite sans révision officielle de cette spécification.


# 4. Overall Architecture

## 4.1 Overview

Le Project Model constitue le cœur persistant d'OPG.

Il représente l'ensemble des données métier nécessaires pour décrire un projet de manière complète, indépendante des technologies et durable dans le temps.

Toutes les autres couches de l'architecture sont construites à partir de cette représentation.

Le Project Model ne dépend d'aucune couche située en dessous de lui.

---

## 4.2 Architectural Layers

L'architecture générale d'OPG est organisée en couches ayant chacune une responsabilité unique.

```text
                User

                  │

                  ▼

          Project Model
        (Persistent Truth)

                  │

                  ▼

         Runtime Builder

                  │

                  ▼

          Runtime Graph

                  │

                  ▼

        Runtime Execution

                  │

                  ▼

             Drivers

                  │

                  ▼

 Blender / USD / FBX / Future Drivers
```

Chaque couche ne connaît que la couche immédiatement supérieure ou inférieure selon sa responsabilité.

Les dépendances inverses sont interdites.

---

## 4.3 Layer Responsibilities

### Project Model

Le Project Model est responsable de :

- la persistance ;
- la structure métier ;
- les identités ;
- les relations ;
- les composants ;
- les métadonnées ;
- les références d'assets.

Il ne contient aucune logique d'exécution.

---

### Runtime Builder

Le Runtime Builder transforme le Project Model en Runtime.

Il construit :

- les graphes Runtime ;
- les index ;
- les caches ;
- les services Runtime ;
- les dépendances d'exécution.

Aucune donnée persistante n'est créée dans cette étape.

---

### Runtime Graph

Le Runtime Graph représente l'organisation interne du Runtime.

Il optimise l'accès aux objets et aux services pendant l'exécution.

Il est entièrement reconstructible.

---

### Runtime Execution

Le Runtime exécute les comportements décrits par le Project Model.

Il gère notamment :

- les systèmes ;
- les événements ;
- les services ;
- les plugins Runtime ;
- les traitements temporaires.

---

### Drivers

Les Drivers assurent uniquement la synchronisation entre le Runtime et les technologies externes.

Ils ne possèdent aucune logique métier.

Ils ne modifient jamais directement le Project Model.

---

## 4.4 Data Flow

Le flux de données est strictement unidirectionnel.

```text
Project Model

        │

        ▼

Runtime Builder

        │

        ▼

Runtime

        │

        ▼

Drivers

        │

        ▼

External Technologies
```

Lorsqu'une modification provient d'un Driver, elle suit le chemin inverse via les mécanismes de synchronisation contrôlés par le Runtime.

Le Driver ne peut jamais modifier directement le Project Model.

---

## 4.5 Internal Structure of the Project Model

Le Project Model est composé de plusieurs sous-systèmes spécialisés.

```text
Project

│

├── Objects

├── Components

├── Metadata

├── Assets

├── References

├── Extensions

├── Validation

├── Transactions

└── Serialization
```

Chaque sous-système possède une responsabilité clairement définie.

Les interactions entre ces sous-systèmes sont explicites.

---

## 4.6 Project Lifecycle

Le cycle de vie général d'un projet est le suivant :

```text
Create Project

        │

        ▼

Load Project

        │

        ▼

Validate

        │

        ▼

Build Runtime

        │

        ▼

Execute

        │

        ▼

Synchronize

        │

        ▼

Save Project
```

À aucun moment le Runtime ne devient la source officielle des données.

Le Project Model demeure la seule représentation persistante.

---

## 4.7 Dependency Rules

Les règles suivantes sont obligatoires.

Le Project Model :

- ne dépend pas du Runtime ;
- ne dépend pas des Drivers ;
- ne dépend pas de Blender ;
- ne dépend pas des interfaces utilisateur.

Le Runtime :

- dépend du Project Model ;
- ne modifie jamais directement les données persistantes.

Les Drivers :

- dépendent du Runtime ;
- ne possèdent aucune logique métier.

Les interfaces utilisateur :

- dépendent des services applicatifs ;
- ne manipulent jamais directement les structures internes du Project Model.

---

## 4.8 Future Evolution

L'architecture doit permettre l'ajout futur de nouveaux éléments sans remise en cause des fondations.

Par exemple :

- nouveaux Drivers ;
- nouveaux composants ;
- nouveaux types d'objets ;
- nouveaux formats de sérialisation ;
- nouveaux systèmes Runtime ;
- nouvelles extensions de validation.

Ces évolutions doivent préserver la stabilité du Project Model.

---

## 4.9 Architectural Principles Recap

L'architecture générale repose sur quelques principes fondamentaux :

- un seul modèle persistant ;
- un Runtime entièrement reconstructible ;
- des Drivers interchangeables ;
- une indépendance totale vis-à-vis des technologies ;
- une séparation stricte des responsabilités ;
- une architecture extensible ;
- une sérialisation déterministe ;
- une évolution contrôlée.

---

## 4.10 Conclusion

Le Project Model constitue la fondation de toute l'architecture OPG.

Les chapitres suivants détailleront progressivement chacun de ses sous-systèmes internes :

- Domain Model ;
- Object Hierarchy ;
- Identity ;
- Relationships ;
- Components ;
- Metadata ;
- Asset References ;
- Serialization ;
- Validation ;
- Transactions ;
- Runtime Integration ;
- Driver Integration ;
- Extension System.


# 5. Domain Model

## 5.1 Overview

Le Domain Model décrit l'ensemble des concepts métier persistants constituant un projet OPG.

Il représente la structure logique du Project Model sans référence à une implémentation particulière.

Le Domain Model est indépendant :

- du Runtime ;
- des Drivers ;
- des interfaces utilisateur ;
- des technologies utilisées pour la persistance.

Il constitue le langage commun utilisé par toutes les couches du système.

---

## 5.2 Objectives

Le Domain Model poursuit plusieurs objectifs :

- représenter fidèlement un projet OPG ;
- garantir la cohérence des données ;
- permettre la reconstruction complète du Runtime ;
- assurer la stabilité des identités ;
- faciliter l'évolution du système.

Le Domain Model ne contient aucune logique spécifique aux technologies d'exécution.

---

## 5.3 Root Entity

Chaque projet possède une unique racine.

Cette racine est représentée par l'entité **Project**.

Le Project constitue le point d'entrée de toutes les données persistantes.

Tous les objets du domaine appartiennent directement ou indirectement à cette racine.

Il ne peut exister qu'un seul Project par fichier de projet.

---

## 5.4 Domain Entities

Le Domain Model est composé des entités suivantes.

### Project

Représente le projet complet.

Responsabilités :

- stocker les informations globales ;
- contenir les objets persistants ;
- gérer la version du projet ;
- référencer les assets ;
- gérer les extensions.

---

### Object

Un Object représente une entité persistante appartenant au projet.

Chaque Object :

- possède une identité stable ;
- peut posséder des composants ;
- peut appartenir à une hiérarchie ;
- peut référencer d'autres objets.

Les Objects constituent les briques fondamentales du Project Model.

---

### Component

Un Component décrit une capacité d'un Object.

Il ne possède pas d'identité indépendante.

Son cycle de vie dépend entièrement de l'objet auquel il appartient.

Un Object peut posséder plusieurs Components.

---

### Asset

Un Asset représente une ressource externe.

Exemples :

- mesh ;
- matériau ;
- texture ;
- image ;
- animation ;
- script ;
- audio ;
- vidéo.

Les Assets ne sont jamais copiés dans les Objects.

Les Objects ne possèdent que des références vers les Assets.

---

### Metadata

Les Metadata décrivent des informations complémentaires.

Elles n'ont aucun impact direct sur le comportement métier.

Exemples :

- auteur ;
- description ;
- tags ;
- catégorie ;
- notes.

---

### Extension

Une Extension représente des données ajoutées par un plugin.

Le cœur du Project Model n'a pas besoin de connaître leur contenu.

Chaque Extension est isolée dans son propre espace de données.

---

## 5.5 Aggregate Structure

Le Domain Model est organisé autour du Project.

```text
Project

│

├── Objects

│     ├── Components

│     ├── Metadata

│     └── References

│

├── Assets

│

├── Extensions

│

└── Project Metadata
```

Le Project constitue l'Aggregate Root principal.

Toutes les modifications transitent par cette racine.

---

## 5.6 Object Responsibilities

Chaque Object est responsable :

- de son identité ;
- de son état persistant ;
- de ses composants ;
- de ses relations ;
- de ses métadonnées.

Un Object n'est jamais responsable :

- du Runtime ;
- des Drivers ;
- de la sérialisation ;
- des caches ;
- des index.

---

## 5.7 Component Responsibilities

Les Components sont responsables uniquement des données spécialisées.

Ils ne possèdent :

- ni hiérarchie ;
- ni identité propre ;
- ni cycle de vie indépendant.

Ils sont entièrement contenus dans leur Object propriétaire.

---

## 5.8 Asset Responsibilities

Les Assets représentent uniquement des ressources.

Ils ne décrivent pas la logique métier.

Ils peuvent être :

- internes ;
- externes ;
- virtuels ;
- générés.

Le système d'Assets sera détaillé dans un chapitre dédié.

---

## 5.9 Domain Invariants

Les invariants suivants sont obligatoires.

Chaque Object :

- possède exactement un identifiant ;
- possède exactement un propriétaire ;
- appartient à un seul Project.

Chaque Component :

- appartient à un seul Object.

Chaque Asset :

- est référencé sans être dupliqué.

Ces règles ne peuvent jamais être violées.

---

## 5.10 Domain Independence

Le Domain Model ne connaît pas :

- Blender ;
- Python ;
- le Runtime ;
- les Drivers ;
- les APIs graphiques ;
- les formats de fichiers externes.

Il représente uniquement le domaine métier.

---

## 5.11 UML Overview

Le modèle conceptuel peut être résumé ainsi.

```text
                    Project

                       │

        ┌──────────────┼──────────────┐

        ▼              ▼              ▼

     Objects        Assets      Extensions

        │

        ▼

    Components

        │

        ▼

     Metadata
```

Cette représentation sera affinée dans les chapitres suivants consacrés aux hiérarchies, aux identités et aux relations.

---

## 5.12 Conclusion

Le Domain Model constitue le socle conceptuel du Project Model.

Les chapitres suivants détailleront chacun des éléments présentés ici afin de définir précisément :

- la hiérarchie des objets ;
- le système d'identité ;
- les relations ;
- les composants ;
- les métadonnées ;
- les références d'assets ;
- les mécanismes de persistance.


# 6. Object Hierarchy

## 6.1 Overview

La hiérarchie des objets constitue la structure organisationnelle du Project Model.

Elle permet d'exprimer les relations de propriété, d'organisation et de cycle de vie entre les différents objets persistants.

Cette hiérarchie est indépendante du Runtime et ne reflète pas nécessairement la structure d'exécution.

---

## 6.2 Hierarchical Model

Le Project Model adopte une hiérarchie arborescente.

Chaque objet appartient à un unique parent.

L'ensemble des objets forme un arbre dont la racine est le Project.

Cette structure garantit :

- une navigation déterministe ;
- une propriété explicite ;
- un cycle de vie cohérent ;
- une persistance simplifiée.

---

## 6.3 Root Object

Le Project constitue l'unique racine de la hiérarchie.

Aucun autre objet ne peut exister en dehors d'un Project.

Tous les objets sont accessibles directement ou indirectement depuis cette racine.

```text
Project
    │
    ├── Object
    │     ├── Object
    │     └── Object
    │
    └── Object
```

---

## 6.4 Parent Ownership

Chaque objet possède exactement un parent.

Cette relation est obligatoire.

Un objet ne peut jamais appartenir simultanément à plusieurs parents.

Le changement de parent constitue une opération explicite du Project Model.

---

## 6.5 Children Collection

Chaque objet peut posséder zéro, un ou plusieurs enfants.

Les enfants sont conservés dans une collection ordonnée.

L'ordre des enfants est persistant.

Toute modification de cet ordre constitue une modification du projet.

---

## 6.6 Ownership Rules

Le propriétaire d'un objet est responsable de :

- son cycle de vie ;
- sa persistance ;
- son intégration dans la hiérarchie.

La suppression d'un propriétaire entraîne la suppression de tous ses descendants, sauf si une stratégie de transfert est explicitement définie.

---

## 6.7 Hierarchy Integrity

La hiérarchie doit toujours respecter les contraintes suivantes :

- un seul parent par objet ;
- aucune racine secondaire ;
- aucun objet orphelin ;
- aucun cycle.

Ces règles sont vérifiées lors de la validation du Project Model.

---

## 6.8 Cyclic Dependencies

Les cycles hiérarchiques sont strictement interdits.

Par exemple :

```text
A
└── B
     └── C
          └── A
```

Cette structure est invalide.

La hiérarchie doit toujours former un arbre acyclique.

---

## 6.9 Hierarchy vs References

La hiérarchie représente la propriété.

Les références représentent les relations fonctionnelles.

Un objet peut référencer n'importe quel autre objet sans modifier la hiérarchie.

Exemple :

```text
Hierarchy

Project
 ├── Camera
 └── Character


References

Character
      │
      ▼
Camera
```

Les références seront décrites dans un chapitre dédié.

---

## 6.10 Traversal

Le Project Model doit permettre plusieurs modes de parcours.

Les principaux parcours sont :

- profondeur (Depth First Search) ;
- largeur (Breadth First Search) ;
- parcours direct des enfants ;
- parcours des ancêtres.

Le choix de l'algorithme dépend du contexte d'utilisation.

---

## 6.11 Object Lifetime

La durée de vie d'un objet dépend de son propriétaire.

Un objet est créé par son parent.

Il est détruit lorsque son parent le retire définitivement de la hiérarchie.

Aucun objet ne peut survivre indépendamment de son Project.

---

## 6.12 Reparenting

Le déplacement d'un objet dans la hiérarchie est appelé **Reparenting**.

Cette opération doit :

- préserver l'identité de l'objet ;
- préserver les identités des descendants ;
- préserver les références existantes ;
- mettre à jour les relations de propriété.

Le Reparenting ne modifie jamais l'identifiant d'un objet.

---

## 6.13 Ordering

L'ordre des enfants est significatif.

Deux projets identiques doivent conserver exactement le même ordre.

Cet ordre participe à la sérialisation déterministe.

Les opérations suivantes modifient l'ordre :

- insertion ;
- déplacement ;
- suppression ;
- tri explicite.

---

## 6.14 Hierarchy Validation

La validation de la hiérarchie vérifie notamment :

- l'existence d'une unique racine ;
- l'absence de cycles ;
- l'absence d'objets orphelins ;
- la cohérence des parents ;
- la cohérence des collections d'enfants.

Toute violation rend le Project Model invalide.

---

## 6.15 UML Overview

La hiérarchie peut être représentée de la manière suivante.

```text
Project
    │
    ├──────────────┐
    │              │
    ▼              ▼

Object A      Object B

    │
    ├───────────┐
    │           │
    ▼           ▼

Object C   Object D
```

Cette hiérarchie représente uniquement les relations de propriété.

Les relations fonctionnelles sont définies indépendamment.

---

## 6.16 Summary

La hiérarchie des objets constitue la colonne vertébrale du Project Model.

Elle garantit :

- une organisation cohérente ;
- une propriété explicite ;
- un cycle de vie maîtrisé ;
- une navigation déterministe ;
- une base solide pour les mécanismes de persistance, de validation et de sérialisation.

Les chapitres suivants introduiront le système d'identité persistante, qui permettra de référencer les objets indépendamment de leur position dans cette hiérarchie.


# 7. Identity System

## 7.1 Overview

L'identité constitue le mécanisme fondamental permettant de distinguer chaque objet du Project Model.

Contrairement au nom, à la position hiérarchique ou aux métadonnées, l'identité représente la nature permanente d'un objet.

Elle permet de garantir la stabilité des références, la cohérence de la sérialisation et la reconstruction fidèle du Runtime.

Chaque objet persistant possède exactement une identité.

---

## 7.2 Objectives

Le système d'identité poursuit les objectifs suivants :

- identifier chaque objet de manière unique ;
- maintenir cette identité pendant toute la durée de vie de l'objet ;
- permettre les références entre objets ;
- garantir la stabilité lors des opérations de déplacement ;
- assurer la compatibilité entre versions ;
- simplifier les mécanismes de synchronisation.

---

## 7.3 Identity Principles

L'identité d'un objet respecte les principes suivants :

- unicité ;
- permanence ;
- indépendance ;
- immutabilité ;
- non-signification.

Une identité ne transporte aucune information métier.

Elle sert uniquement à identifier un objet.

---

## 7.4 Global Uniqueness

Chaque objet du Project Model possède un identifiant unique à l'intérieur du projet.

Deux objets ne peuvent jamais partager la même identité.

Cette règle est vérifiée lors de la validation du projet.

---

## 7.5 Identity Lifetime

Une identité est créée en même temps que l'objet.

Elle n'est jamais modifiée.

Elle disparaît uniquement lorsque l'objet est définitivement supprimé du projet.

Une identité supprimée ne doit jamais être réutilisée.

---

## 7.6 Identity Independence

L'identité est totalement indépendante :

- du nom de l'objet ;
- de son type ;
- de sa position dans la hiérarchie ;
- de son propriétaire ;
- de son ordre dans une collection ;
- de son état Runtime.

Toutes ces propriétés peuvent évoluer sans modifier l'identité.

---

## 7.7 UUID

L'identifiant persistant d'un objet est représenté par un UUID.

Le format exact sera défini lors de l'implémentation.

Les exigences sont les suivantes :

- unicité ;
- stabilité ;
- génération automatique ;
- absence de signification métier.

Le Project Model ne dépend d'aucun fournisseur particulier de UUID.

---

## 7.8 Human Readable Names

Le nom d'un objet ne constitue jamais son identité.

Plusieurs objets peuvent partager le même nom.

Le renommage d'un objet ne modifie aucune référence.

Toutes les relations utilisent exclusivement l'identité persistante.

---

## 7.9 References

Toutes les références entre objets utilisent l'identité persistante.

Aucune référence ne doit être construite à partir :

- d'un nom ;
- d'un chemin hiérarchique ;
- d'un index ;
- d'une position dans une collection.

Cette règle garantit la stabilité des références lors des opérations d'édition.

---

## 7.10 Reparenting

Lorsqu'un objet est déplacé dans la hiérarchie :

- son identité reste inchangée ;
- les identités de ses descendants restent inchangées ;
- toutes les références restent valides.

Le déplacement ne modifie jamais les identifiants.

---

## 7.11 Duplication

La duplication d'un objet crée une nouvelle identité.

Les données métier peuvent être copiées.

L'identité ne doit jamais être copiée.

Chaque nouvel objet reçoit un nouvel identifiant.

---

## 7.12 Import

Lors de l'import d'un projet externe :

- les identités existantes sont conservées lorsque cela est possible ;
- les conflits sont résolus de manière déterministe ;
- aucune collision d'identité n'est autorisée.

La stratégie exacte de résolution sera définie dans le chapitre consacré à l'importation.

---

## 7.13 Serialization

Les identités sont persistées avec les objets.

Elles participent directement à la sérialisation.

La lecture puis la réécriture d'un projet ne doit jamais modifier les identifiants.

---

## 7.14 Runtime Mapping

Le Runtime ne crée pas de nouvelles identités métier.

Chaque objet Runtime conserve un lien direct vers l'identité persistante de son objet d'origine.

Cette correspondance permet :

- la synchronisation ;
- les mises à jour ;
- la reconstruction du Runtime.

---

## 7.15 Validation

La validation du système d'identité vérifie notamment :

- l'unicité des identifiants ;
- l'absence d'identifiant vide ;
- l'absence de duplication ;
- la cohérence des références ;
- la stabilité des correspondances.

Toute violation rend le Project Model invalide.

---

## 7.16 UML Overview

Le système d'identité peut être représenté ainsi.

```text
Project

   │

   ├──────────────┐

   ▼              ▼

Object A      Object B

UUID A        UUID B

   │              │

   └──────┐   ┌───┘
          ▼   ▼

      References
```

Toutes les références utilisent les UUID.

La hiérarchie demeure indépendante de ce mécanisme.

---

## 7.17 Summary

Le système d'identité constitue le fondement de l'ensemble du Project Model.

Il garantit :

- l'identification permanente des objets ;
- la stabilité des références ;
- la cohérence des opérations d'édition ;
- une sérialisation fiable ;
- une reconstruction déterministe du Runtime.

Les chapitres suivants s'appuieront sur ce mécanisme pour définir les relations entre objets et le système de composants.


# 8. Relationships

## 8.1 Overview

Les relations permettent aux objets du Project Model d'interagir entre eux sans modifier leur hiérarchie.

Alors que la hiérarchie décrit la propriété et le cycle de vie des objets, les relations décrivent leurs dépendances fonctionnelles.

Les relations constituent un mécanisme fondamental de modélisation du domaine.

Elles sont persistantes, explicites et indépendantes du Runtime.

---

## 8.2 Objectives

Le système de relations poursuit les objectifs suivants :

- représenter les liens métier entre objets ;
- maintenir une séparation claire entre propriété et dépendance ;
- préserver la stabilité des références ;
- permettre la reconstruction du Runtime ;
- faciliter la validation du modèle.

---

## 8.3 Ownership vs Relationship

Deux notions doivent toujours être distinguées.

### Ownership

L'ownership définit :

- le propriétaire ;
- le cycle de vie ;
- la hiérarchie.

### Relationship

Une relation définit :

- une dépendance métier ;
- une association logique ;
- un lien fonctionnel.

Une relation ne modifie jamais la hiérarchie.

---

## 8.4 Explicit Relationships

Toutes les relations doivent être explicitement représentées dans le Project Model.

Aucune relation ne peut être déduite :

- d'un nom ;
- d'un chemin ;
- d'une convention implicite ;
- d'un ordre hiérarchique.

Chaque relation est persistée.

---

## 8.5 Reference by Identity

Les relations utilisent exclusivement les identités persistantes.

Une relation ne référence jamais :

- un nom ;
- une position ;
- un index ;
- un chemin.

Les UUID constituent l'unique mécanisme de référence.

---

## 8.6 Relationship Cardinality

Le système doit permettre plusieurs formes de cardinalité.

### One-to-One

Un objet référence exactement un autre objet.

Exemple :

```text
Camera
    │
    ▼
Lens
```

---

### One-to-Many

Un objet référence plusieurs objets.

```text
Scene

 ├── Camera

 ├── Light

 └── Character
```

---

### Many-to-Many

Plusieurs objets peuvent partager plusieurs références.

```text
Material

▲      ▲

│      │

Mesh A Mesh B
```

La cardinalité exacte dépend du type de relation.

---

## 8.7 Direction

Une relation possède toujours une direction.

```text
Object A

    │

    ▼

Object B
```

Le sens de la relation est explicite.

Les relations bidirectionnelles sont représentées par deux relations distinctes.

---

## 8.8 Optional Relationships

Certaines relations sont obligatoires.

D'autres sont optionnelles.

Cette contrainte est définie par chaque type de relation.

La validation vérifie leur présence lorsque cela est nécessaire.

---

## 8.9 Relationship Lifetime

Une relation possède son propre cycle de vie.

Elle peut être :

- créée ;
- supprimée ;
- remplacée.

La suppression d'une relation ne supprime jamais automatiquement les objets concernés.

---

## 8.10 Dangling References

Une relation ne peut jamais pointer vers un objet inexistant.

Les références orphelines sont interdites.

Lorsqu'un objet est supprimé, toutes les relations concernées doivent être mises à jour ou supprimées.

---

## 8.11 Cyclic Relationships

Contrairement à la hiérarchie, certaines relations fonctionnelles peuvent former des cycles.

Exemple :

```text
A ───► B

▲       │

│       ▼

└────── C
```

Ces cycles sont autorisés uniquement lorsqu'ils ont une signification métier clairement définie.

Ils ne doivent jamais compromettre les algorithmes de validation ou de reconstruction.

---

## 8.12 Runtime Independence

Les relations décrivent uniquement le domaine.

Elles ne représentent pas :

- les dépendances Runtime ;
- les graphes d'exécution ;
- les événements ;
- les services.

Le Runtime construit ses propres graphes à partir de ces relations.

---

## 8.13 Serialization

Les relations sont persistées avec les objets.

La sérialisation doit préserver :

- leur direction ;
- leur cardinalité ;
- leurs identités ;
- leur ordre lorsque celui-ci est significatif.

La lecture puis la réécriture d'un projet ne doit modifier aucune relation.

---

## 8.14 Validation

Le système de validation vérifie notamment :

- la validité des identifiants référencés ;
- l'existence des objets ciblés ;
- la cardinalité ;
- les contraintes métier ;
- l'absence de références interdites.

Toute violation rend le Project Model invalide.

---

## 8.15 UML Overview

Le modèle conceptuel des relations peut être résumé ainsi.

```text
                 Project

                    │

        ┌───────────┼───────────┐

        ▼                       ▼

     Object A             Object B

        │                     ▲

        └──────────────►──────┘

             Relationship
```

La hiérarchie reste indépendante des relations.

Les deux systèmes sont complémentaires.

---

## 8.16 Design Principles

Le système de relations repose sur les principes suivants :

- relations explicites ;
- références par identité ;
- indépendance vis-à-vis de la hiérarchie ;
- stabilité des références ;
- validation systématique ;
- sérialisation déterministe.

Ces principes garantissent une architecture robuste et évolutive.

---

## 8.17 Summary

Les relations permettent d'exprimer les interactions métier entre objets sans compromettre la structure hiérarchique du Project Model.

Associées au système d'identité, elles constituent le socle des futurs mécanismes de composants, de dépendances, de validation et de reconstruction du Runtime.


# 9. Component Model

## 9.1 Overview

Le Component Model constitue le mécanisme principal de composition des objets du Project Model.

Plutôt que d'utiliser de profondes hiérarchies d'héritage, les objets sont construits par l'assemblage de composants spécialisés.

Chaque composant encapsule un ensemble cohérent de données métier représentant une capacité précise.

Cette approche garantit un modèle modulaire, extensible et indépendant des technologies.

---

## 9.2 Objectives

Le Component Model poursuit les objectifs suivants :

- favoriser la composition plutôt que l'héritage ;
- isoler les responsabilités ;
- simplifier l'évolution des objets ;
- permettre l'extensibilité par plugins ;
- réduire le couplage entre les différentes parties du modèle.

---

## 9.3 Definition

Un Component représente un ensemble cohérent de données appartenant exclusivement à un Object.

Un Component :

- ne possède pas d'identité propre ;
- ne possède pas de cycle de vie indépendant ;
- n'existe jamais en dehors de son propriétaire.

Il constitue une partie intégrante de l'objet auquel il appartient.

---

## 9.4 Ownership

Chaque Component appartient exactement à un seul Object.

Cette relation est obligatoire.

Un Component ne peut jamais être partagé entre plusieurs objets.

La suppression de l'objet entraîne automatiquement la suppression de tous ses Components.

---

## 9.5 Composition

Un Object peut posséder plusieurs Components.

Exemple :

```text
ProjectObject

│

├── TransformComponent

├── RenderComponent

├── PhysicsComponent

└── MetadataComponent
```

La combinaison de ces composants définit entièrement les capacités de l'objet.

---

## 9.6 Single Responsibility

Chaque Component possède une responsabilité unique.

Un Component ne doit jamais regrouper plusieurs responsabilités indépendantes.

Par exemple :

✔ TransformComponent

✔ MaterialComponent

✔ AnimationComponent

✘ SceneAndAnimationComponent

Cette règle facilite la maintenance et l'extensibilité.

---

## 9.7 Component Independence

Les Components sont conçus pour être faiblement couplés.

Ils communiquent uniquement via leur Object propriétaire ou par des mécanismes explicitement définis.

Un Component ne doit jamais modifier directement un autre Component sans passer par les règles du Project Model.

---

## 9.8 Built-in Components

Le cœur d'OPG définit un ensemble de Components standards.

Exemples :

- TransformComponent
- VisibilityComponent
- MaterialComponent
- MetadataComponent
- AssetReferenceComponent
- AnimationComponent

Cette liste pourra évoluer sans modifier l'architecture générale.

---

## 9.9 Custom Components

Les plugins peuvent introduire leurs propres Components.

Chaque Component personnalisé :

- possède un identifiant unique ;
- respecte les règles de sérialisation ;
- participe à la validation ;
- demeure isolé du cœur du système.

Le noyau du Project Model n'a pas besoin de connaître leur implémentation.

---

## 9.10 Component Registration

Tous les types de Components sont enregistrés dans un registre central.

Ce registre permet notamment :

- la création dynamique ;
- la sérialisation ;
- la désérialisation ;
- la validation ;
- l'extension par plugins.

Le mécanisme de registre sera spécifié dans un chapitre dédié.

---

## 9.11 Component Constraints

Chaque type de Component peut définir ses propres contraintes.

Exemples :

- nombre maximal d'instances ;
- dépendances obligatoires ;
- incompatibilités ;
- valeurs autorisées.

Ces contraintes sont vérifiées lors de la validation du Project Model.

---

## 9.12 Runtime Interaction

Les Components décrivent uniquement des données persistantes.

Ils ne contiennent :

- aucune logique Runtime ;
- aucun cache ;
- aucun état temporaire ;
- aucune dépendance vers un Driver.

Le Runtime interprète ces données pour construire ses propres structures.

---

## 9.13 Serialization

Chaque Component est sérialisé avec son Object propriétaire.

La sérialisation doit préserver :

- le type du Component ;
- ses données ;
- son ordre lorsque celui-ci est significatif.

Deux sérialisations successives d'un même projet doivent produire exactement le même résultat.

---

## 9.14 Validation

Chaque Component participe au processus de validation.

La validation vérifie notamment :

- la cohérence interne ;
- les contraintes métier ;
- les dépendances ;
- les incompatibilités ;
- l'intégrité des données.

Un Component invalide rend son Object invalide.

---

## 9.15 UML Overview

Le modèle conceptuel peut être représenté ainsi.

```text
                 ProjectObject

                        │

        ┌───────────────┼───────────────┐

        ▼               ▼               ▼

 Transform      Material       Metadata

 Component      Component      Component
```

Les Components ne possèdent pas de hiérarchie.

Ils sont contenus dans leur Object propriétaire.

---

## 9.16 Design Principles

Le Component Model repose sur les principes suivants :

- composition plutôt qu'héritage ;
- responsabilité unique ;
- propriété explicite ;
- faible couplage ;
- extensibilité ;
- sérialisation déterministe ;
- validation systématique.

---

## 9.17 Summary

Le Component Model constitue le principal mécanisme d'extension du Project Model.

Il permet de construire des objets riches tout en conservant une architecture modulaire, évolutive et indépendante des technologies.

Les chapitres suivants préciseront les systèmes de métadonnées, de références d'assets et de persistance qui s'appuieront directement sur ce modèle de composition.


# 10. Metadata System

## 10.1 Overview

Le Metadata System permet d'associer des informations descriptives aux objets du Project Model.

Ces informations enrichissent le projet sans modifier son comportement métier.

Les métadonnées sont persistantes, extensibles et indépendantes du Runtime.

Elles constituent un mécanisme générique utilisable par le noyau d'OPG, les Drivers, les outils d'édition et les plugins.

---

## 10.2 Objectives

Le Metadata System poursuit les objectifs suivants :

- enrichir les objets avec des informations descriptives ;
- faciliter l'organisation des projets ;
- améliorer la recherche et le filtrage ;
- permettre la personnalisation des workflows ;
- offrir un point d'extension aux plugins.

Les métadonnées ne doivent jamais modifier le comportement fonctionnel d'un objet.

---

## 10.3 Definition

Une métadonnée représente une information descriptive associée à un objet.

Elle ne possède pas de logique métier.

Elle complète les données fonctionnelles sans les remplacer.

Les métadonnées sont persistées avec leur objet propriétaire.

---

## 10.4 Ownership

Chaque ensemble de métadonnées appartient à un unique Object.

Les métadonnées n'existent jamais indépendamment de leur propriétaire.

Leur cycle de vie est identique à celui de l'objet auquel elles sont associées.

---

## 10.5 Built-in Metadata

Le noyau du Project Model définit un ensemble minimal de métadonnées standards.

Exemples :

- Name
- Description
- Author
- Tags
- Category
- Notes
- Created Date
- Modified Date
- Version

Cette liste pourra évoluer dans les versions futures.

---

## 10.6 Custom Metadata

Les plugins peuvent ajouter leurs propres métadonnées.

Chaque métadonnée personnalisée doit :

- posséder une clé unique ;
- être sérialisable ;
- être validable ;
- respecter les règles générales du Project Model.

Le cœur du système ne dépend jamais de ces extensions.

---

## 10.7 Metadata Types

Le système doit prendre en charge différents types de valeurs.

Exemples :

- texte ;
- entier ;
- nombre décimal ;
- booléen ;
- date ;
- liste ;
- identifiant ;
- structure composée.

Les types exacts seront définis lors de l'implémentation.

---

## 10.8 Metadata Namespace

Afin d'éviter les conflits, les métadonnées sont organisées en espaces de noms.

Exemple :

```text
core:name

core:author

core:description

plugin.physics:density

plugin.render:quality
```

Chaque plugin dispose de son propre espace de noms.

---

## 10.9 Metadata Immutability

Les métadonnées peuvent être modifiées au cours de la vie d'un projet.

Cependant :

- leur structure reste cohérente ;
- leur type reste valide ;
- leur propriétaire ne change pas implicitement.

Toute modification constitue une transaction du Project Model.

---

## 10.10 Search and Filtering

Les métadonnées constituent la principale source d'information pour :

- la recherche ;
- les filtres ;
- les vues personnalisées ;
- les outils d'organisation.

Le Runtime ne dépend pas directement de ces informations.

---

## 10.11 Serialization

Les métadonnées sont sérialisées avec leur objet propriétaire.

La sérialisation doit préserver :

- les clés ;
- les types ;
- les valeurs ;
- les espaces de noms.

Deux sérialisations successives d'un même projet doivent produire exactement le même résultat.

---

## 10.12 Validation

La validation vérifie notamment :

- l'unicité des clés dans un même espace de noms ;
- la validité des types ;
- la cohérence des valeurs ;
- le respect des contraintes définies par le noyau ou les plugins.

Une métadonnée invalide rend son objet invalide.

---

## 10.13 Runtime Interaction

Les métadonnées sont accessibles au Runtime.

Le Runtime peut les consulter.

Il ne doit pas les modifier directement.

Toute modification passe par le Project Model.

---

## 10.14 Driver Interaction

Les Drivers peuvent utiliser les métadonnées pour adapter leur comportement.

Exemples :

- informations d'import ;
- paramètres d'export ;
- préférences d'affichage ;
- annotations spécifiques.

Ces usages ne doivent jamais modifier la structure du Domain Model.

---

## 10.15 UML Overview

Le système peut être représenté ainsi.

```text
                ProjectObject

                      │

                      ▼

             Metadata Collection

                      │

     ┌────────┬────────┬────────┐

     ▼        ▼        ▼        ▼

   Name    Author    Tags    Custom
```

Les métadonnées restent entièrement séparées des composants métier.

---

## 10.16 Design Principles

Le Metadata System repose sur les principes suivants :

- séparation entre données métier et données descriptives ;
- extensibilité ;
- espaces de noms ;
- validation systématique ;
- sérialisation déterministe ;
- indépendance vis-à-vis du Runtime.

---

## 10.17 Summary

Le Metadata System fournit un mécanisme standardisé permettant d'enrichir les objets du Project Model sans modifier leur comportement métier.

Il facilite l'organisation, la recherche, l'édition et l'extensibilité de la plateforme tout en conservant une architecture claire, cohérente et indépendante des technologies.


# 11. Asset Reference System

## 11.1 Overview

Le Project Model ne contient jamais directement les ressources utilisées par un projet.

Il contient uniquement des références persistantes permettant d'identifier ces ressources.

Cette séparation garantit l'indépendance du modèle vis-à-vis des formats de fichiers, des technologies de stockage et des outils d'édition.

Les Assets constituent des ressources externes décrites par le Project Model mais gérées indépendamment de celui-ci.

---

## 11.2 Objectives

Le système de références d'Assets poursuit les objectifs suivants :

- séparer les données métier des ressources ;
- éviter la duplication des fichiers ;
- permettre le partage d'Assets ;
- simplifier les migrations ;
- faciliter la reconstruction du Runtime ;
- garantir l'indépendance vis-à-vis des technologies.

---

## 11.3 Asset Definition

Un Asset représente une ressource exploitable par un projet.

Exemples :

- Mesh
- Material
- Texture
- HDRI
- Image
- Animation
- Audio
- Video
- Script
- Font
- Geometry Cache

Le Project Model ne fait aucune hypothèse sur la technologie utilisée pour représenter ces ressources.

---

## 11.4 Asset References

Les Objects ne possèdent jamais directement les Assets.

Ils possèdent uniquement des références persistantes.

Exemple :

```text
ProjectObject

      │

      ▼

AssetReference

      │

      ▼

Texture
```

Cette approche réduit le couplage et facilite la maintenance.

---

## 11.5 Identity

Chaque Asset possède une identité persistante.

Cette identité est indépendante :

- du chemin du fichier ;
- de son nom ;
- de son emplacement ;
- du Driver utilisé.

Les références utilisent exclusivement cette identité.

---

## 11.6 Shared Assets

Un même Asset peut être référencé par plusieurs objets.

Exemple :

```text
Texture

   ▲

   │

 ┌─┴─────────────┐

 │               │

Mesh A      Mesh B
```

La modification de l'Asset est visible par tous les objets qui le référencent.

---

## 11.7 External Resources

Les Assets peuvent être stockés :

- dans le projet ;
- sur le disque local ;
- sur un serveur ;
- dans une bibliothèque partagée ;
- dans un système de gestion d'Assets.

Le Project Model reste indépendant de leur localisation.

---

## 11.8 Missing Assets

Une référence peut exister même si la ressource n'est momentanément pas disponible.

Dans ce cas :

- la référence demeure valide ;
- l'identité est conservée ;
- le Runtime peut utiliser une ressource de substitution ;
- le Driver peut signaler l'absence de l'Asset.

Le Project Model reste valide.

---

## 11.9 Asset Types

Le système doit permettre l'ajout de nouveaux types d'Assets sans modification du cœur du Project Model.

Les nouveaux types peuvent être introduits par :

- des plugins ;
- des Drivers ;
- des extensions futures.

---

## 11.10 Versioning

Un Asset peut évoluer indépendamment du projet.

Le système doit permettre de connaître :

- la version de l'Asset ;
- son état ;
- sa compatibilité.

La stratégie exacte de gestion des versions sera définie dans un document spécifique.

---

## 11.11 Serialization

Les références d'Assets sont sérialisées avec les objets.

La sérialisation conserve notamment :

- l'identité de l'Asset ;
- son type ;
- ses paramètres éventuels.

Aucune donnée binaire de l'Asset n'est intégrée au Project Model.

---

## 11.12 Runtime Interaction

Le Runtime résout les références d'Assets au moment de la construction de ses structures internes.

Il peut :

- charger les ressources nécessaires ;
- créer des caches ;
- partager les instances ;
- libérer les ressources inutilisées.

Ces mécanismes restent entièrement temporaires.

---

## 11.13 Driver Interaction

Les Drivers sont responsables de l'utilisation effective des Assets.

Par exemple :

- Blender crée une Image Blender ;
- USD crée un prim approprié ;
- FBX résout les textures.

Le Project Model demeure totalement indépendant de ces mécanismes.

---

## 11.14 Validation

La validation vérifie notamment :

- l'existence des références ;
- la cohérence des types ;
- l'intégrité des identités ;
- les contraintes définies par le projet.

Une ressource manquante ne rend pas nécessairement le projet invalide.

En revanche, une référence corrompue constitue une erreur de validation.

---

## 11.15 UML Overview

Le système peut être représenté ainsi.

```text
               ProjectObject

                      │

                      ▼

             Asset Reference

                      │

        ┌─────────────┼─────────────┐

        ▼             ▼             ▼

     Texture       Material      Animation
```

Les ressources restent entièrement séparées des objets persistants.

---

## 11.16 Design Principles

Le système de références d'Assets repose sur les principes suivants :

- séparation entre objets et ressources ;
- références persistantes ;
- identité stable ;
- partage des ressources ;
- indépendance technologique ;
- sérialisation déterministe ;
- extensibilité.

---

## 11.17 Summary

Le système de références d'Assets permet au Project Model de manipuler des ressources complexes sans compromettre son indépendance vis-à-vis des technologies.

Il garantit une architecture modulaire, extensible et adaptée aux évolutions futures de la plateforme OPG.


# 12. Serialization System

## 12.1 Overview

La sérialisation permet de transformer le Project Model en une représentation persistante pouvant être sauvegardée, versionnée, échangée et reconstruite.

La sérialisation constitue une représentation fidèle du Project Model.

Elle ne représente jamais le Runtime.

Le Runtime est systématiquement reconstruit à partir des données persistées.

---

## 12.2 Objectives

Le système de sérialisation poursuit les objectifs suivants :

- persister intégralement le Project Model ;
- produire une représentation déterministe ;
- faciliter le contrôle de version ;
- simplifier les migrations ;
- préserver la compatibilité entre versions ;
- permettre la reconstruction complète du Runtime.

---

## 12.3 Serialization Scope

La sérialisation comprend notamment :

- les objets ;
- les composants ;
- les relations ;
- les métadonnées ;
- les références d'Assets ;
- les extensions ;
- les informations globales du projet.

Le Runtime, les caches et les états temporaires sont exclus.

---

## 12.4 Serialization Principles

Le système repose sur les principes suivants :

- déterminisme ;
- stabilité ;
- lisibilité ;
- extensibilité ;
- indépendance technologique ;
- compatibilité ascendante.

Ces principes s'appliquent à toutes les versions du Project Model.

---

## 12.5 Deterministic Serialization

Deux projets contenant exactement les mêmes données doivent produire exactement le même résultat de sérialisation.

Cela implique notamment :

- le même ordre des objets ;
- le même ordre des propriétés ;
- le même ordre des collections ;
- le même format des valeurs.

Cette propriété facilite :

- Git ;
- les revues de code ;
- les tests ;
- les signatures numériques.

---

## 12.6 Logical Representation

La sérialisation représente uniquement la structure logique du projet.

Elle ne décrit jamais :

- les pointeurs mémoire ;
- les adresses ;
- les caches Runtime ;
- les identifiants temporaires.

La représentation persistante demeure totalement indépendante de l'implémentation interne.

---

## 12.7 Serialization Format

Le Project Model ne dépend d'aucun format physique particulier.

La représentation logique pourra être stockée sous différentes formes :

- JSON ;
- binaire ;
- base de données ;
- format propriétaire.

La structure logique demeure identique quel que soit le support.

---

## 12.8 Stable Ordering

Toutes les collections persistées possèdent un ordre déterministe.

Cet ordre est défini par le Project Model.

Il ne dépend jamais :

- de l'ordre mémoire ;
- du Runtime ;
- des conteneurs internes du langage utilisé.

---

## 12.9 Incremental Changes

La sérialisation doit permettre d'identifier précisément les modifications apportées au projet.

Les changements doivent rester localisés.

Une modification d'un objet ne doit pas entraîner la réécriture inutile d'éléments non modifiés.

Cette propriété facilite les systèmes de contrôle de version.

---

## 12.10 Identity Preservation

La sérialisation conserve intégralement les identités persistantes.

Une opération de sauvegarde puis de chargement ne modifie jamais :

- les UUID ;
- les relations ;
- les composants ;
- les références.

L'identité constitue la base de la reconstruction du Project Model.

---

## 12.11 Extension Serialization

Les Extensions participent à la sérialisation.

Chaque extension est responsable de la représentation de ses propres données.

Le noyau du Project Model n'a pas besoin de connaître leur contenu.

Cette approche garantit l'évolutivité du système.

---

## 12.12 Runtime Reconstruction

Après désérialisation, le Runtime est entièrement reconstruit.

Aucune information Runtime n'est persistée.

Le processus général est le suivant :

```text
Serialized Project

        │

        ▼

Deserialize

        │

        ▼

Project Model

        │

        ▼

Runtime Builder

        │

        ▼

Runtime
```

Le Runtime reconstruit doit être strictement équivalent à celui précédant la sauvegarde.

---

## 12.13 Validation

La désérialisation est suivie d'une validation complète.

Cette validation vérifie notamment :

- la cohérence des identités ;
- la hiérarchie ;
- les relations ;
- les composants ;
- les métadonnées ;
- les références d'Assets.

Un projet invalide ne doit jamais produire un Runtime incohérent.

---

## 12.14 Error Handling

Le système doit distinguer plusieurs catégories d'erreurs :

- erreur de format ;
- erreur de version ;
- donnée manquante ;
- donnée corrompue ;
- violation des contraintes métier.

Chaque catégorie possède une stratégie de traitement spécifique.

---

## 12.15 UML Overview

Le processus de persistance peut être représenté ainsi.

```text
Project Model

      │

      ▼

Serialization

      │

      ▼

Persistent Representation

      │

      ▼

Deserialization

      │

      ▼

Project Model

      │

      ▼

Runtime Builder
```

Le Runtime ne participe jamais directement à la sérialisation.

---

## 12.16 Design Principles

Le système de sérialisation repose sur les principes suivants :

- persistance du seul Project Model ;
- reconstruction systématique du Runtime ;
- déterminisme ;
- stabilité ;
- extensibilité ;
- validation automatique ;
- indépendance technologique.

---

## 12.17 Summary

Le système de sérialisation constitue le mécanisme garantissant la pérennité des projets OPG.

Il assure une représentation persistante fidèle, stable, déterministe et indépendante des technologies, permettant la reconstruction complète du Runtime et l'évolution contrôlée du Project Model.


# 13. Versioning & Migration

## 13.1 Overview

Le Project Model est conçu pour évoluer sur le long terme.

De nouvelles fonctionnalités, de nouveaux composants et de nouveaux types d'objets seront progressivement introduits.

Le système de versionnement garantit que cette évolution peut s'effectuer sans compromettre l'intégrité des projets existants.

Chaque version du Project Model possède une stratégie de migration clairement définie.

---

## 13.2 Objectives

Le système de versionnement poursuit les objectifs suivants :

- préserver la compatibilité des projets ;
- permettre l'évolution du modèle ;
- limiter les ruptures de compatibilité ;
- assurer des migrations reproductibles ;
- garantir l'intégrité des données persistantes.

---

## 13.3 Schema Version

Chaque Project possède un numéro de version de schéma.

Cette version représente la structure du Project Model utilisée lors de la sauvegarde.

Elle est indépendante :

- de la version du Runtime ;
- de la version des Drivers ;
- de la version des plugins.

Le numéro de schéma constitue la référence officielle pour toutes les migrations.

---

## 13.4 Project Version

Le Project possède également une version de projet.

Cette version correspond au document utilisateur.

Elle peut évoluer indépendamment du schéma interne.

Exemple :

- Project Version : 2.3
- Schema Version : 7

Ces deux informations remplissent des rôles différents.

---

## 13.5 Compatibility

Trois niveaux de compatibilité sont définis.

### Backward Compatibility

Une nouvelle version d'OPG peut ouvrir un projet créé avec une version plus ancienne.

---

### Forward Compatibility

Lorsqu'elle est possible, une ancienne version d'OPG peut ignorer certaines informations inconnues sans rendre le projet inutilisable.

---

### Breaking Changes

Certaines évolutions peuvent nécessiter une migration obligatoire.

Ces changements sont explicitement documentés.

---

## 13.6 Migration Pipeline

L'ouverture d'un projet suit le processus suivant.

```text
Project File

      │

      ▼

Read Schema Version

      │

      ▼

Migration Manager

      │

      ▼

Migration Steps

      │

      ▼

Validated Project Model

      │

      ▼

Runtime Builder
```

Chaque étape possède une responsabilité clairement définie.

---

## 13.7 Incremental Migration

Les migrations sont toujours incrémentales.

Exemple :

```text
Version 3

      │

      ▼

Migration 3 → 4

      │

      ▼

Migration 4 → 5

      │

      ▼

Migration 5 → 6
```

Une migration directe entre deux versions éloignées est évitée.

Cette approche simplifie la maintenance et les tests.

---

## 13.8 Deterministic Migration

Une migration est déterministe.

Deux projets identiques produisent toujours exactement le même résultat après migration.

Les migrations ne doivent jamais introduire de comportement aléatoire.

---

## 13.9 Data Preservation

Une migration ne doit jamais supprimer des données sans justification explicite.

Lorsque certaines informations deviennent obsolètes :

- elles sont transformées ;
- elles sont remplacées ;
- ou elles sont archivées.

La perte de données constitue une exception documentée.

---

## 13.10 Extension Migration

Chaque Extension est responsable de la migration de ses propres données.

Le noyau du Project Model ne connaît pas leur structure interne.

Les plugins doivent fournir leurs propres mécanismes de migration.

---

## 13.11 Validation

Chaque migration est suivie d'une validation complète.

Cette validation vérifie notamment :

- les identités ;
- la hiérarchie ;
- les relations ;
- les composants ;
- les métadonnées ;
- les références d'Assets.

Un projet migré ne peut être utilisé que si cette validation est réussie.

---

## 13.12 Migration History

Toutes les migrations sont documentées.

Pour chaque version sont précisés :

- les changements introduits ;
- les transformations appliquées ;
- les incompatibilités éventuelles ;
- les impacts connus.

Cette documentation fait partie intégrante de l'architecture.

---

## 13.13 Runtime Independence

Le Runtime ne participe jamais aux migrations.

Les migrations s'appliquent exclusivement au Project Model.

Le Runtime est reconstruit uniquement après la fin de la migration et de la validation.

---

## 13.14 Failure Handling

En cas d'échec d'une migration :

- le projet d'origine est conservé ;
- la migration est interrompue ;
- une erreur explicite est produite ;
- aucun Runtime n'est construit.

Le système ne doit jamais produire un projet partiellement migré.

---

## 13.15 UML Overview

Le processus global peut être représenté ainsi.

```text
Project File

      │

      ▼

Schema Detection

      │

      ▼

Migration Manager

      │

      ▼

Migration Pipeline

      │

      ▼

Validation

      │

      ▼

Project Model

      │

      ▼

Runtime Builder
```

---

## 13.16 Design Principles

Le système de versionnement repose sur les principes suivants :

- migrations incrémentales ;
- déterminisme ;
- validation systématique ;
- préservation des données ;
- indépendance vis-à-vis du Runtime ;
- documentation obligatoire.

---

## 13.17 Summary

Le système de versionnement garantit que le Project Model peut évoluer de manière maîtrisée pendant toute la durée de vie d'OPG.

Il assure la compatibilité des projets, la reproductibilité des migrations et la stabilité des données persistantes tout en permettant l'évolution continue de la plateforme.


# 14. Validation System

## 14.1 Overview

Le Validation System garantit l'intégrité structurelle, fonctionnelle et sémantique du Project Model.

Avant toute opération majeure — chargement, sauvegarde, migration, construction du Runtime ou export — le Project Model doit être validé.

Le Runtime ne doit jamais être construit à partir d'un modèle invalide.

La validation constitue donc une étape obligatoire du cycle de vie d'un projet.

---

## 14.2 Objectives

Le Validation System poursuit les objectifs suivants :

- garantir la cohérence du Project Model ;
- détecter les erreurs avant leur propagation ;
- protéger le Runtime contre les données invalides ;
- fournir des diagnostics explicites ;
- permettre une évolution sûre du modèle.

---

## 14.3 Validation Philosophy

La validation ne corrige jamais un projet.

Elle vérifie uniquement sa conformité à la spécification.

Les corrections éventuelles relèvent :

- de l'utilisateur ;
- d'un outil d'édition ;
- d'un processus de migration documenté.

Le Validation System demeure totalement déterministe.

---

## 14.4 Validation Levels

La validation est organisée en plusieurs niveaux.

### Structural Validation

Vérifie notamment :

- l'existence de la racine ;
- la cohérence de la hiérarchie ;
- les identités ;
- les composants.

---

### Referential Validation

Vérifie :

- les références ;
- les Assets ;
- les dépendances ;
- les liens entre objets.

---

### Semantic Validation

Vérifie les contraintes métier.

Exemples :

- composants obligatoires ;
- incompatibilités ;
- cardinalités ;
- règles du domaine.

---

### Extension Validation

Chaque plugin valide ses propres données.

Le noyau du Project Model ne dépend pas de ces validations spécialisées.

---

## 14.5 Validation Pipeline

Le processus suit toujours le même ordre.

```text
Project Model

      │

      ▼

Structural Validation

      │

      ▼

Identity Validation

      │

      ▼

Relationship Validation

      │

      ▼

Component Validation

      │

      ▼

Metadata Validation

      │

      ▼

Asset Validation

      │

      ▼

Extension Validation

      │

      ▼

Validation Report
```

Chaque étape suppose que la précédente est valide.

---

## 14.6 Validation Rules

Une règle de validation possède les caractéristiques suivantes :

- un identifiant ;
- une description ;
- une sévérité ;
- une logique de vérification ;
- un message de diagnostic.

Chaque règle est indépendante des autres.

---

## 14.7 Validation Severity

Le système distingue plusieurs niveaux.

### Information

Indique une observation sans impact sur la validité.

---

### Warning

Signale une situation inhabituelle.

Le projet reste valide.

---

### Error

Indique une violation de la spécification.

Le projet devient invalide.

Le Runtime ne peut pas être construit.

---

### Fatal

Indique une corruption majeure.

Le chargement du projet doit être interrompu.

---

## 14.8 Validation Report

Chaque validation produit un rapport structuré.

Le rapport contient notamment :

- les règles exécutées ;
- les diagnostics ;
- les objets concernés ;
- les niveaux de sévérité ;
- le résultat global.

Le rapport est entièrement déterministe.

---

## 14.9 Incremental Validation

Lorsqu'un projet est modifié, seules les parties concernées peuvent être revalidées.

Le système doit néanmoins garantir que le résultat obtenu est strictement identique à celui d'une validation complète.

Cette optimisation ne modifie jamais les règles de validation.

---

## 14.10 Runtime Interaction

Le Runtime Builder dépend directement du Validation System.

Le processus est le suivant :

```text
Project Model

      │

      ▼

Validation

      │

      ▼

Runtime Builder
```

En cas d'échec de validation :

- aucun Runtime n'est créé ;
- aucun Driver n'est initialisé ;
- aucun traitement d'exécution ne démarre.

---

## 14.11 Driver Interaction

Les Drivers ne réalisent jamais la validation métier.

Ils peuvent effectuer des vérifications propres à leur technologie.

Ces vérifications ne remplacent jamais la validation du Project Model.

---

## 14.12 Extension Validation

Les plugins peuvent enregistrer leurs propres validateurs.

Chaque validateur :

- possède un identifiant ;
- déclare les types concernés ;
- produit des diagnostics normalisés.

Les extensions ne peuvent pas désactiver les validations du noyau.

---

## 14.13 Validation Performance

Le Validation System doit rester performant sur les projets volumineux.

Les optimisations autorisées comprennent notamment :

- index temporaires ;
- caches de validation ;
- validation incrémentale ;
- parallélisation lorsque cela est possible.

Ces optimisations ne doivent jamais modifier le résultat de la validation.

---

## 14.14 UML Overview

Le système peut être représenté ainsi.

```text
Project Model

      │

      ▼

Validation Engine

      │

 ┌────┼────┬────┬────┐

 ▼    ▼    ▼    ▼    ▼

Structure

Identity

Relations

Components

Extensions

      │

      ▼

Validation Report
```

Le Runtime Builder intervient uniquement après une validation réussie.

---

## 14.15 Design Principles

Le Validation System repose sur les principes suivants :

- validation obligatoire ;
- déterminisme ;
- diagnostics explicites ;
- séparation des responsabilités ;
- extensibilité ;
- indépendance vis-à-vis des Drivers.

---

## 14.16 Validation Invariants

Les invariants suivants sont obligatoires.

Un Project Model valide possède toujours :

- une unique racine ;
- des identités uniques ;
- une hiérarchie acyclique ;
- des références cohérentes ;
- des composants valides ;
- des métadonnées conformes ;
- des références d'Assets valides ;
- des extensions validées.

Aucun Runtime ne peut être construit si l'un de ces invariants est violé.

---

## 14.17 Summary

Le Validation System constitue le gardien de l'intégrité du Project Model.

Il garantit que seules des données cohérentes, complètes et conformes à la spécification peuvent être utilisées pour construire le Runtime.

Il représente ainsi l'un des mécanismes fondamentaux assurant la fiabilité, la stabilité et la pérennité de l'architecture OPG.


# 15. Transaction System

## 15.1 Overview

Le Transaction System garantit que toutes les modifications apportées au Project Model sont exécutées de manière cohérente, atomique et traçable.

Aucune modification persistante ne peut être effectuée directement sur le Project Model.

Toute modification passe obligatoirement par une transaction.

Cette règle garantit l'intégrité du modèle, facilite les mécanismes d'annulation et prépare l'évolution vers des scénarios collaboratifs.

---

## 15.2 Objectives

Le Transaction System poursuit les objectifs suivants :

- garantir l'atomicité des modifications ;
- préserver la cohérence du Project Model ;
- permettre l'annulation et la restauration des opérations ;
- assurer la traçabilité des changements ;
- préparer les évolutions futures vers le travail collaboratif.

---

## 15.3 Transaction Definition

Une transaction représente une modification logique appliquée au Project Model.

Elle regroupe une ou plusieurs opérations considérées comme une seule unité de travail.

Une transaction est soit :

- entièrement appliquée ;
- entièrement annulée.

Aucun état intermédiaire ne peut être rendu persistant.

---

## 15.4 Transaction Lifecycle

Une transaction suit toujours le cycle suivant :

```text
Create Transaction

        │

        ▼

Validate

        │

        ▼

Execute

        │

        ▼

Commit

        │

        ▼

Project Model Updated
```

En cas d'échec, la transaction est annulée avant toute modification persistante.

---

## 15.5 Atomicity

Une transaction est atomique.

Toutes les modifications qu'elle contient sont appliquées simultanément.

Si une seule opération échoue :

- aucune modification n'est conservée ;
- le Project Model retrouve son état précédent.

Cette propriété garantit la cohérence du système.

---

## 15.6 Consistency

Chaque transaction doit préserver les invariants du Project Model.

Après validation et exécution :

- la hiérarchie reste valide ;
- les identités restent uniques ;
- les références restent cohérentes ;
- les composants respectent leurs contraintes.

Une transaction ne peut jamais produire un modèle invalide.

---

## 15.7 Isolation

Pendant son exécution, une transaction est isolée des autres traitements.

Les modifications en cours ne deviennent visibles qu'après le Commit.

Cette règle garantit un état cohérent du Project Model.

---

## 15.8 Durability

Après validation et Commit, les modifications deviennent persistantes.

Elles seront présentes lors de la prochaine sérialisation du projet.

Une transaction validée ne peut pas être perdue sans une action explicite.

---

## 15.9 Transaction Types

Le système prend en charge plusieurs catégories de transactions.

Exemples :

- création d'objet ;
- suppression d'objet ;
- déplacement dans la hiérarchie ;
- modification de composant ;
- modification de métadonnées ;
- ajout ou suppression de références ;
- modification d'Assets.

Toutes utilisent le même mécanisme transactionnel.

---

## 15.10 Nested Transactions

Une transaction peut contenir plusieurs opérations internes.

Cependant, le Project Model ne considère qu'un seul résultat final.

Les transactions imbriquées restent transparentes pour le modèle persistant.

Leur comportement détaillé sera défini lors de l'implémentation.

---

## 15.11 Undo / Redo

Chaque transaction doit pouvoir produire les informations nécessaires aux mécanismes :

- Undo ;
- Redo.

Le système ne définit pas encore leur implémentation.

Il garantit uniquement que les données nécessaires pourront être produites.

---

## 15.12 Transaction Log

Le système peut conserver un journal des transactions.

Chaque entrée peut notamment contenir :

- un identifiant ;
- un horodatage ;
- l'auteur ;
- le type d'opération ;
- les objets concernés.

Ce journal est distinct du Project Model lui-même.

---

## 15.13 Runtime Interaction

Le Runtime n'effectue jamais de modifications directes.

Les changements transitent toujours par une transaction.

Le Runtime est ensuite synchronisé à partir du Project Model mis à jour.

Cette approche garantit une séparation stricte des responsabilités.

---

## 15.14 Driver Interaction

Les Drivers ne modifient jamais directement les données persistantes.

Lorsqu'un Driver provoque une modification :

- une transaction est créée ;
- le Project Model est mis à jour ;
- le Runtime est synchronisé ;
- le Driver reçoit ensuite l'état cohérent.

---

## 15.15 Validation

Chaque transaction est validée avant son exécution.

La validation vérifie notamment :

- les droits de modification ;
- les contraintes métier ;
- les dépendances ;
- les identités ;
- les références.

Une transaction invalide est rejetée.

---

## 15.16 Error Handling

En cas d'erreur :

- toutes les modifications sont annulées ;
- le Project Model retrouve son état initial ;
- un diagnostic explicite est produit ;
- aucun Runtime incohérent n'est construit.

Le système garantit qu'aucune transaction partiellement appliquée ne peut subsister.

---

## 15.17 UML Overview

Le processus général peut être représenté ainsi.

```text
User Action

      │

      ▼

Transaction

      │

      ▼

Validation

      │

      ▼

Execution

      │

      ▼

Commit

      │

      ▼

Project Model

      │

      ▼

Runtime Synchronization
```

Le Runtime n'est synchronisé qu'après un Commit réussi.

---

## 15.18 Design Principles

Le Transaction System repose sur les principes suivants :

- atomicité ;
- cohérence ;
- isolation ;
- durabilité ;
- validation obligatoire ;
- traçabilité ;
- séparation entre modifications et exécution.

---

## 15.19 ACID Compliance

Le Transaction System s'inspire des propriétés ACID :

- Atomicity ;
- Consistency ;
- Isolation ;
- Durability.

Ces principes sont adaptés au contexte du Project Model afin de garantir la stabilité et la reproductibilité des modifications.

---

## 15.20 Summary

Le Transaction System constitue le mécanisme officiel de modification du Project Model.

Il garantit que toutes les évolutions du projet sont cohérentes, validées, atomiques et entièrement traçables.

Il prépare également les futurs systèmes d'Undo/Redo, de collaboration et d'historisation qui seront développés dans les prochaines évolutions d'OPG.


# 16. Runtime Integration

## 16.1 Overview

Le Runtime est une représentation temporaire du Project Model destinée exclusivement à l'exécution.

Le Runtime n'est jamais persisté.

Il est systématiquement reconstruit à partir d'un Project Model valide.

Cette séparation garantit que le Project Model demeure l'unique source de vérité persistante.

---

## 16.2 Objectives

L'intégration entre le Project Model et le Runtime poursuit les objectifs suivants :

- construire un Runtime cohérent ;
- préserver l'intégrité du Project Model ;
- garantir une reconstruction déterministe ;
- séparer totalement la persistance de l'exécution ;
- permettre l'évolution indépendante des deux systèmes.

---

## 16.3 Architectural Principle

Le Runtime ne constitue jamais une copie persistante du Project Model.

Il représente une projection optimisée pour l'exécution.

Le Project Model décrit le projet.

Le Runtime interprète cette description.

Cette distinction constitue l'un des principes fondamentaux de l'architecture OPG.

---

## 16.4 Build Pipeline

La construction du Runtime suit toujours le même processus.

```text
Project Model

      │

      ▼

Validation

      │

      ▼

Runtime Builder

      │

      ▼

Runtime Graph

      │

      ▼

Runtime Services

      │

      ▼

Executable Runtime
```

Chaque étape dépend exclusivement de la précédente.

---

## 16.5 Runtime Builder Responsibilities

Le Runtime Builder est responsable de :

- parcourir le Project Model ;
- créer les objets Runtime ;
- construire le Runtime Graph ;
- enregistrer les Services ;
- préparer les systèmes Runtime ;
- initialiser les Plugins Runtime.

Il ne modifie jamais le Project Model.

---

## 16.6 Runtime Objects

Chaque Runtime Object possède un lien direct vers son objet persistant d'origine.

Cette correspondance est maintenue pendant toute la durée de vie du Runtime.

Elle permet notamment :

- la synchronisation ;
- les mises à jour ;
- la résolution des références.

---

## 16.7 Runtime Graph Construction

Le Runtime Graph est construit exclusivement à partir du Project Model.

Le Runtime Builder interprète :

- les objets ;
- les composants ;
- les relations ;
- les références ;
- les métadonnées nécessaires à l'exécution.

Le Runtime Graph n'est jamais persisté.

---

## 16.8 Runtime Services

Les Runtime Services sont créés pendant la construction du Runtime.

Ils regroupent notamment :

- Service Registry ;
- Event System ;
- Scheduler ;
- Plugin Manager ;
- Metrics ;
- Logging ;
- Health Monitoring.

Ces services appartiennent exclusivement au Runtime.

---

## 16.9 Runtime Components

Les Components du Project Model ne sont pas exécutables.

Le Runtime peut créer des représentations optimisées de ces Components.

Ces représentations :

- sont temporaires ;
- sont reconstruites à chaque démarrage ;
- ne sont jamais persistées.

---

## 16.10 Runtime State

Le Runtime possède son propre état.

Cet état comprend notamment :

- caches ;
- index ;
- états temporaires ;
- ressources allouées ;
- résultats de calcul.

Aucune de ces informations ne fait partie du Project Model.

---

## 16.11 Synchronization Principle

Le Runtime constitue une projection du Project Model.

Lorsqu'une modification intervient :

```text
Project Model

      │

      ▼

Transaction

      │

      ▼

Validation

      │

      ▼

Runtime Synchronization
```

Le Runtime est mis à jour uniquement après une transaction validée.

---

## 16.12 Runtime Destruction

Le Runtime peut être détruit à tout moment.

Sa destruction ne provoque aucune perte d'information.

Toutes les données persistantes demeurent stockées dans le Project Model.

Cette propriété garantit la reconstruction complète du Runtime.

---

## 16.13 Runtime Rebuild

Une reconstruction complète peut être déclenchée :

- après le chargement d'un projet ;
- après une migration ;
- après certaines modifications majeures ;
- après une récupération d'erreur.

Le résultat obtenu doit être strictement déterministe.

---

## 16.14 Runtime Independence

Le Runtime ignore :

- le format de sérialisation ;
- les fichiers de projet ;
- les migrations ;
- les mécanismes de stockage.

Ces responsabilités appartiennent exclusivement au Project Model.

---

## 16.15 Error Handling

Si la construction du Runtime échoue :

- le Project Model reste inchangé ;
- aucun Runtime partiellement construit n'est conservé ;
- les ressources temporaires sont libérées ;
- un diagnostic détaillé est produit.

Le système garantit qu'aucun Runtime incohérent ne peut être utilisé.

---

## 16.16 UML Overview

Le processus général peut être représenté ainsi.

```text
               Project Model

                     │

                     ▼

               Runtime Builder

                     │

         ┌───────────┼───────────┐

         ▼           ▼           ▼

 Runtime Graph   Services   Plugins

         │

         ▼

     Runtime Engine
```

Le Runtime Builder constitue le seul point de transformation entre le modèle persistant et le modèle d'exécution.

---

## 16.17 Design Principles

L'intégration Runtime repose sur les principes suivants :

- reconstruction systématique ;
- absence de persistance Runtime ;
- séparation stricte des responsabilités ;
- déterminisme ;
- synchronisation contrôlée ;
- indépendance vis-à-vis des Drivers.

---

## 16.18 Invariants

Les invariants suivants sont obligatoires.

Un Runtime valide :

- provient toujours d'un Project Model valide ;
- ne modifie jamais directement le Project Model ;
- peut être détruit sans perte d'information ;
- peut être reconstruit à tout moment ;
- conserve les correspondances avec les identités persistantes.

---

## 16.19 Summary

L'intégration entre le Project Model et le Runtime constitue le point de transition entre la persistance et l'exécution.

Elle garantit que le Runtime demeure une représentation temporaire, reconstruisible et totalement indépendante des mécanismes de stockage, tout en restant synchronisé avec l'unique source de vérité : le Project Model.


# 17. Driver Integration

## 17.1 Overview

Les Drivers constituent la couche d'adaptation entre le Runtime et les technologies externes.

Ils permettent de représenter, manipuler ou exécuter les données du Runtime dans un environnement particulier sans modifier le Project Model.

Le Driver ne possède aucune logique métier.

Son rôle est exclusivement technique.

---

## 17.2 Objectives

Le système de Drivers poursuit les objectifs suivants :

- isoler les dépendances technologiques ;
- permettre plusieurs implémentations d'un même Runtime ;
- garantir l'indépendance du Project Model ;
- simplifier l'ajout de nouvelles plateformes ;
- assurer une synchronisation cohérente.

---

## 17.3 Architectural Position

Le Driver constitue la dernière couche de l'architecture OPG.

```text
Project Model

        │

        ▼

Runtime

        │

        ▼

Driver

        │

        ▼

Technology
```

Le Driver ne connaît jamais directement le Project Model.

Toutes les interactions transitent exclusivement par le Runtime.

---

## 17.4 Driver Responsibilities

Un Driver est responsable de :

- créer les représentations natives ;
- synchroniser les états ;
- convertir les données Runtime ;
- recevoir les événements externes ;
- appliquer les mises à jour autorisées.

Le Driver n'est jamais responsable :

- des règles métier ;
- de la validation ;
- de la sérialisation ;
- des transactions.

---

## 17.5 Driver Independence

Chaque Driver est totalement indépendant des autres.

L'existence d'un Driver Blender n'implique aucune dépendance vers :

- USD ;
- FBX ;
- Unreal Engine ;
- Unity ;
- Godot ;
- Maya ;
- Houdini.

Chaque Driver implémente uniquement le contrat défini par le Runtime.

---

## 17.6 Runtime Contract

Le Runtime expose un contrat stable à destination des Drivers.

Ce contrat définit notamment :

- les objets Runtime accessibles ;
- les événements ;
- les services ;
- les opérations de synchronisation ;
- les points d'extension.

Les Drivers ne doivent jamais accéder aux structures internes du Runtime.

---

## 17.7 Synchronization

Le Driver synchronise son environnement avec le Runtime.

Deux types de synchronisation sont possibles.

### Runtime → Driver

Le Runtime demande au Driver de refléter l'état courant.

Exemples :

- création d'un objet ;
- suppression ;
- modification d'un composant.

---

### Driver → Runtime

Le Driver signale une modification provenant de la technologie externe.

Cette modification devient une transaction du Project Model après validation.

Le Driver ne modifie jamais directement les données persistantes.

---

## 17.8 Driver Lifecycle

Chaque Driver suit le cycle suivant.

```text
Load

    │

    ▼

Initialize

    │

    ▼

Synchronize

    │

    ▼

Execute

    │

    ▼

Shutdown
```

Le Runtime contrôle entièrement ce cycle de vie.

---

## 17.9 Driver State

Le Driver peut conserver des informations temporaires.

Exemples :

- pointeurs natifs ;
- handles GPU ;
- caches internes ;
- ressources chargées.

Ces informations :

- ne sont jamais persistées ;
- ne font jamais partie du Project Model.

---

## 17.10 Event Flow

Le flux des événements suit toujours une direction contrôlée.

```text
Technology

      │

      ▼

Driver

      │

      ▼

Runtime

      │

      ▼

Project Transaction

      │

      ▼

Project Model
```

Le Driver constitue uniquement un point de passage.

---

## 17.11 Multiple Drivers

Un même Runtime peut être synchronisé avec plusieurs Drivers.

Exemple :

```text
Runtime

 │

 ├──────────────┐

 ▼              ▼

Blender      USD

 │              │

 ▼              ▼

Scene A     Scene B
```

Chaque Driver reste indépendant.

---

## 17.12 Driver Failure

Une défaillance d'un Driver ne doit jamais corrompre le Project Model.

En cas d'erreur :

- le Driver est isolé ;
- le Runtime reste cohérent ;
- le Project Model demeure intact.

La reprise peut être effectuée par une nouvelle synchronisation.

---

## 17.13 Driver Registration

Les Drivers sont enregistrés auprès du Runtime.

Chaque Driver déclare notamment :

- son identifiant ;
- son nom ;
- sa version ;
- ses capacités ;
- les extensions qu'il prend en charge.

Cette déclaration permet une découverte dynamique des Drivers disponibles.

---

## 17.14 Driver Extensibility

L'architecture permet l'ajout de nouveaux Drivers sans modification du Project Model.

Les futurs Drivers pourront notamment cibler :

- Blender ;
- USD ;
- FBX ;
- Unreal Engine ;
- Unity ;
- Godot ;
- Maya ;
- Houdini ;
- des moteurs propriétaires.

Le contrat Runtime reste identique.

---

## 17.15 UML Overview

Le modèle général peut être représenté ainsi.

```text
               Runtime

                  │

      ┌───────────┼───────────┐

      ▼           ▼           ▼

 Blender      USD Driver   Custom Driver

      │           │           │

      ▼           ▼           ▼

 Blender      USD Scene   External Tool
```

Tous les Drivers implémentent le même contrat architectural.

---

## 17.16 Design Principles

Le système de Drivers repose sur les principes suivants :

- indépendance technologique ;
- contrat Runtime unique ;
- absence de logique métier ;
- synchronisation contrôlée ;
- isolation des erreurs ;
- extensibilité ;
- interchangeabilité.

---

## 17.17 Invariants

Les invariants suivants sont obligatoires.

Un Driver :

- ne connaît jamais directement le Project Model ;
- ne modifie jamais les données persistantes ;
- ne réalise jamais de validation métier ;
- ne contient jamais de logique fonctionnelle ;
- peut être remplacé sans modifier le Runtime.

---

## 17.18 Summary

Le système de Drivers constitue la couche d'adaptation entre l'architecture OPG et les technologies externes.

Il garantit que le Project Model demeure totalement indépendant des outils utilisés tout en permettant au Runtime d'interagir avec une grande variété d'environnements grâce à un contrat unique, stable et extensible.


# 18. Extension System

## 18.1 Overview

Le Extension System permet d'étendre les capacités d'OPG sans modifier le noyau du Project Model.

Les extensions constituent des modules indépendants capables d'ajouter de nouveaux comportements, de nouveaux types d'objets, de nouveaux composants ou de nouveaux outils tout en respectant les règles fondamentales de l'architecture.

Le cœur du système reste stable tandis que les fonctionnalités évoluent au travers d'extensions.

---

## 18.2 Objectives

Le Extension System poursuit les objectifs suivants :

- permettre l'évolution du système sans modifier le Core ;
- favoriser la modularité ;
- simplifier le développement de plugins ;
- garantir la compatibilité des extensions ;
- isoler les dépendances spécifiques.

---

## 18.3 Architectural Principles

Les extensions sont considérées comme des modules de premier niveau.

Elles ne modifient jamais directement le noyau du Project Model.

Toutes les interactions passent par les interfaces publiques définies par l'architecture.

Cette règle garantit la stabilité du Core.

---

## 18.4 Extension Types

Le système autorise plusieurs catégories d'extensions.

Exemples :

- nouveaux Components ;
- nouveaux Object Types ;
- nouveaux Metadata Types ;
- nouveaux Validators ;
- nouveaux Importers ;
- nouveaux Exporters ;
- nouveaux Drivers ;
- nouveaux Runtime Services ;
- nouveaux outils d'édition.

Chaque catégorie respecte un contrat spécifique.

---

## 18.5 Extension Registration

Chaque extension doit être enregistrée auprès du système.

L'enregistrement déclare notamment :

- son identifiant ;
- son nom ;
- sa version ;
- son auteur ;
- ses dépendances ;
- ses capacités.

Le registre permet la découverte dynamique des extensions disponibles.

---

## 18.6 Extension Lifecycle

Une extension suit le cycle de vie suivant.

```text
Discovery

     │

     ▼

Registration

     │

     ▼

Initialization

     │

     ▼

Activation

     │

     ▼

Execution

     │

     ▼

Deactivation

     │

     ▼

Unload
```

Le Runtime contrôle intégralement ce cycle.

---

## 18.7 Extension Isolation

Chaque extension est isolée des autres.

Une extension ne doit jamais accéder directement :

- aux données internes d'une autre extension ;
- aux structures privées du Runtime ;
- aux structures privées du Project Model.

Toutes les interactions passent par les interfaces publiques.

---

## 18.8 Dependencies

Une extension peut dépendre d'autres extensions.

Ces dépendances sont explicites.

Le système vérifie :

- leur existence ;
- leur compatibilité ;
- leur version minimale.

Les dépendances circulaires sont interdites.

---

## 18.9 Extension Data

Une extension peut stocker ses propres données dans le Project Model.

Ces données :

- restent isolées ;
- sont sérialisées ;
- participent à la validation ;
- suivent les règles générales du Project Model.

Le Core n'interprète jamais ces données.

---

## 18.10 Runtime Extensions

Une extension peut également ajouter des fonctionnalités Runtime.

Exemples :

- systèmes ;
- services ;
- processeurs ;
- événements ;
- observateurs.

Ces ajouts restent entièrement séparés du Project Model.

---

## 18.11 Driver Extensions

Les Drivers peuvent eux aussi être étendus.

Une extension Driver peut notamment fournir :

- nouveaux importeurs ;
- nouveaux exporteurs ;
- nouveaux convertisseurs ;
- nouveaux adaptateurs technologiques.

Le contrat Driver reste inchangé.

---

## 18.12 Validation

Chaque extension participe à la validation du projet.

Elle vérifie uniquement les données dont elle est responsable.

Le Validation System agrège ensuite tous les résultats dans un rapport unique.

---

## 18.13 Serialization

Les données d'une extension participent à la sérialisation.

Le noyau garantit leur persistance.

L'extension reste responsable :

- du format logique de ses données ;
- de leur migration ;
- de leur validation.

---

## 18.14 Versioning

Chaque extension possède son propre numéro de version.

Le système vérifie la compatibilité entre :

- le Project Model ;
- le Runtime ;
- les Extensions.

Une extension incompatible ne doit jamais être activée.

---

## 18.15 Error Handling

Une défaillance d'une extension ne doit jamais compromettre le fonctionnement du Core.

En cas d'erreur :

- l'extension est isolée ;
- un diagnostic est produit ;
- le Runtime poursuit son exécution lorsque cela est possible.

Le Project Model demeure toujours cohérent.

---

## 18.16 UML Overview

Le système peut être représenté ainsi.

```text
                 Core

                  │

      ┌───────────┼───────────┐

      ▼           ▼           ▼

 Extension A  Extension B  Extension C

      │           │           │

      ▼           ▼           ▼

 Components  Validators  Drivers
```

Toutes les extensions utilisent les interfaces publiques du Core.

---

## 18.17 Design Principles

Le système d'extensions repose sur les principes suivants :

- stabilité du Core ;
- modularité ;
- isolation ;
- extensibilité ;
- contrats publics ;
- validation indépendante ;
- sérialisation contrôlée.

---

## 18.18 Security

Les extensions sont considérées comme des composants de confiance limitée.

Elles ne doivent jamais :

- contourner les transactions ;
- modifier directement les données persistantes ;
- désactiver les validations du Core ;
- accéder aux structures internes non publiques.

Le Runtime reste responsable du respect de ces contraintes.

---

## 18.19 Future Evolution

L'architecture permet l'apparition de nouvelles catégories d'extensions sans modification du noyau.

Cette capacité garantit la pérennité du système sur le long terme.

Les futures évolutions pourront ainsi enrichir OPG tout en conservant une architecture stable.

---

## 18.20 Summary

Le Extension System constitue le principal mécanisme d'évolution d'OPG.

Il permet d'ajouter de nouvelles capacités sans modifier le noyau de la plateforme, garantissant ainsi une architecture modulaire, extensible et durable.

Le Core demeure volontairement minimal, tandis que les fonctionnalités spécifiques sont apportées par des extensions clairement isolées et contractuellement définies.


# 19. Performance Architecture

## 19.1 Overview

Les performances du Project Model constituent une exigence architecturale.

Le système doit rester performant, prédictible et évolutif, quel que soit le volume des données manipulées.

Les optimisations ne doivent jamais modifier les règles métier définies par cette spécification.

Le comportement fonctionnel prévaut toujours sur les performances.

---

## 19.2 Objectives

L'architecture doit permettre :

- le chargement rapide des projets ;
- une navigation fluide dans le Project Model ;
- des recherches efficaces ;
- une validation performante ;
- une reconstruction rapide du Runtime ;
- une consommation mémoire maîtrisée.

Ces objectifs doivent rester compatibles avec la lisibilité du système.

---

## 19.3 Performance Principles

Les optimisations reposent sur les principes suivants :

- déterminisme ;
- simplicité ;
- reproductibilité ;
- absence de duplication inutile ;
- séparation entre données persistantes et caches.

Les optimisations ne doivent jamais modifier le comportement métier.

---

## 19.4 Memory Model

Le Project Model représente uniquement les données persistantes.

Il ne contient jamais :

- de caches Runtime ;
- d'états temporaires ;
- de ressources natives ;
- de structures optimisées pour l'exécution.

Ces éléments appartiennent exclusivement au Runtime.

---

## 19.5 Lazy Loading

L'architecture autorise le chargement différé de certaines informations.

Exemples :

- Assets ;
- Extensions ;
- données volumineuses ;
- ressources externes.

Le comportement observé par les utilisateurs demeure identique, que le chargement soit immédiat ou différé.

---

## 19.6 Indexes

Le Runtime peut construire des index temporaires afin d'accélérer :

- la recherche ;
- la résolution des identités ;
- les relations ;
- les Assets ;
- les composants.

Ces index ne sont jamais persistés.

Ils sont reconstruits à chaque création du Runtime.

---

## 19.7 Cache Strategy

Les caches sont considérés comme des optimisations.

Ils doivent toujours pouvoir être supprimés puis reconstruits sans perte d'information.

Le Project Model ne dépend jamais d'un cache.

---

## 19.8 Traversal Performance

Le parcours de la hiérarchie doit rester efficace, quelle que soit la taille du projet.

L'architecture doit permettre :

- les parcours en profondeur ;
- les parcours en largeur ;
- les recherches ciblées ;
- les parcours filtrés.

Les stratégies d'optimisation sont laissées à l'implémentation.

---

## 19.9 Validation Performance

La validation doit rester performante sur les projets de grande taille.

Le système peut utiliser :

- validation incrémentale ;
- index temporaires ;
- parallélisation ;
- caches de validation.

Le résultat obtenu doit rester strictement identique à celui d'une validation complète.

---

## 19.10 Serialization Performance

La sérialisation doit limiter les opérations inutiles.

L'architecture favorise :

- une écriture déterministe ;
- des modifications localisées ;
- une représentation stable ;
- la compatibilité avec les systèmes de contrôle de version.

Les performances ne doivent jamais compromettre la lisibilité des données persistées.

---

## 19.11 Runtime Build Performance

La construction du Runtime doit être optimisée sans modifier les responsabilités du Runtime Builder.

Les optimisations autorisées comprennent notamment :

- allocation groupée ;
- index pré-calculés ;
- résolution différée ;
- parallélisation lorsque cela est possible.

Le Runtime obtenu doit rester strictement identique.

---

## 19.12 Scalability

L'architecture doit permettre la gestion de projets de tailles très différentes.

Exemples :

- quelques objets ;
- plusieurs milliers d'objets ;
- bibliothèques d'Assets importantes ;
- projets comportant de nombreuses extensions.

La complexité du système doit rester maîtrisée.

---

## 19.13 Thread Safety

Le Project Model est considéré comme une structure cohérente.

Toute modification passe obligatoirement par une transaction.

Les traitements parallèles ne doivent jamais compromettre :

- la cohérence ;
- les identités ;
- les relations ;
- les invariants du modèle.

La stratégie de synchronisation sera définie lors de l'implémentation.

---

## 19.14 Profiling

L'architecture prévoit la possibilité de mesurer les performances du système.

Les outils de profilage pourront notamment mesurer :

- le temps de chargement ;
- le temps de validation ;
- le temps de construction du Runtime ;
- la consommation mémoire ;
- le temps de sérialisation.

Ces mesures ne modifient jamais le comportement du Project Model.

---

## 19.15 Performance Metrics

Les futures implémentations devront pouvoir mesurer notamment :

- durée de chargement ;
- durée de sauvegarde ;
- durée de validation ;
- durée de construction du Runtime ;
- nombre d'objets ;
- nombre de composants ;
- nombre de relations ;
- consommation mémoire.

Ces indicateurs serviront au suivi de l'évolution des performances.

---

## 19.16 UML Overview

Le modèle général peut être résumé ainsi.

```text
                Project Model

                      │

        ┌─────────────┼─────────────┐

        ▼             ▼             ▼

   Validation     Serialization   Runtime Builder

        │             │             │

        └─────────────┼─────────────┘

                      ▼

            Optimizations

        (Caches / Indexes / Lazy Loading)

                      ▼

             Runtime Performance
```

Les optimisations restent entièrement séparées des données persistantes.

---

## 19.17 Design Principles

L'architecture de performance repose sur les principes suivants :

- simplicité ;
- déterminisme ;
- séparation entre données et optimisations ;
- reconstruction systématique ;
- absence de dépendance aux caches ;
- évolutivité ;
- reproductibilité.

---

## 19.18 Performance Invariants

Les invariants suivants sont obligatoires.

Une optimisation ne doit jamais :

- modifier les données persistantes ;
- contourner la validation ;
- modifier les identités ;
- modifier les relations ;
- modifier les transactions ;
- modifier les règles métier.

Les optimisations demeurent toujours transparentes.

---

## 19.19 Future Optimizations

Les futures versions d'OPG pourront introduire :

- nouveaux index ;
- nouveaux caches ;
- nouvelles stratégies de chargement ;
- nouvelles optimisations mémoire ;
- nouvelles stratégies de parallélisation.

Ces évolutions devront respecter l'ensemble des principes définis dans cette spécification.

---

## 19.20 Summary

L'architecture de performance garantit que le Project Model peut évoluer vers des projets de grande taille tout en conservant un comportement déterministe, stable et indépendant des technologies.

Les optimisations sont considérées comme des détails d'implémentation et ne modifient jamais les règles fondamentales du système.


# 20. Complete UML Architecture

## 20.1 Overview

Ce chapitre présente une vue synthétique de l'architecture complète du Project Model.

Les diagrammes décrivent les relations entre les principaux sous-systèmes sans entrer dans les détails d'implémentation.

Ils constituent une référence de haut niveau permettant de comprendre rapidement l'organisation générale d'OPG.

---

## 20.2 Global Architecture

L'architecture complète du système peut être représentée de la manière suivante.

```text
                        Project Model
                     (Persistent Truth)

                              │

        ┌─────────────────────┼─────────────────────┐

        ▼                     ▼                     ▼

    Objects             Asset References      Metadata

        │                     │                     │

        ▼                     ▼                     ▼

   Components            Relationships       Extensions

                              │

                              ▼

                      Validation System

                              │

                              ▼

                     Transaction System

                              │

                              ▼

                     Serialization System

                              │

                              ▼

                     Versioning System

                              │

                              ▼

                     Runtime Builder

                              │

                              ▼

                          Runtime

                              │

                              ▼

                           Drivers

                              │

                              ▼

          Blender / USD / FBX / Future Technologies
```

Cette architecture illustre la séparation stricte entre :

- persistance ;
- exécution ;
- intégration technologique.

---

## 20.3 Layer Diagram

Les couches architecturales sont organisées comme suit.

```text
+--------------------------------------------------+
|                  User Interface                  |
+--------------------------------------------------+

+--------------------------------------------------+
|               Application Layer                  |
+--------------------------------------------------+

+--------------------------------------------------+
|                Project Model                     |
+--------------------------------------------------+

+--------------------------------------------------+
|              Runtime Builder                     |
+--------------------------------------------------+

+--------------------------------------------------+
|                  Runtime                         |
+--------------------------------------------------+

+--------------------------------------------------+
|                  Drivers                         |
+--------------------------------------------------+

+--------------------------------------------------+
|          External Technologies                   |
+--------------------------------------------------+
```

Chaque couche possède une responsabilité clairement définie.

---

## 20.4 Domain Model Diagram

Le Domain Model peut être résumé ainsi.

```text
Project

 │

 ├───────────────┐

 ▼               ▼

Objects       Assets

 │

 ▼

Components

 │

 ▼

Metadata

 │

 ▼

Relationships

 │

 ▼

Extensions
```

Le Project constitue l'unique Aggregate Root.

---

## 20.5 Object Hierarchy Diagram

```text
Project

 │

 ├───────────────┐

 ▼               ▼

Object A     Object B

 │

 ├───────────┐

 ▼           ▼

Object C   Object D
```

La hiérarchie représente uniquement les relations de propriété.

---

## 20.6 Identity Diagram

```text
Project

 │

 ▼

Object

 │

 ▼

UUID

 │

 ▼

Relationships
```

Toutes les références utilisent exclusivement les identités persistantes.

---

## 20.7 Component Diagram

```text
Project Object

 │

 ├──────────────┐

 ▼              ▼

Transform   Material

 │

 ▼

Metadata
```

Les capacités d'un objet sont obtenues par composition.

---

## 20.8 Runtime Integration Diagram

```text
Project Model

      │

      ▼

Validation

      │

      ▼

Runtime Builder

      │

      ▼

Runtime Graph

      │

      ▼

Runtime Services

      │

      ▼

Runtime
```

Le Runtime est entièrement reconstruit.

---

## 20.9 Driver Integration Diagram

```text
Runtime

 │

 ├──────────────┐

 ▼              ▼

Blender      USD

 │              │

 ▼              ▼

Scene      Scene
```

Les Drivers implémentent tous le même contrat.

---

## 20.10 Transaction Flow Diagram

```text
User Action

      │

      ▼

Transaction

      │

      ▼

Validation

      │

      ▼

Commit

      │

      ▼

Project Model

      │

      ▼

Runtime Synchronization
```

Toutes les modifications suivent ce flux.

---

## 20.11 Serialization Diagram

```text
Project Model

      │

      ▼

Serialization

      │

      ▼

Persistent File

      │

      ▼

Deserialization

      │

      ▼

Project Model

      │

      ▼

Runtime Builder
```

Le Runtime n'est jamais sérialisé.

---

## 20.12 Validation Diagram

```text
Project Model

      │

      ▼

Validation Engine

 │

 ├──────────────┐

 ▼              ▼

Structure    Semantics

 │

 ▼

Validation Report
```

La validation précède toujours la construction du Runtime.

---

## 20.13 Extension Diagram

```text
Core

 │

 ├──────────────┬──────────────┐

 ▼              ▼              ▼

Components   Drivers     Validators

 │

 ▼

Extensions
```

Le Core reste indépendant des extensions.

---

## 20.14 Architectural Rules

Les diagrammes précédents illustrent les règles fondamentales suivantes :

- un seul Project Model persistant ;
- un seul Runtime reconstruit ;
- des Drivers interchangeables ;
- des Extensions isolées ;
- une validation obligatoire ;
- une sérialisation déterministe ;
- une séparation stricte des responsabilités.

---

## 20.15 Summary

Les diagrammes UML présentés dans ce chapitre synthétisent l'ensemble de l'architecture du Project Model.

Ils constituent une vue de référence destinée aux architectes, aux développeurs du Runtime, aux développeurs de Drivers et aux auteurs de plugins.

Les chapitres précédents demeurent la référence normative pour les règles détaillées de chaque sous-système.


# 21. Implementation Roadmap

## 21.1 Overview

Cette feuille de route décrit le découpage officiel de l'implémentation du Project Model.

Chaque ticket représente une unité de développement autonome, testable et intégrable.

L'ordre présenté ci-dessous constitue la séquence officielle de réalisation.

Aucune implémentation ne doit être réalisée en dehors de cette feuille de route sans révision préalable de l'architecture.

---

## 21.2 Development Principles

L'implémentation du Project Model suit les principes suivants :

- un ticket par fonctionnalité ;
- aucune implémentation partielle ;
- architecture validée avant le code ;
- couverture de tests obligatoire ;
- intégration continue après chaque ticket ;
- aucune régression autorisée.

Chaque ticket doit être terminé avant le suivant.

---

## 21.3 Phase 1 — Project Foundation

Cette première phase met en place les fondations du Project Model.

| Ticket | Description |
|---------|-------------|
| M-004-001 | Project Skeleton |
| M-004-002 | Project Core |
| M-004-003 | Object Base |
| M-004-004 | Object Collection |
| M-004-005 | Root Object |
| M-004-006 | Hierarchy Management |

---

## 21.4 Phase 2 — Identity & Relationships

Cette phase introduit les mécanismes d'identification et de liaison.

| Ticket | Description |
|---------|-------------|
| M-004-007 | Identity System |
| M-004-008 | UUID Management |
| M-004-009 | Relationship System |
| M-004-010 | Reference Resolution |
| M-004-011 | Ownership Rules |

---

## 21.5 Phase 3 — Components

Cette phase met en place le modèle de composition.

| Ticket | Description |
|---------|-------------|
| M-004-012 | Component Base |
| M-004-013 | Component Collection |
| M-004-014 | Component Registry |
| M-004-015 | Built-in Components |
| M-004-016 | Custom Components |

---

## 21.6 Phase 4 — Metadata & Assets

Cette phase introduit les systèmes descriptifs.

| Ticket | Description |
|---------|-------------|
| M-004-017 | Metadata System |
| M-004-018 | Metadata Registry |
| M-004-019 | Asset References |
| M-004-020 | Asset Resolution |
| M-004-021 | Asset Validation |

---

## 21.7 Phase 5 — Persistence

Cette phase implémente les mécanismes de sauvegarde.

| Ticket | Description |
|---------|-------------|
| M-004-022 | Serialization Core |
| M-004-023 | Deserialization |
| M-004-024 | Schema Versioning |
| M-004-025 | Migration Pipeline |
| M-004-026 | Persistence Tests |

---

## 21.8 Phase 6 — Validation

Cette phase garantit l'intégrité du Project Model.

| Ticket | Description |
|---------|-------------|
| M-004-027 | Validation Core |
| M-004-028 | Structural Validation |
| M-004-029 | Semantic Validation |
| M-004-030 | Validation Reports |

---

## 21.9 Phase 7 — Transactions

Cette phase met en place le système officiel de modification.

| Ticket | Description |
|---------|-------------|
| M-004-031 | Transaction Core |
| M-004-032 | Transaction Manager |
| M-004-033 | Undo Preparation |
| M-004-034 | Redo Preparation |
| M-004-035 | Transaction History |

---

## 21.10 Phase 8 — Runtime Integration

Cette phase relie M-004 au Runtime M-003.

| Ticket | Description |
|---------|-------------|
| M-004-036 | Runtime Builder Integration |
| M-004-037 | Runtime Mapping |
| M-004-038 | Runtime Synchronization |
| M-004-039 | Runtime Update Pipeline |

---

## 21.11 Phase 9 — Driver Integration

Cette phase prépare les technologies externes.

| Ticket | Description |
|---------|-------------|
| M-004-040 | Driver Interfaces |
| M-004-041 | Driver Synchronization |
| M-004-042 | Driver Mapping |
| M-004-043 | Driver Validation |

---

## 21.12 Phase 10 — Extensions

Cette phase ouvre officiellement le système aux plugins.

| Ticket | Description |
|---------|-------------|
| M-004-044 | Extension Registry |
| M-004-045 | Extension Serialization |
| M-004-046 | Extension Validation |
| M-004-047 | Extension Lifecycle |

---

## 21.13 Phase 11 — Optimization

Cette phase améliore les performances.

| Ticket | Description |
|---------|-------------|
| M-004-048 | Index System |
| M-004-049 | Lazy Loading |
| M-004-050 | Cache Layer |
| M-004-051 | Performance Improvements |

---

## 21.14 Phase 12 — Finalization

Cette dernière phase stabilise complètement le Project Model.

| Ticket | Description |
|---------|-------------|
| M-004-052 | Documentation Alignment |
| M-004-053 | Architecture Review |
| M-004-054 | Integration Tests |
| M-004-055 | Final Validation |
| M-004-056 | Project Model Complete |

---

## 21.15 Testing Strategy

Chaque ticket suit obligatoirement le cycle suivant :

1. Implémentation.
2. Tests unitaires.
3. Tests d'intégration.
4. Validation architecturale.
5. Revue de code.
6. Fusion dans la branche principale.

Aucun ticket incomplet ne peut être fusionné.

---

## 21.16 Repository Workflow

Chaque ticket suit le workflow officiel du dépôt.

```text
feature/M-004-XXX

        │

        ▼

Implementation

        │

        ▼

Pytest

        │

        ▼

Commit

        │

        ▼

Push

        │

        ▼

Pull Request

        │

        ▼

Merge

        │

        ▼

Main
```

Ce processus garantit une intégration continue stable.

---

## 21.17 Completion Criteria

La série M-004 est considérée comme terminée lorsque :

- tous les tickets sont implémentés ;
- tous les tests passent ;
- la documentation est synchronisée ;
- les validations sont satisfaites ;
- le Runtime fonctionne intégralement avec le nouveau Project Model.

---

## 21.18 Final Statement

Le présent document constitue la spécification officielle du Project Model d'OPG v3.

Il fait autorité sur toute implémentation future de la série M-004.

Toute évolution du Project Model devra être conforme aux principes, règles et architectures définis dans cette documentation.

Cette spécification devient la **Single Source of Truth** pour l'ensemble du développement du Project Model.