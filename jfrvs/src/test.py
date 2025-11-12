import time
from datetime import datetime

from playwright.sync_api import sync_playwright

# Constants

ORANGE_LOGIN_PAGE = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

# Main test method

def test_navigation_to_website():
    with sync_playwright() as p:

        print("Launching Chromium...") 

        browser = p.chromium.launch()
        page = browser.new_page()

        print("Navigating to OrangeRM...")

        page.goto(ORANGE_LOGIN_PAGE)

        page.wait_for_load_state('networkidle')

        if page.title() == 'OrangeHRM':
            page.screenshot(path=f'./test_prints/test_navigation_to_website/{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.png')
            browser.close()
            return True
        
        browser.close()
        return False

def test_login():
    with sync_playwright() as p:

        print("Launching Chromium...") 

        browser = p.chromium.launch()
        page = browser.new_page()

        print("Navigating to OrangeRM...")

        page.goto(ORANGE_LOGIN_PAGE)

        page.wait_for_load_state('networkidle')

        print("Filling credentials...")

        username_field = page.locator('input[name="username"]')
        username_field.wait_for(state='visible')
        username_field.fill('Admin')
            
        password_field = page.locator('input[name="password"]')
        password_field.fill('admin123')

        print('Login in...')

        login_button = page.locator('button[type="submit"]')
        login_button.click()

        time.sleep(3)

        page.screenshot(path='1.png')

        if 'dashboard' in page.url:
            page.screenshot(path=f'./test_prints/test_login/{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.png')
            browser.close()
            return True
        
        browser.close()
        return False
    
def test_change_user_name():
    with sync_playwright() as p:

        print("Launching Chromium...") 

        browser = p.chromium.launch()
        page = browser.new_page()

        print("Navigating to OrangeRM...")

        page.goto(ORANGE_LOGIN_PAGE)

        page.wait_for_load_state('networkidle')

        print("Filling credentials...")

        username_field = page.locator('input[name="username"]')
        username_field.wait_for(state='visible')
        username_field.fill('Admin')
            
        password_field = page.locator('input[name="password"]')
        password_field.fill('admin123')

        print('Login in...')

        login_button = page.locator('button[type="submit"]')
        login_button.click()

        time.sleep(3)

        page.wait_for_selector('.oxd-sidepanel', state='visible')

        my_info_link = page.locator('a[href="/web/index.php/pim/viewMyDetails"]')
        my_info_link.click()

        time.sleep(3)

        firstname_field = page.locator('input[name="firstName"]')
        firstname_field.fill('James')
        lastname_field = page.locator('input[name="lastName"]')
        lastname_field.fill('Queue')

        page.click('button.oxd-button--secondary:nth-child(2)')

        time.sleep(3)

        dashboard_link = page.locator('a[href="/web/index.php/dashboard/index"]')
        dashboard_link.click()

        time.sleep(3)

        print(page.locator('.oxd-userdropdown-name').text_content())

        if page.locator('.oxd-userdropdown-name').text_content() == "James Queue":
            page.screenshot(path=f'./test_prints/test_change_user_name/{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.png')
            browser.close()
            return True
        
        browser.close()
        return False

if __name__ == "__main__":
    print('='*50)
    print("First test: Navigation")
    print('='*50)
    print('')
    first_test = test_navigation_to_website()
    if first_test:
        print("Passed!")
    print('='*50)
    print("Second test: Access")
    print('='*50)
    print('')
    second_test = test_login()
    if second_test:
        print("Passed!")
    print('='*50)
    print("Third test: Changing user name")
    print('='*50)
    print('')
    third_test = test_change_user_name()
    if third_test:
        print("Passed!")
    print('='*50)
    print(f"Results: {first_test + second_test + third_test} of 3 tests passed succesfully.")
    print('='*50)
    print('')