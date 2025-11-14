package com.orangehrm;

import com.orangehrm.pages.AddEmployeePage;
import com.orangehrm.pages.LoginPage;
import org.junit.jupiter.api.Test;

import java.time.Instant;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class AddEmployeeTest extends BaseTest {

  @Test
  void deveAdicionarFuncionario() {
    new LoginPage(page).open().login("Admin", "admin123");

    AddEmployeePage add = new AddEmployeePage(page);
    add.openPIM();
    add.openAddEmployeeForm();

    String sufixo = String.valueOf(Instant.now().getEpochSecond());
    add.fillEmployee("Helio", "H", "Strappazzon" + sufixo);

    add.save();
    assertTrue(add.isPersonalDetailsVisible(),
        "Era esperado ver 'Personal Details' após salvar o funcionário.");
  }
}
