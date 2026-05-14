@echo off
setlocal
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

set INSTALLER=%USERPROFILE%\DC\ACCDocs\SEPE\BIBLIOTECA\Project Files\REVIT\PYREVIT\pyRevit_CLI_6.4.0.26100_signed.exe
set CLONE_NAME=SEPE-Revit
set EXT_NAME=SEPE-Revit
set EXT_URL=https://github.com/rdrgotxra/SEPE-Revit.git

pyrevit clones >nul 2>nul

if errorlevel 1 (
    echo Instalando pyRevit...

    if not exist "%~dp0%INSTALLER%" (
        echo Instalador não encontrado:
        echo %~dp0%INSTALLER%
        pause
        exit /b 1
    )

    start /wait "" "%~dp0%INSTALLER%"
    timeout /t 5 /nobreak >nul

    echo Verificando instalação do pyRevit...
    pyrevit clones >nul 2>nul

    if errorlevel 1 (
        echo pyRevit ainda não foi encontrado.
        echo Feche a janela e tente novamente.
        pause
        exit /b 1
    )
)

pyrevit clones | findstr /i /c:"%CLONE_NAME%" >nul

if errorlevel 1 (
    echo Criando clone pyRevit...
    pyrevit clone "%CLONE_NAME%" core --debug

    if errorlevel 1 (
        echo Falha ao criar clone.
        pause
        exit /b 1
    )
)

echo Conectando clone Revit...
pyrevit attach "%CLONE_NAME%" default --installed >nul 2>nul

if errorlevel 1 (
    echo Falha ao executar attach.
    pause
    exit /b 1
)

echo Instalando extensão %EXT_NAME%...
pyrevit extend ui "%EXT_NAME%" "%EXT_URL%" --branch=main >nul 2>nul

if errorlevel 1 (
    echo Falha na instalação da extensão. Continuando...
)

echo.
echo [93mInstalação concluída![0m
echo [93mBons Projetos! :)[0m
echo.

pause
