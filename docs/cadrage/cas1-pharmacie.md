# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
La détection automatique les infomations manquantes dans une ordonnance.

## Utilisateur final (obligatoire)
les pharmaciens et préparateurs en pharmacie qui vérifient la complétude des ordonnances.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
(a)Les champs obligatoires sont connus à l'avance et ne nécissitent pas les données étiquetées.
(b)Les régles permettent de vérifier pourquoi l'ordonnance est incompléte et qui est important dans un contexte.
(d) une erreur peut avoir des conséquences importantes.

## Données nécessaires et leur origine (obligatoire)
Les ordonnances contenant les informations à vérifier, comme l'identité du patient, la date, et  le médicament .

## Métrique de succès et seuil d'acceptation (obligatoire)
Taux de détection correcte des ordonnances incomplètes sur un jeu de test ; acceptation à partir de 95 %.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une information manquante non détectée peut entraîner une délivrance inappropriée ; le pharmacien vérifie donc systématiquement le résultat avant toute validation de l'ordonnance.

## Risques éthiques ou de confidentialité (obligatoire)
Les ordonnances contiennent des données de santé : accès limité aux personnes autorisées, anonymisation pour les tests et stockage sécurisé des données.

## Approche écartée et pourquoi (facultatif)

