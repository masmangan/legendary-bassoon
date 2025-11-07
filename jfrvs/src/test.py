import time

from playwright.sync_api import sync_playwright

# Constants

ORANGE_LOGIN_PAGE = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

# Main test method

def test():
    with sync_playwright() as p:

        print("Launching Chromium...") 

         = p.chromiubrowserm.launch()
        page = browser.new_page()

        print("Navigating to OrangeRM...")

        page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        page.wait_for_load_state('networkidle')

        page.screenshot(path='1.png')

        print("Filling credentials...")

        username_field = page.locator('input[name="username"]')
        username_field.wait_for(state='visible')
        username_field.fill('Admin')
            
        password_field = page.locator('input[name="password"]')
        password_field.fill('admin123')

        page.screenshot(path='2.png')

        print('Login in...')

        login_button = page.locator('button[type="submit"]')
        login_button.click()

        time.sleep(5)

        page.screenshot(path='3.png')

        browser.close()

if __name__ == "__main__":
    print(test())