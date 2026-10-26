# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Identifier et prioriser automatiquement les avis négatifs afin de permettre au service client de traiter rapidement les retours nécessitant une attention particulière.

## Utilisateur final (obligatoire)
Les agents du service client et les responsables du site e-commerce, qui souhaitent identifier rapidement les avis négatifs.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
(a) Les milliers d'avis disponibles peuvent être étiquetés afin de constituer un jeu de données pour entraîner un classifieur. (c) Un modèle de classification peut traiter un grand volume d'avis à faible coût par requête. (d) Un avis mal classé peut être corrigé par un agent du service client, ce qui limite la conséquence de l'erreur.

## Données nécessaires et leur origine (obligatoire)
Un ensemble d'avis clients contenant le texte de l'avis et une étiquette indiquant son sentiment, obtenu à partir des avis historiques et d'un étiquetage réalisé par des agents.

## Métrique de succès et seuil d'acceptation (obligatoire)
F1 macro sur un jeu de test indépendant ; acceptation à partir de 0,85, avec un rappel d'au moins 0,90 pour la classe négative.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Un avis négatif mal classé peut retarder sa prise en charge ; les agents peuvent vérifier les avis prioritaires et corriger les erreurs de classification.

## Risques éthiques ou de confidentialité (obligatoire)
Les avis peuvent contenir des informations personnelles ; les données doivent être anonymisées lorsque cela est nécessaire et leur accès limité aux personnes autorisées.

## Approche écartée et pourquoi (facultatif)

