
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import io.github.bonigarcia.wdm.WebDriverManager;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.Duration;
import org.apache.commons.io.FileUtils;

import static org.junit.Assert.assertTrue;

public class addLogEmployeeTest {

  private WebDriver driver;
  private WebDriverWait wait;

  @Before
  public void setUp() {
    WebDriverManager.chromedriver().setup();
    ChromeOptions options = new ChromeOptions();
    options.addArguments("--headless");
    options.addArguments("--window-size=1552,832");
    driver = new ChromeDriver(options);
    wait = new WebDriverWait(driver, Duration.ofSeconds(10));
  }

  @After
  public void tearDown() {
    driver.quit();
  }

  private void takeScreenshot(String stepName) {
    try {
      Files.createDirectories(Paths.get("screenshots"));
      File scrFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
      String timestamp = String.valueOf(System.currentTimeMillis());
      FileUtils.copyFile(scrFile, new File("screenshots/" + stepName + "_" + timestamp + ".png"));
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  @Test
  public void shouldAddEmployeeLogSuccessfully() throws InterruptedException {
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
    Thread.sleep(500);
    takeScreenshot("01_LoginPage");

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.name("username"))).sendKeys("Admin");
    Thread.sleep(500);
    takeScreenshot("02_UsernameEntered");

    driver.findElement(By.name("password")).sendKeys("admin123");
    Thread.sleep(500);
    takeScreenshot("03_PasswordEntered");

    driver.findElement(By.xpath("//button[@type='submit']")).click();
    Thread.sleep(500);
    takeScreenshot("04_AfterLoginClick");

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//span[text()='Performance']"))).click();
    Thread.sleep(500);
    takeScreenshot("05_PerformanceClicked");

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//a[text()='Employee Trackers']"))).click();
    Thread.sleep(500);
    takeScreenshot("06_EmployeeTrackersClicked");

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".oxd-table-card .oxd-button"))).click();
    Thread.sleep(500);
    takeScreenshot("07_ViewTrackerClicked");

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//button[normalize-space()='Add Log']")))
        .click();
    Thread.sleep(500);
    takeScreenshot("08_AddLogClicked");

    WebElement logInputContainer = wait
        .until(ExpectedConditions.elementToBeClickable(By.xpath("//label[text()='Log']/../following-sibling::div")));
    logInputContainer.click();
    Thread.sleep(500);
    takeScreenshot("09_LogInputClicked");

    logInputContainer.findElement(By.xpath(".//input")).sendKeys("Feedback Bacanudo");
    Thread.sleep(500);
    takeScreenshot("10_LogEntered");

    WebElement commentTextArea = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector(".oxd-textarea")));
    commentTextArea.click();
    Thread.sleep(500);
    takeScreenshot("11_CommentClicked");
    
    commentTextArea.sendKeys("Esse cara é muito bacana, merece um feedback positivo!");
    Thread.sleep(500);
    takeScreenshot("12_CommentEntered");

    driver.findElement(By.xpath("//button[@type='submit']")).click();
    Thread.sleep(500);
    takeScreenshot("13_SaveClicked");

    wait.until(ExpectedConditions.invisibilityOfElementLocated(By.cssSelector(".oxd-loading-spinner")));
    wait.until(ExpectedConditions.invisibilityOfElementLocated(By.xpath("//h6[text()='Add Tracker Log']")));
    
    wait.until(ExpectedConditions.textToBePresentInElementLocated(By.xpath("//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[2]/div[2]"), "Feedback Bacanudo"));
    Thread.sleep(500);
    takeScreenshot("14_LogVisible");

    WebElement trackLogsContainer = driver.findElement(By.xpath("//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[2]/div[2]"));
    assertTrue("New log entry should be visible within the trackLogs container.",
        trackLogsContainer.getText().contains("Feedback Bacanudo"));

    driver.findElement(By.cssSelector(".oxd-userdropdown-tab")).click();
    Thread.sleep(500);
    takeScreenshot("15_UserDropdownClicked");

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("Logout"))).click();
    Thread.sleep(500);
    takeScreenshot("16_LogoutClicked");

    wait.until(ExpectedConditions.visibilityOfElementLocated(By.name("username")));
    Thread.sleep(500);
    takeScreenshot("17_BackToLogin");
  }
}
