@echo off
echo Starting EyeSpy with MongoDB Integration...
echo.

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setting up database...
python setup_database.py

echo.
echo Starting Flask server...
python app.py

pause