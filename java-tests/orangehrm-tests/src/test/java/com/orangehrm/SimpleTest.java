package com.orangehrm;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.*;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.io.File;
import java.time.Duration;

import static org.junit.jupiter.api.Assertions.*;

public class SimpleTest {

    private WebDriver driver;

    @BeforeEach
    void setUp() {
        WebDriverManager.chromedriver().setup();

        ChromeOptions options = new ChromeOptions();

        // 🔍 Detecta automaticamente o Chrome ou Chromium no sistema
        String[] paths = {"/usr/bin/chromium", "/usr/bin/chromium-browser", "/usr/bin/google-chrome"};
        for (String path : paths) {
            if (new File(path).exists()) {
                options.setBinary(path);
                System.out.println("✅ Usando navegador em: " + path);
                break;
            }
        }

        // ⚙️ Configurações para rodar em ambiente sem interface (como Codespaces)
        options.addArguments("--headless=new");
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-dev-shm-usage");
        options.addArguments("--window-size=1920,1080");

        driver = new ChromeDriver(options);
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
    }

    @Test
    void testPaginaAbre() {
        driver.get("https://example.com");
        String title = driver.getTitle();
        System.out.println("Título da página: " + title);
        assertEquals("Example Domain", title);
    }

    @AfterEach
    void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
