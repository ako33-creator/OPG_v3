# OPG v3 — Git Workflow

Version : 1.0

---

# Objectif

Git est le système officiel de gestion de versions du projet OPG v3.

Chaque modification du projet doit pouvoir être :

- identifiée ;
- tracée ;
- restaurée ;
- documentée.

---

# Single Source of Truth

Le développement est effectué exclusivement dans :

```
SRC/
```

Les dossiers suivants ne sont pas considérés comme source de vérité :

```
incoming/
releases/
backups/
```

---

# Workflow officiel

Chaque Milestone suit obligatoirement le cycle suivant.

```
Développement
        ↓
Tests
        ↓
Nettoyage
        ↓
git status
        ↓
git add
        ↓
git commit
        ↓
Git Tag
        ↓
Release Notes
        ↓
Patch
        ↓
Validation
```

---

# Vérification

Toujours commencer par :

```bash
git status
```

Le dépôt doit être propre.

---

# Ajout des fichiers

```bash
git add .
```

---

# Création d'un commit

```bash
git commit -m "M-XXX Description"
```

Exemple :

```bash
git commit -m "M-002 Core Foundation"
```

---

# Création d'un tag

```bash
git tag v3.0.0-m002
```

---

# Vérification des tags

```bash
git tag
```

---

# Release Notes

Chaque Milestone possède un document :

```
docs/Releases/
```

Format :

```
M-001-Core-Bootstrap.md
M-002-Core-Foundation.md
```

---

# Scripts d'ingénierie

Tous les scripts de maintenance sont placés dans :

```
tools/
```

Exemples :

```
cleanup_copies.ps1
create_release.ps1
create_patch.ps1
backup_project.ps1
git_tag.ps1
update_changelog.ps1
```

---

# Règles

Ne jamais modifier directement un patch.

Ne jamais développer dans incoming.

Ne jamais développer dans releases.

Toujours développer dans SRC.

---

# Fin de Milestone

Avant validation :

- Tests réussis
- Dépôt Git propre
- Commit créé
- Tag créé
- Release Notes rédigées
- Patch généré
- Validation officielle