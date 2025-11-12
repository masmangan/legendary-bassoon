package com.orangehrm;

import com.orangehrm.pages.LoginPage;

import io.github.bonigarcia.wdm.WebDriverManager;

import com.orangehrm.pages.AddEmployeePage;
import org.junit.jupiter.api.*;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;

import java.time.Duration;

public class AddEmployeeTest {

    private WebDriver driver;
    private WebDriverWait wait;

 @BeforeEach
public void setUp() {
    WebDriverManager.chromedriver().setup();

    ChromeOptions options = new ChromeOptions();

    // 🔍 Detecta automaticamente o binário disponível
    String[] possiblePaths = {
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        "/usr/bin/google-chrome"
    };
    for (String path : possiblePaths) {
        if (new java.io.File(path).exists()) {
            options.setBinary(path);
            System.out.println("✅ Usando navegador em: " + path);
            break;
        }
    }

    // ⚙️ Configurações para ambiente sem interface (Codespaces)
    options.addArguments("--headless=new");
    options.addArguments("--no-sandbox");
    options.addArguments("--disable-dev-shm-usage");
    options.addArguments("--window-size=1920,1080");

    driver = new ChromeDriver(options);
    wait = new WebDriverWait(driver, Duration.ofSeconds(10));
}



    @Test
    public void testAddEmployee() {
        // Navega até a tela de PIM → Add Employee
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//span[text()='PIM']"))).click();
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//a[text()='Add Employee']"))).click();

        AddEmployeePage addEmployeePage = new AddEmployeePage(driver);
        addEmployeePage.addEmployee("Helio", "Testador");

        Assertions.assertTrue(addEmployeePage.isEmployeeCreated(),
                "Erro: O funcionário não foi criado corretamente.");
    }

    @AfterEach
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
