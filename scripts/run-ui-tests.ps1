<#
run-ui-tests.ps1

Inicia o chromedriver (assumindo chromedriver.exe na mesma pasta), executa os testes UI (tag 'ui')
e finaliza o chromedriver quando os testes terminam.

Uso: execute este script a partir da pasta do repositório (ele assume ./scripts/chromedriver.exe)
#>

param(
    [int]$Port = 9515
)

Push-Location $PSScriptRoot

$chromedriverPath = Join-Path $PSScriptRoot "chromedriver.exe"
if (-Not (Test-Path $chromedriverPath)) {
    Write-Error "chromedriver.exe não encontrado em $chromedriverPath. Rode install-chromedriver.ps1 primeiro ou coloque o executável aqui."
    Pop-Location
    exit 1
}

Write-Host "Iniciando chromedriver..."
$startInfo = New-Object System.Diagnostics.ProcessStartInfo
$startInfo.FileName = $chromedriverPath
$startInfo.Arguments = "--port=$Port"
$startInfo.UseShellExecute = $true

$proc = [System.Diagnostics.Process]::Start($startInfo)
Start-Sleep -Seconds 1

if ($proc -eq $null) {
    Write-Error "Falha ao iniciar chromedriver"
    Pop-Location
    exit 1
}

try {
    Write-Host "Rodando testes UI..."
    Push-Location ..
    # Executa apenas os testes UI (pasta internal/ui)
    & go test -tags=ui ./internal/ui -v
    $exitCode = $LASTEXITCODE
    Pop-Location
} finally {
    Write-Host "Finalizando chromedriver (PID $($proc.Id))..."
    try {
        $proc.Kill()
        $proc.WaitForExit(5000)
    } catch {
        Write-Warning "Erro ao encerrar chromedriver: $_"
    }
    Pop-Location
}

exit $exitCode
