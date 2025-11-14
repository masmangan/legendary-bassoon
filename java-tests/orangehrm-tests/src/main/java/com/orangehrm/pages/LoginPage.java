package com.orangehrm.pages;

import com.microsoft.playwright.Page;

public class LoginPage {

    private Page page;

    private String usernameField = "input[name='username']";
    private String passwordField = "input[name='password']";
    private String loginButton   = "button[type='submit']";
    private String errorMessage  = ".oxd-alert-content-text";

    public LoginPage(Page page) {
        this.page = page;
    }

    public void open() {
        page.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
    }

    public void login(String username, String password) {
        page.fill(usernameField, username);
        page.fill(passwordField, password);
        page.click(loginButton);
    }

    public boolean isDashboardVisible() {
        page.waitForURL("**/dashboard");
        return page.url().contains("/dashboard");
    }

    public String getErrorMessage() {
        return page.textContent(errorMessage);
    }
}
