from playwright.sync_api import sync_playwright


def create_storage_state():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

        page.fill(
            "input[name='username']",
            "Admin"
        )

        page.fill(
            "input[name='password']",
            "admin123"
        )

        page.click(
            "button[type='submit']"
        )

        page.wait_for_url("**/dashboard/index")

        page.context.storage_state(
            path="storage_state.json"
        )

        browser.close()


create_storage_state()