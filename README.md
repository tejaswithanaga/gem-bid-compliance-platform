# AI-Powered Integrated Bid Compliance Verification Platform

## Overview
A student demonstration project that helps users verify bid compliance using a checklist and generates a compliance summary.

## Features
- Enter a tender or bid title.
- Verify technical specifications.
- Check warranty information.
- Verify the delivery period.
- Confirm the price quote.
- Check required seller documents.
- Generate a compliance report with a percentage score.
- Display the verification status of each checklist item.

## Technology Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python and Flask
- **Deployment:** Docker and Docker Compose

## Project Structure
```text
gem-bid-compliance-platform/
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── default.conf
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## How to Run
1. Install Docker Desktop.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   docker compose up --build -d
   ```

4. Open `http://localhost:8080` in your browser.

## Disclaimer
This is an educational prototype. It does not connect to the Government e-Marketplace (GeM) or replace official compliance checks or professional procurement review.

## Future Enhancements
- Add downloadable compliance reports.
- Improve validation messages.
- Add automated testing for checklist verification.
CI/CD pipeline automatic trigger test
