from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://example.com')
        title = page.title()
        browser.close()
        assert 'Example' in title

if __name__ == "__main__":
    test()
    print("Test completed successfully!")