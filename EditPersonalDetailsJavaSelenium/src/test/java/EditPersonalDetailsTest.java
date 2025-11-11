import java.time.Duration;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver; // Importação adicionada
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.github.bonigarcia.wdm.WebDriverManager;

// Adicionado "throws InterruptedException" para a pequena pausa que vamos usar
public class EditPersonalDetailsTest {

    private WebDriver driver;
    private WebDriverWait wait;

    private final String BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/";
    private final String USERNAME = "Admin";
    private final String PASSWORD = "admin123";

    @BeforeEach
    void setUp() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        driver.manage().window().maximize();
    }

    @AfterEach
    void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
    
    @Test
    void testEditMaritalStatus() throws InterruptedException { 
        // --- 1. Login ---
        driver.get(BASE_URL + "auth/login");
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.name("username"))).sendKeys(USERNAME);
        driver.findElement(By.name("password")).sendKeys(PASSWORD);
        driver.findElement(By.cssSelector("button[type='submit']")).click();

        // --- 2. Navegar para "My Info" ---
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("Dashboard")));
        driver.findElement(By.linkText("My Info")).click();
        
        // Espera a página carregar
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//label[text()='Marital Status']")));

        // --- 3. Mudar o "Marital Status" ---
        By dropdownLocator = By.xpath("//label[text()='Marital Status']/../following-sibling::div");
        WebElement maritalStatusDropdown = driver.findElement(dropdownLocator);

        // Pega o valor atual para garantir que vamos mudá-lo
        String valorAtual = maritalStatusDropdown.getText();
        String novoValor = valorAtual.equals("Single") ? "Married" : "Single"; // Alterna o valor

        // Clica no dropdown
        maritalStatusDropdown.click();
        
        // Clica na nova opção
        wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//div[@role='option']/span[text()='" + novoValor + "']"))).click();
        
        // --- 4. Salvar as alterações (MÉTODO ROBUSTO) ---
        By saveButtonLocator = By.cssSelector("div.oxd-form-actions button[type='submit']");
        WebElement saveButton = wait.until(ExpectedConditions.elementToBeClickable(saveButtonLocator));
        
        // Rola o botão para o FIM da tela (evita a barra de menu)
        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("arguments[0].scrollIntoView(false);", saveButton);

        // Usa um CLIQUE REAL para enviar os dados ao servidor
        saveButton.click();

        // --- 5. Verificar (Assert) ---
        // Espera pelo pop-up de sucesso
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".oxd-toast--success")));

        // Recarrega a página para validar a persistência
        driver.navigate().refresh();
        
        Thread.sleep(500); 
        // Espera os campos carregarem novamente
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//label[text()='Marital Status']")));

        Thread.sleep(500); 
        // Pega o novo valor que foi salvo
        String valorSalvo = driver.findElement(dropdownLocator).getText();

        // Valida
        Assertions.assertEquals(novoValor, valorSalvo, "O Marital Status não foi atualizado corretamente.");
    }
}