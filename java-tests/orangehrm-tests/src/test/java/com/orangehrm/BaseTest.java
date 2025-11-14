package com.orangehrm;

import com.microsoft.playwright.*;
import org.junit.jupiter.api.*;
import java.util.Arrays;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class BaseTest {
  protected Playwright playwright;
  protected Browser browser;
  protected BrowserContext context;
  protected Page page;

  @BeforeAll
  void setupAll() {
    boolean headless = Boolean.parseBoolean(System.getProperty("HEADLESS", "true"));
    playwright = Playwright.create();
    browser = playwright.chromium().launch(
        new BrowserType.LaunchOptions()
            .setHeadless(headless)
            .setArgs(Arrays.asList("--no-sandbox", "--disable-dev-shm-usage"))
    );
  }

  @BeforeEach
  void setup() {
    context = browser.newContext(new Browser.NewContextOptions().setViewportSize(1920, 1080));
    page = context.newPage();
  }

  @AfterEach
  void teardown() { if (context != null) context.close(); }

  @AfterAll
  void teardownAll() {
    if (browser != null) browser.close();
    if (playwright != null) playwright.close();
  }
}