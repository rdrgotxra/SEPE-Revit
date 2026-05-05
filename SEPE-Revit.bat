@echo off

echo Instalando extensão SEPE-Revit...
pyrevit clone clone_pyrevit core
if %errorlevel% neq 0 exit /b

pyrevit attach clone_pyrevit default --installed
if %errorlevel% neq 0 exit /b

pyrevit extend ui SEPE-Revit https://github.com/rdrgotxra/SEPE-Revit.git --branch main
if %errorlevel% neq 0 exit /b

echo SEPE-Revit instalado! Bons projetos!
pause