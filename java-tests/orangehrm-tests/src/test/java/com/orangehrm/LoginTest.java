package com.orangehrm;

import com.orangehrm.pages.LoginPage;
import org.junit.jupiter.api.*;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

public class LoginTest {

    private WebDriver driver;
    private LoginPage loginPage;

    @BeforeEach
    void setUp() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        loginPage = new LoginPage(driver);
    }

    @Test
    @DisplayName("Login com credenciais válidas deve acessar o dashboard")
    void testLoginValido() {
        loginPage.open();
        loginPage.login("Admin", "admin123");
        Assertions.assertTrue(loginPage.isDashboardVisible(), "Falha ao validar o login válido!");
    }

    @Test
    @DisplayName("Login com senha incorreta deve mostrar mensagem de erro")
    void testLoginInvalido() {
        loginPage.open();
        loginPage.login("Admin", "senhaErrada");
        String mensagem = loginPage.getErrorMessage();
        Assertions.assertTrue(mensagem.contains("Invalid credentials"), "Mensagem de erro incorreta!");
    }

    @AfterEach
    void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}