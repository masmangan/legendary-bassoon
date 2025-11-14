package com.orangehrm;

import com.microsoft.playwright.*;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;

public class BaseTest {

    protected Playwright playwright;
    protected Browser browser;
    protected Page page;

    @BeforeEach
    void setup() {
        playwright = Playwright.create();

        // TROCAMOS chromium() → webkit()
        browser = playwright.webkit().launch(
            new BrowserType.LaunchOptions()
                .setHeadless(true) // pode trocar para false se quiser ver o teste rodando
        );

        page = browser.newPage();
    }

    @AfterEach
    void tearDown() {
        browser.close();
        playwright.close();
    }
}
