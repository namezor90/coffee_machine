# ☕ Virtual Coffee Machine

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Virtuális kávéautomata szimulátor, amely kezeli az alapanyagokat, pénzérmeket és kávékészítést.

## ✨ Jellemzők

- 🍵 3 kávétípus (espresso, latte, cappuccino)
- 💰 Érme kezelés (quarter, dime, nickel, penny)
- 📊 Készletnyilvántartás
- 💱 Visszajáró számítás
- 📈 Erőforrás jelentések

## 🚀 Telepítés

```bash
git clone https://github.com/namezor90/coffee_machine.git
cd coffee-machine
python main.py
```

## 💻 Használat

1. Indítsd el a programot
2. Válassz kávétípust:
   - `espresso` ($1.50)
   - `latte` ($2.50)
   - `cappuccino` ($3.00)
3. Helyezd be az érméket
4. További parancsok:
   - `report1` - alapanyag készlet
   - `report2` - érme készlet
   - `off` - kikapcsolás

## 📁 Projekt Struktúra

```
coffee-machine/
└── main.py    # Teljes program logika
```

## 🛠️ Fejlesztés

Új kávétípus hozzáadása a `MENU` szótárhoz:

```python
"new_coffee": {
    "ingredients": {
        "water": 100,
        "milk": 50,
        "coffee": 20,
    },
    "cost": 2.0,
}
```

## 📝 Licensz

[MIT](LICENSE)

## 🤝 Közreműködés

1. Fork-old a projektet
2. Hozz létre egy új branch-et (`git checkout -b feature/awesome`)
3. Commit-old a változtatásokat (`git commit -m 'Add awesome feature'`)
4. Push-old a branch-et (`git push origin feature/awesome`)
5. Nyiss egy Pull Request-et

## 👥 Szerzők

- [@namezor90](https://github.com/namezor90)

## 🏷️ Verziótörténet

- 1.0.0
  - Alap funkcionalitás
  - 3 kávétípus
  - Érme kezelés
  - Készletjelentések
