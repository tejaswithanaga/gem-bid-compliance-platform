SIH26100 — BID COMPLIANCE VERIFICATION DEMO
Frontend: HTML/CSS/JavaScript served by Nginx
Backend: Python Flask API
Containerization: Docker Compose

IMPORTANT: This is a student demonstration only. It is not connected to GeM, does not use a real AI model, and does not provide official procurement compliance advice.

RUN IT
1. Install Docker Desktop and start it. Wait until Docker Engine is running.
2. Extract this ZIP file.
3. Open the extracted folder in File Explorer, click the address bar, type cmd, and press Enter.
4. Build and start both containers:
   docker compose up --build -d
5. Open this URL in your browser:
   http://localhost:8080
6. Enter a tender/bid title and tick checklist items.
7. Click Verify Sample Bid. The Flask backend returns a percentage and a checklist report.

CHECK / STOP
Check containers:
   docker compose ps
View logs:
   docker compose logs
Stop and remove containers:
   docker compose down

TO CHANGE THE FRONTEND
Edit frontend/index.html, save, then rebuild:
   docker compose up --build -d

SAMPLE OUTPUT
Compliance score: 80%
Status: Partially compliant
Checklist items passed: 4 of 5
The exact output depends on which boxes you tick.

TROUBLESHOOTING
- If Docker Desktop asks for WSL, open PowerShell as Administrator and run: wsl --install
  Restart Windows if requested, then start Docker Desktop.
- If port 8080 is already in use, change "8080:80" in docker-compose.yml to "8081:80", then rebuild and open http://localhost:8081.
- To run the whole application, keep Docker Desktop running.
