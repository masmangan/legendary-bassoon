package com.orangehrm;

import com.orangehrm.pages.LoginPage;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class LoginTest extends BaseTest {
  @Test
  void deveLogarComSucesso() {
    new LoginPage(page).open().login("Admin", "admin123");
    assertTrue(page.url().contains("/dashboard"),
        "Após login, esperava estar no dashboard. URL atual: " + page.url());
  }
}