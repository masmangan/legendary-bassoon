<?php
declare(strict_types=1);

use PHPUnit\Framework\TestCase;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Chrome\ChromeOptions;
use Facebook\WebDriver\WebDriverBy;

final class SeleniumLoginRegisterTest extends TestCase
{
    private $driver;
    private $baseUrl = 'http://127.0.0.1:8080';

    protected function setUp(): void
    {
        // Configura o Chrome (modo headless)
        $options = new ChromeOptions();
        $options->addArguments([
            '--headless=new',
            '--no-sandbox',
            '--disable-dev-shm-usage',
            '--window-size=1200,800'
        ]);

        $capabilities = DesiredCapabilities::chrome();
        $capabilities->setCapability(ChromeOptions::CAPABILITY, $options);

        // Conecta ao ChromeDriver
        $this->driver = RemoteWebDriver::create('http://127.0.0.1:9515', $capabilities, 5000);
    }

    protected function tearDown(): void
    {
        if ($this->driver) {
            $this->driver->takeScreenshot(__DIR__ . '/../../evidences/final-' . time() . '.png');
            $this->driver->quit();
        }
    }

    public function testUserRegistrationAndLoginFlow(): void
    {
        // ETAPA 1: Cadastro
        $this->driver->get($this->baseUrl . '/register.html');

        $email = 'selenium_' . time() . '@example.com';
        $this->driver->findElement(WebDriverBy::name('name'))->sendKeys('Usuário Selenium');
        $this->driver->findElement(WebDriverBy::name('email'))->sendKeys($email);
        $this->driver->findElement(WebDriverBy::name('password'))->sendKeys('Senha123!');
        $this->driver->findElement(WebDriverBy::name('password_confirm'))->sendKeys('Senha123!');
        $this->driver->findElement(WebDriverBy::cssSelector('button[type="submit"]'))->click();

        sleep(1);
        $this->driver->takeScreenshot(__DIR__ . '/../../evidences/register-' . time() . '.png');

        // ETAPA 2: Login
        $this->driver->findElement(WebDriverBy::name('email'))->sendKeys($email);
        $this->driver->findElement(WebDriverBy::name('password'))->sendKeys('Senha123!');
        $this->driver->findElement(WebDriverBy::cssSelector('button[type="submit"]'))->click();

        sleep(1);
        $this->driver->takeScreenshot(__DIR__ . '/../../evidences/login-' . time() . '.png');

        // ETAPA 3: Dashboard
        $bodyText = $this->driver->findElement(WebDriverBy::tagName('body'))->getText();
        $this->assertStringContainsString('Bem-vindo', $bodyText, 'Texto "Bem-vindo" não encontrado no dashboard.');

        $this->driver->takeScreenshot(__DIR__ . '/../../evidences/dashboard-' . time() . '.png');
    }
}
