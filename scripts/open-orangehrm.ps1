<#
open-orangehrm.ps1

Inicia chromedriver, abre o Chrome no OrangeHRM e deixa aberto para você usar.
Perfeito para executar testes manualmente no navegador.

Uso: execute este script a partir da pasta do repositório
#>

param(
    [int]$Port = 9515
)

Push-Location $PSScriptRoot

$chromedriverPath = Join-Path $PSScriptRoot "chromedriver.exe"
if (-Not (Test-Path $chromedriverPath)) {
    Write-Error "chromedriver.exe não encontrado em $chromedriverPath. Rode install-chromedriver.ps1 primeiro."
    Pop-Location
    exit 1
}

# Carrega variáveis de ambiente
Push-Location ..
if (Test-Path ".env") {
    Get-Content .env | ForEach-Object {
        if ($_ -match '^\s*([^=]+)=(.*)$') {
            $key = $matches[1].Trim()
            $value = $matches[2].Trim()
            [System.Environment]::SetEnvironmentVariable($key, $value)
        }
    }
}
Pop-Location

$baseUrl = [System.Environment]::GetEnvironmentVariable("ORANGEHRM_BASE_URL")
if (-Not $baseUrl) {
    $baseUrl = "https://opensource-demo.orangehrmlive.com"
    Write-Warning "ORANGEHRM_BASE_URL não encontrado. Usando padrão: $baseUrl"
}

Write-Host "Iniciando chromedriver na porta $Port..."
$startInfo = New-Object System.Diagnostics.ProcessStartInfo
$startInfo.FileName = $chromedriverPath
$startInfo.Arguments = "--port=$Port"
$startInfo.UseShellExecute = $true

$proc = [System.Diagnostics.Process]::Start($startInfo)
Start-Sleep -Seconds 2

if ($proc -eq $null) {
    Write-Error "Falha ao iniciar chromedriver"
    Pop-Location
    exit 1
}

Write-Host "Chromedriver iniciado (PID $($proc.Id))"
Write-Host "Abrindo Chrome no OrangeHRM: $baseUrl"

# Abre o navegador Chrome na URL
& "chrome.exe" $baseUrl

Write-Host ""
Write-Host "Chrome foi aberto em $baseUrl"
Write-Host "Chromedriver continua rodando (PID $($proc.Id))"
Write-Host ""
Write-Host "Para encerrar o chromedriver quando terminar, aperte Ctrl+C ou execute:"
Write-Host "  taskkill /PID $($proc.Id) /F"

Pop-Location

# Aguarda Ctrl+C para encerrar
while ($true) {
    Start-Sleep -Seconds 1
}
