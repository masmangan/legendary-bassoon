<#
run-ui-tests.ps1

Inicia o chromedriver (assumindo chromedriver.exe na mesma pasta), executa os testes UI (tag 'ui')
e finaliza o chromedriver quando os testes terminam.

Uso: execute este script a partir da pasta do repositório (ele assume ./scripts/chromedriver.exe)
#>

param(
    [int]$Port = 9515,
    [switch]$KeepOpen = $false
)

Push-Location $PSScriptRoot

$chromedriverPath = Join-Path $PSScriptRoot "chromedriver.exe"
if (-Not (Test-Path $chromedriverPath)) {
    Write-Error "chromedriver.exe não encontrado em $chromedriverPath. Rode install-chromedriver.ps1 primeiro ou coloque o executável aqui."
    Pop-Location
    exit 1
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

try {
    Write-Host "Rodando testes UI (isto abrirá o Chrome automaticamente)..."
    Push-Location ..
    # Executa apenas os testes UI (pasta internal/ui)
    & go test -tags=ui ./internal/ui -v
    $exitCode = $LASTEXITCODE
    Pop-Location
    
    if ($KeepOpen) {
        Write-Host "Testes concluídos. Pressione ENTER para encerrar o chromedriver..."
        Read-Host
    }
} finally {
    if (-Not $KeepOpen -or $exitCode -ne 0) {
        Write-Host "Finalizando chromedriver (PID $($proc.Id))..."
        try {
            $proc.Kill()
            $proc.WaitForExit(5000)
        } catch {
            Write-Warning "Erro ao encerrar chromedriver: $_"
        }
    } else {
        Write-Host "Chromedriver permanecerá rodando. Use taskkill /PID $($proc.Id) para encerrar manualmente."
    }
    Pop-Location
}

exit $exitCode
