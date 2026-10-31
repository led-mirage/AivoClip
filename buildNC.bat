@echo off
setlocal

set "AIVOCLIP_ROOT=%~dp0"
pushd "%AIVOCLIP_ROOT%" || exit /b 1

if not exist "build" mkdir "build"

rem pyenv-win cannot currently locate the Tcl/Tk 9 ZIP libraries bundled with Python 3.14.
for /f "delims=" %%I in ('venv\Scripts\python.exe -c "import sys; print(sys.base_prefix)"') do set "AIVOCLIP_PYTHON_ROOT=%%I"
for %%F in ("%AIVOCLIP_PYTHON_ROOT%\tcl\libtcl*.zip") do if exist "%%~fF" set "AIVOCLIP_TCL_ZIP=%%~fF"
for %%F in ("%AIVOCLIP_PYTHON_ROOT%\tcl\libtk*.zip") do if exist "%%~fF" set "AIVOCLIP_TK_ZIP=%%~fF"
set "AIVOCLIP_TCL_STAGE=%AIVOCLIP_ROOT%build\tcl-stage\tcl"
set "AIVOCLIP_TK_STAGE=%AIVOCLIP_ROOT%build\tcl-stage\tk"

if defined AIVOCLIP_TCL_ZIP if defined AIVOCLIP_TK_ZIP (
    powershell -NoProfile -Command "Expand-Archive -LiteralPath $env:AIVOCLIP_TCL_ZIP -DestinationPath $env:AIVOCLIP_TCL_STAGE -Force; Expand-Archive -LiteralPath $env:AIVOCLIP_TK_ZIP -DestinationPath $env:AIVOCLIP_TK_STAGE -Force"
    if errorlevel 1 (
        popd
        exit /b 1
    )
    set "TCL_LIBRARY=%AIVOCLIP_TCL_STAGE%\tcl_library"
    set "TK_LIBRARY=%AIVOCLIP_TK_STAGE%\tk_library"
)

"venv\Scripts\python.exe" -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name AivoClipNC ^
    --icon "%AIVOCLIP_ROOT%image\application.ico" ^
    --version-file "%AIVOCLIP_ROOT%version_info.txt" ^
    --add-data "%AIVOCLIP_ROOT%image:image" ^
    --distpath "dist" ^
    --workpath "build\AivoClipNC" ^
    --specpath "build" ^
    "%AIVOCLIP_ROOT%application.py"

set "AIVOCLIP_EXIT_CODE=%ERRORLEVEL%"
popd
exit /b %AIVOCLIP_EXIT_CODE%
