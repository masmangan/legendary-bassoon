package com.orangehrm.pages;

import com.microsoft.playwright.Page;

public class LoginPage {
  private final Page page;
  private static final String USERNAME = "input[name='username']";
  private static final String PASSWORD = "input[name='password']";
  private static final String SUBMIT   = "button[type='submit']";

  public LoginPage(Page page) { this.page = page; }

  public LoginPage open() {
    page.navigate("https://opensource-demo.orangehrmlive.com/");
    page.waitForSelector(USERNAME);
    return this;
  }

  public void login(String username, String password) {
    page.fill(USERNAME, username);
    page.fill(PASSWORD, password);
    page.click(SUBMIT);
    page.waitForURL("**/dashboard/**");
  }
}