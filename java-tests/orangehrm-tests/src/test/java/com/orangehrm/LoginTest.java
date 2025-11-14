package com.orangehrm;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class LoginTest extends BaseTest {

    @Test
    void testSuccessfulLogin() {
        page.navigate("https://opensource-demo.orangehrmlive.com/");

        page.fill("input[name='username']", "Admin");
        page.fill("input[name='password']", "admin123");
        page.click("button[type='submit']");

        // Verificação do dashboard
        assertTrue(
            page.locator("h6").first().innerText().contains("Dashboard")
        );
    }
}
