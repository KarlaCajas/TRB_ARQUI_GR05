# Script de instalación y ejecución rápida
# Uso: .\setup_y_ejecutar.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   CONVERSOR DE UNIDADES - CLIENTE      " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
Write-Host "Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ $pythonVersion encontrado" -ForegroundColor Green
} catch {
    Write-Host "❌ Python no está instalado. Por favor, instale Python 3.7 o superior." -ForegroundColor Red
    exit 1
}

Write-Host ""

# Instalar dependencias
Write-Host "Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencias instaladas correctamente" -ForegroundColor Green
} else {
    Write-Host "❌ Error al instalar dependencias" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "IMPORTANTE: Asegúrate de que el servidor" -ForegroundColor Yellow
Write-Host ".NET esté ejecutándose en el puerto 5014" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$respuesta = Read-Host "¿Deseas ejecutar el cliente ahora? (S/N)"

if ($respuesta -eq "S" -or $respuesta -eq "s") {
    Write-Host ""
    Write-Host "🚀 Ejecutando cliente de conversión de unidades..." -ForegroundColor Green
    Write-Host ""
    python cliente_api.py
} else {
    Write-Host ""
    Write-Host "Para ejecutar el cliente más tarde, usa:" -ForegroundColor Yellow
    Write-Host "  python cliente_api.py" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "         Programa finalizado            " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
