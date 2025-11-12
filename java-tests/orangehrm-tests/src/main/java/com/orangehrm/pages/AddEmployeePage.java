package com.orangehrm.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class AddEmployeePage {
    private WebDriver driver;

    private By firstNameField = By.name("firstName");
    private By lastNameField = By.name("lastName");
    private By saveButton = By.xpath("//button[@type='submit']");

    public AddEmployeePage(WebDriver driver) {
        this.driver = driver;
    }

    public void addEmployee(String firstName, String lastName) {
        driver.findElement(firstNameField).sendKeys(firstName);
        driver.findElement(lastNameField).sendKeys(lastName);
        driver.findElement(saveButton).click();
    }

    public boolean isEmployeeCreated() {
        WebElement header = driver.findElement(By.xpath("//h6[contains(text(), 'Personal Details')]"));
        return header.isDisplayed();
    }
}
