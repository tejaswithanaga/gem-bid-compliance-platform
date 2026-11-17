# AI-Powered Integrated Bid Compliance Verification Platform

## Overview

The **AI-Powered Integrated Bid Compliance Verification Platform** is a student demonstration project designed to help users verify bid compliance through a checklist and generate a compliance summary.

Users can enter a tender or bid title, check important compliance requirements, and view an overall compliance percentage and verification status.

This project currently uses a **rule-based checklist verification approach**. It is an educational prototype and does not perform automatic AI-based document analysis.

## Features

- Enter a tender or bid title.
- Verify technical specifications.
- Check warranty information.
- Verify the delivery period.
- Confirm the price quote.
- Check required seller documents.
- Generate a compliance report with a percentage score.
- Display the verification status of each checklist item.
- Run automated tests using Pytest.
- Build and deploy the application using Docker.
- Automate the build, testing, and deployment process using Jenkins CI/CD.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Testing | Pytest |
| Containerization | Docker |
| Container Management | Docker Compose |
| CI/CD | Jenkins |
| Version Control | Git and GitHub |

## Project Structure

```text
gem-bid-compliance-platform/
│
├── backend/
│   ├── app.py
│   ├── verification.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_verification.py
│
├── frontend/
│   ├── index.html
│   ├── default.conf
│   └── Dockerfile
│
├── docker-compose.yml
├── Jenkinsfile
├── README.md
└── .gitignore
```

## Application Workflow

1. The user enters the tender or bid title.
2. The user selects the compliance checklist items.
3. The frontend sends the selected checklist information to the Flask backend.
4. The backend processes the information using the verification module.
5. The system calculates the compliance percentage.
6. The application displays the verification status and compliance summary.

## Compliance Checklist

The application checks the following five requirements:

1. Technical Specifications
2. Warranty Information
3. Delivery Period
4. Price Quote
5. Seller Documents

The compliance percentage is calculated based on the number of completed checklist items.

**Example:** If 4 out of 5 checklist items are completed:

Compliance Score = (4 / 5) × 100 = 80%

## How to Run the Application

### Prerequisites

- Docker Desktop
- Git
- A web browser

### Steps

1. Clone the repository:

```bash
git clone https://github.com/tejaswithanaga/gem-bid-compliance-platform.git
```

2. Open the project directory:

```bash
cd gem-bid-compliance-platform
```

3. Build and start the application:

```bash
docker compose up --build -d
```

4. Open the application in your browser:

```text
http://localhost:8080
```

### Stop the Application

```bash
docker compose down
```

## Automated Testing

The backend verification module is tested using Pytest.

Run the following command while the backend container is running:

```bash
docker compose exec backend python -m pytest -v
```

The test cases cover:

- All checklist items compliant.
- Partially compliant checklist.
- No checklist items compliant.
- Missing checklist information.
- Invalid checklist information.

**Latest test result:** All 5 automated test cases passed.

## Jenkins CI/CD Pipeline

The project uses Jenkins to automate the build, testing, and deployment process.

The pipeline contains the following stages:

1. **Checkout:** Retrieves the source code from the GitHub repository.
2. **Build:** Builds the backend and frontend Docker images.
3. **Test:** Executes automated Pytest test cases.
4. **Deploy:** Deploys the application using Docker Compose.

### Pipeline Configuration

- Repository: `https://github.com/tejaswithanaga/gem-bid-compliance-platform.git`
- Branch: `feature/code-quality-review`
- Pipeline script: `Jenkinsfile`

The Jenkins pipeline was executed successfully, with all five tests passing and both application containers starting successfully.

### GitHub Webhook Integration

A GitHub webhook can be configured to notify Jenkins whenever new changes are pushed to the repository.

To enable automatic pipeline triggering:

1. Open the GitHub repository.
2. Navigate to **Settings → Webhooks**.
3. Add the Jenkins webhook endpoint.
4. Select the push event.
5. Save the webhook configuration.
6. Enable the appropriate GitHub push trigger in the Jenkins job.
7. Push a new commit and verify that Jenkins starts a build.

The webhook configuration and trigger should be tested separately to confirm automatic execution.

## Repository

GitHub Repository:

https://github.com/tejaswithanaga/gem-bid-compliance-platform

## Future Enhancements

- Add downloadable compliance reports.
- Improve validation messages.
- Integrate AI-based document analysis.
- Add more comprehensive verification test cases.
- Introduce user authentication and role-based access.
- Improve the compliance dashboard.

## Disclaimer

This is an educational prototype. It does not connect to the Government e-Marketplace (GeM), perform official GeM verification, or replace official compliance checks or professional procurement review.
