<#
Install-Chromedriver.ps1

Detecta a versão do Google Chrome instalada e baixa a versão correspondente
do chromedriver (Windows). Extrai o chromedriver.exe na pasta atual.

Uso: execute este script dentro da pasta onde quer que o chromedriver.exe fique (ex: ./scripts)
#>

Write-Host "Detectando versão do Google Chrome..."

$chromeVersion = $null
try {
    $chromeVersion = (Get-ItemProperty 'HKLM:\SOFTWARE\Google\Chrome\BLBeacon' -ErrorAction Stop).version
} catch {
    try {
        $chromeVersion = (Get-ItemProperty 'HKCU:\SOFTWARE\Google\Chrome\BLBeacon' -ErrorAction Stop).version
    } catch {
        Write-Warning "Não consegui detectar a versão do Chrome no registro. Será usado o 'latest' do chromedriver.";
    }
}

if ($chromeVersion) {
    Write-Host "Versão do Chrome detectada: $chromeVersion"
    $major = $chromeVersion.Split('.')[0]
    Write-Host "Buscando versão do chromedriver compatível com major version $major..."
    $latestUrl = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE/$major"
    try {
        $driverVersion = Invoke-RestMethod -Uri $latestUrl -UseBasicParsing -ErrorAction Stop
    } catch {
        Write-Warning "Falha ao buscar versão específica: $_. Usando LATEST_RELEASE (mais recente)."
        $driverVersion = Invoke-RestMethod -Uri "https://chromedriver.storage.googleapis.com/LATEST_RELEASE" -UseBasicParsing
    }
} else {
    Write-Host "Usando última versão disponível do chromedriver..."
    $driverVersion = Invoke-RestMethod -Uri "https://chromedriver.storage.googleapis.com/LATEST_RELEASE" -UseBasicParsing
}

Write-Host "Versão do chromedriver a baixar: $driverVersion"

$zipName = "chromedriver_win32.zip"
$uri = "https://chromedriver.storage.googleapis.com/$driverVersion/$zipName"

Write-Host "Baixando $uri ..."
Invoke-WebRequest -Uri $uri -OutFile $zipName -UseBasicParsing

Write-Host "Extraindo..."
Expand-Archive -Path $zipName -DestinationPath . -Force
Remove-Item $zipName

Write-Host "Chromedriver pronto: $(Resolve-Path .\chromedriver.exe)"
