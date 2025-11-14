package com.orangehrm.pages;

import com.microsoft.playwright.Page;

public class AddEmployeePage {

    private Page page;

    private String menuPIM = "a[href='/web/index.php/pim/viewPimModule']";
    private String addButton = "a.oxd-button.oxd-button--medium.oxd-button--secondary";
    private String firstName = "input[name='firstName']";
    private String lastName = "input[name='lastName']";
    private String saveButton = "button[type='submit']";
    private String successToast = ".oxd-toast-content-text";

    public AddEmployeePage(Page page) {
        this.page = page;
    }

    public void goToAddEmployee() {
        page.click(menuPIM);
        page.click(addButton);
    }

    public void addEmployee(String fName, String lName) {
        page.fill(firstName, fName);
        page.fill(lastName, lName);
        page.click(saveButton);
    }

    public boolean isSuccessMessageShown() {
        return page.isVisible(successToast);
    }
}
