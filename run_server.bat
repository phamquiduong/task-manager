@echo off

echo ----------------------------------------------------
echo             Install all pip packages
echo ----------------------------------------------------
pip install -r requirements.txt

cd src

echo ----------------------------------------------------
echo                   Run migrate
echo ----------------------------------------------------
python manage.py migrate

echo ----------------------------------------------------
echo                    Run server
echo ----------------------------------------------------
set /p port="Please Input Server Port (default 80): "

if "%port%"=="" (
    set port=80
)

python manage.py runserver 0.0.0.0:%port%
