package com.orangehrm.pages;

import com.microsoft.playwright.Locator;
import com.microsoft.playwright.Page;

public class AddEmployeePage {
  private final Page page;

  private static final String PIM_MENU     = "nav >> text=PIM";
  private static final String ADD_BUTTON   = "button:has-text('Add')";
  private static final String FIRST_NAME   = "input[name='firstName']";
  private static final String MIDDLE_NAME  = "input[name='middleName']";
  private static final String LAST_NAME    = "input[name='lastName']";
  private static final String SAVE_BUTTON  = "button:has-text('Save')";
  private static final String PERSONAL_DETAILS_HEADER = "text=Personal Details";

  public AddEmployeePage(Page page) { this.page = page; }

  public void openPIM() {
    page.click(PIM_MENU);
    page.waitForURL("**/pim/**");
  }

  public void openAddEmployeeForm() {
    page.click(ADD_BUTTON);
    page.waitForSelector(FIRST_NAME);
  }

  public void fillEmployee(String first, String middle, String last) {
    page.fill(FIRST_NAME, first);
    page.fill(MIDDLE_NAME, middle);
    page.fill(LAST_NAME, last);
  }

  public void save() {
    page.click(SAVE_BUTTON);
    page.waitForSelector(PERSONAL_DETAILS_HEADER);
  }

  public boolean isPersonalDetailsVisible() {
    Locator header = page.locator(PERSONAL_DETAILS_HEADER);
    return header.first().isVisible();
  }
}