# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Répondre automatiquement aux questions des étudiants et du personnel sur le règlement intérieur en s'appuyant sur les documents officiels de l'école.

## Utilisateur final (obligatoire)
Les étudiants et le personnel de l'école, qui souhaitent obtenir rapidement une information concernant le règlement intérieur.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
(b)Le RAG permet de retrouver les passages des documents utilisés pour produire la réponse, ce qui facilite sa vérification. (a) Des questions étiquetées ne sont pas nécessaires pour commencer puisque les documents officiels constituent directement la source d'information.

## Données nécessaires et leur origine (obligatoire)
Les versions officielles du règlement intérieur et les autres documents réglementaires de l'école, fournis par l'administration.

## Métrique de succès et seuil d'acceptation (obligatoire)
Taux de réponses correctement justifiées par un passage pertinent du règlement ; acceptation à partir de 90 % sur un jeu de questions de test.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une réponse incorrecte peut induire un étudiant en erreur sur ses obligations ; les réponses doivent citer leur source et les cas sensibles doivent être vérifiés auprès de l'administration

## Risques éthiques ou de confidentialité (obligatoire)
Le système doit utiliser uniquement les documents officiels et éviter de divulguer des informations personnelles ou des documents accessibles uniquement à certains utilisateurs.

## Approche écartée et pourquoi (facultatif)

