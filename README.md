# A MINIMAL WORKING SETUP OF A SIMPLE CI/CD SECURITY PIPELINE
The goal is to implement a simple and automated CI/CD security pipeline that runs on every code change, performs security checks, and makes results clearlyvvisible and actionable in a separate dashboard.

# Platform Used
GitHub (Web)
GitHub Actions
GitHub CodeQL (SAST)

# Implementation

# 1. Source Code Repository
Create a GitHub repository containing a minimal Python application.
Add a requirements.txt file to define dependencies.

# 2. CI/CD Automation with GitHub Actions
Add a GitHub Actions workflow in .github/workflows/.
The workflow runs automatically on every push to main.

# 3. Security Integration (SAST)
Integrate a CodeQL for Static Application Security Testing.

# 4. Results Visibility & Actionability
Security findings are published to GitHub’s Security à Code scanning dashboard.

CodeQL scans your .yml workflow file and it may notic that it has too many permissions which could be risky if someone else modifies it.
Try to fix this by tightening the permissions which are only needed and clear the alert on the next run.

# SUMMARY
Whenever code is pushed, GitHub Actions automatically builds the app and runs static security analysis using CodeQL. Findings are published to GitHub’s Security dashboard, where developers can see severity, affected files, and remediation guidance.
