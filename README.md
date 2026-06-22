# LinkedinGamesSolver
Python scripts to solve the LinkedIn games automatically.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/ARM4da/LinkedinGamesSolver.git
cd LinkedinGamesSolver
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Run
```bash
python main.py
```

## Project structure
```
LinkedinGamesSolver/
├── main.py                             # Entry point
├── core/
│   └── gamesScraper.py                 # Generic HTML scraper
└── games/
    └── sudoku/
        ├── numbersCollectorSudoku.py   # Grid extractor
        └── solverSudoku.py             # Backtracking solver
```