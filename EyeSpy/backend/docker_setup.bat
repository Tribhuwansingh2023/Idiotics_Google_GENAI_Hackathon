@echo off
echo EyeSpy Docker Setup
echo ==================

echo Checking if Docker is installed...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Docker not found! Please install Docker Desktop:
    echo https://www.docker.com/products/docker-desktop/
    echo.
    echo After installation, run this script again.
    pause
    exit /b 1
)

echo Docker found! Starting MongoDB container...
docker run -d --name eyespy-mongo -p 27017:27017 mongo:latest

echo Waiting for MongoDB to start...
timeout /t 5 /nobreak >nul

echo Setting up database...
python setup_database.py

echo Starting EyeSpy server...
python app.py

pause