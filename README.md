# Slovensko v Habsburskej monarchii (16. – 18. storočie)

Interaktívny vzdelávací web so 7 tematickými podstránkami a vedomostným kvízom (20 otázok).
Obsah vychádza výhradne zo študijného materiálu „Slovensko v Habsburskej monarchii v 16. – 18. storočí“,
fotografie pochádzajú z Wikimedia Commons (zoznam s autormi a licenciami je na stránke *Zdroje*).

## Štruktúra
- `site/` – hotová statická stránka (HTML, CSS, JS)
- `build/` – Python skript, ktorý generuje HTML stránky z obsahu (`content.py`, `quiz.py`, `images.py`)
- `.github/workflows/pages.yml` – pri každom pushi do `main` zostaví web a publikuje ho do vetvy `gh-pages` (GitHub Pages)

## Lokálne spustenie
```bash
python build/build.py
cd site && python -m http.server 8000
```
