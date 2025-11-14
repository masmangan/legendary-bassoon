package com.orangehrm;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AddEmployeeTest extends BaseTest {

    @Test
    void testAddEmployee() {
        // Login
        page.navigate("https://opensource-demo.orangehrmlive.com/");
        page.fill("input[name='username']", "Admin");
        page.fill("input[name='password']", "admin123");
        page.click("button[type='submit']");

        // Navegar para PIM
        page.click("a[href='/web/index.php/pim/viewPimModule']");

        // Add Employee
        page.click("button:has-text('Add')");

        page.fill("input[name='firstName']", "Helio");
        page.fill("input[name='lastName']", "TestUser");

        page.click("button[type='submit']");

        // Verificar se redirecionou para Employee Profile
        page.waitForSelector("h6:has-text('Personal Details')");
        assertTrue(page.locator("h6").innerText().contains("Personal Details"));
    }
}


