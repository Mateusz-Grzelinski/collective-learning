# Collective learning

Projekt na przedmiot `Modelowanie i symulacja systemów`, semestr 5.

## Latex - kopilacja

Potrzebne pakiety do kompilacji (linux manjaro, arch):

```bash
sudo pacman -S texlive-core texlive-bin texlive-science texlive-latexextra
```

## Opis

Praca ma na celu pokazanie rozprzestrzeniania się wiedzy w społeczeństwie w
różnych hierarchiach zarządzania i jak ona wpływa na efektywność jednostek.

Symulacja składa się ze środowiska i zasobów, w którym są umieszczani są agenci.
### Idealistyczny model do rozważenia
- N agentów w sieci G
- Agenci mają jeden cel, jest nim budowa modelu z obserwacji
- Istnieje model który nie będzie sprzeczny z jakąkolwiek informacją uzyskaną przez obserwacje
- Każdy agent umie się uczyć to znaczy zaktualizować model, by nie był sprzeczny z obserwacjami o których wie
- Interakcja między agentami polega na zapytaniach gdzie a1 proponuje a2 pewien model a - -następnie czeka na kontrargumenty ze strony a2 , które przeczą temu modelowi
- Agenci dają poprawne odpowiedzi na zapytania
- W dowolnym momencie agent może dostać nowe informacje
- W każdym momencie jest zbiór niezależnych, równoczesnych komunikacji

### Agent

-   jego celem jest zbieranie zasobu
-   zna położenie magazynu zasobu
-   wybiera drogę na podstawie posiadanej wiedzy
-   dzieli się wiedzą z innymi agentami
-   posiada pewien stopień przysfajalności wiedzy

### Wiedza

-   traktowana w sposób ciągły lub dyskretny (?)
-   może być trawała (dostępna po śmierci agenta) lub nietrwała (ginie wraz z agentem)
-   może być fałszywa (?) raczej bez tego

### Dzielenie się wiedzą

-   agent z agentem
-   agent -> medium trwałe -> agent
-   agent -> 'social media' -> wszyscy agenci - metoda natychmiastowej komunikacji
-   agent otrzymuje wiedzę pewną część wiedzy w procesie uczenia, ta wiedza jest
    zależna od jego stopnia przysfajalności wiedzy
-   transfer wiedzy jest obciążony błędem i kosztem (?)

### Model 1 - pszczółki w ulu

-   populacja turkusowa
-   przekazanie wiedzy agent z agentem
-   brak medium trwałego do zapisania wiedzy
-   wiedza najnowsza jest najlepsza (?)

## Linki

Zbiór przydatnych linków i referencji

### Referencje

-   [eksperyment setnej małpy](https://www.odkrywamyzakryte.com/efekt-setnej-malpy) - wiedza zdobyta
    przez jednostkę przechodzi na cały gatunek (należy traktować jako przykład,
    nie twierdzenie)
-   [eksperyment więzienny](https://pl.wikipedia.org/wiki/Eksperyment_wi%C4%99zienny) - jak
    zachowuje się człowiek, jeśli ma władzę nad drugim, również odwrotnie
    (należy traktować jako przykład, nie twierdzenie)
-   [Turkusowe zarządzanie](http://nagrajbiznes.tv/jakim-kolorem-jestes-frederic-laloux-i-barwy-organizacji/) -
    opisanie hierarchii firmy (społecznośći) za pomocą kolorów

### Papiery naukowe

-   [Learning by doing](https://www.sciencedirect.com/science/article/pii/S1474667015376382) -
    jak reprezentować poziom wiedzy w populacji
