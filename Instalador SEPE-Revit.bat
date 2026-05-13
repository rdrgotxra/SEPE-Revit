@echo off
chcp 65001 >nul

title Instalador SEPE-Revit

echo.
echo    ███████╗███████╗██████╗ ███████╗
echo    ██╔════╝██╔════╝██╔══██╗██╔════╝
echo    ███████╗█████╗  ██████╔╝█████╗
echo    ╚════██║██╔══╝  ██╔═══╝ ██╔══╝
echo    ███████║███████╗██║     ███████╗
echo    ╚══════╝╚══════╝╚═╝     ╚══════╝
echo.
echo    [94m------ C É L U L A  B I M ------[0m
echo.

set "INSTALLER=pyRevit_6.4.0.26100_signed.exe"

set "EXT_PATH="
set "PATH1=%USERPROFILE%\DC\ACCDocs\SEPE\BIBLIOTECA\Project Files\REVIT\PYREVIT"
set "PATH2=%USERPROFILE%\Autodesk Docs\SEPE\BIBLIOTECA\Project Files\REVIT\PYREVIT"
set "PATH3=%USERPROFILE%\Documents\SEPE-Revit\PYREVIT"
set "PATH4=%~dp0SEPE-Revit"

where pyrevit >nul 2>nul

if errorlevel 1 (

    echo.
    echo Instalando pyRevit...

    if not exist "%~dp0%INSTALLER%" (
        echo.
        echo Instalador não encontrado:
        echo.
        echo %~dp0%INSTALLER%
        echo.
        pause
        exit /b 1
    )

    start /wait "" "%~dp0%INSTALLER%"

    call refreshenv >nul 2>nul

    where pyrevit >nul 2>nul

    timeout /t 5 /nobreak >nul
    if errorlevel 1 (
        echo.
        echo pyRevit não foi encontrado após a instalação.
        echo Reinicie o terminal e tente novamente.
        echo.
        pause
        exit /b 1
    )

    pyrevit extensions disable pyRevitTools >nul 2>nul

)

if exist "%PATH1%" set "EXT_PATH=%PATH1%"
if exist "%PATH2%" set "EXT_PATH=%PATH2%"
if exist "%PATH3%" set "EXT_PATH=%PATH3%"
if exist "%PATH4%" set "EXT_PATH=%PATH4%"

if "%EXT_PATH%"=="" (

    echo Pasta da extensão não encontrada.
    echo.
    echo Locais verificados:
    echo.
    echo %PATH1%
    echo %PATH2%
    echo %PATH3%
    echo %PATH4%
    echo.
    pause
    exit /b 1

)

echo Registrando extensão no pyRevit...

pyrevit extensions paths add "%EXT_PATH%" >nul 2>nul

if errorlevel 1 (
    echo Falha no registro da extensão.
)

echo Associando pyRevit às versões do Revit...

pyrevit attach default >nul 2>nul

if errorlevel 1 (
    echo Falha na associação do pyRevit ao Revit.
)

echo [93mInstalação concluída! Bons projetos![0m
echo.

pause
