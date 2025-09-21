# Selenium Test Automation Project

This project contains automated tests for the Events UAT application using Selenium WebDriver and Python.

## Project Structure
```
Tests/
├── tests/                  # Test files
├── pages/                  # Page Object Model classes
├── utils/                  # Utility functions and helpers
├── reports/               # Test reports and screenshots
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore rules
```

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Tests
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

### Single test:
```bash
python tests/first_test.py
```

### With pytest:
```bash
pytest tests/ -v
```

### Generate HTML report:
```bash
pytest tests/ --html=reports/report.html
```

## Browser Support
- Chrome (default)
- Brave Browser (configured)
- Firefox (configurable)

## Test Data
- Username: TestGrace
- Password: pagamio123
- Application URL: https://events-uat.pagamio.tech/

## Contributing
1. Create a feature branch
2. Make your changes
3. Add tests for new features
4. Submit a pull request