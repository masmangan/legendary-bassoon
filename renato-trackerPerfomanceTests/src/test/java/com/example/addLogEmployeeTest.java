
import org.junit.After;

import org.junit.Before;

import org.junit.Test;

import org.openqa.selenium.By;

import org.openqa.selenium.Dimension;

import org.openqa.selenium.WebDriver;

import org.openqa.selenium.WebElement;

import org.openqa.selenium.chrome.ChromeDriver;

import org.openqa.selenium.support.ui.ExpectedConditions;

import org.openqa.selenium.support.ui.WebDriverWait;

import io.github.bonigarcia.wdm.WebDriverManager;

import java.time.Duration;

import static org.junit.Assert.assertTrue;

public class addLogEmployeeTest {

  private WebDriver driver;

  private WebDriverWait wait;

  @Before

  public void setUp() {
    WebDriverManager.chromedriver().setup();
    driver = new ChromeDriver();

    wait = new WebDriverWait(driver, Duration.ofSeconds(10));

    driver.manage().window().setSize(new Dimension(1552, 832));

  }

  @After

  public void tearDown() {

    driver.quit();

  }

  @Test

  public void shouldAddEmployeeLogSuccessfully() {

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.name("username"))).sendKeys("Admin");

    driver.findElement(By.name("password")).sendKeys("admin123");

    driver.findElement(By.xpath("//button[@type='submit']")).click();

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//span[text()='Performance']"))).click();

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//a[text()='Employee Trackers']"))).click();

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".oxd-table-card .oxd-button"))).click();

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//button[normalize-space()='Add Log']")))
        .click();

    WebElement logInputContainer = wait
        .until(ExpectedConditions.elementToBeClickable(By.xpath("//label[text()='Log']/../following-sibling::div")));

    logInputContainer.click();

    logInputContainer.findElement(By.xpath(".//input")).sendKeys("Feedback Bacanudo");

    WebElement commentTextArea = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector(".oxd-textarea")));
    commentTextArea.click();
    commentTextArea.sendKeys("Esse cara é muito bacana, merece um feedback positivo!");

    driver.findElement(By.xpath("//button[@type='submit']")).click();

    wait.until(ExpectedConditions.textToBePresentInElementLocated(By.xpath("//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[2]/div[2]"), "Feedback Bacanudo"));

    WebElement trackLogsContainer = driver.findElement(By.xpath("//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[2]/div[2]"));
    assertTrue("New log entry should be visible within the trackLogs container.",
        trackLogsContainer.getText().contains("Feedback Bacanudo"));

    driver.findElement(By.cssSelector(".oxd-userdropdown-tab")).click();

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("Logout"))).click();

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.name("username")));

  }

}
