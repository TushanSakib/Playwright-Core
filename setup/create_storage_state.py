from playwright.sync_api import sync_playwright


BASE_URL = (
    "https://opensource-demo.orangehrmlive.com/"
    "web/index.php/auth/login"
)

USERNAME = "Admin"
PASSWORD = "admin123"


def create_storage_state():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        context = browser.new_context()

        page = context.new_page()

        page.goto(BASE_URL)

        page.locator(
            "input[name='username']"
        ).fill(USERNAME)

        page.locator(
            "input[name='password']"
        ).fill(PASSWORD)

        page.locator(
            "button[type='submit']"
        ).click()

        page.wait_for_url(
            "**/dashboard/index"
        )

        context.storage_state(
            path="storage_state.json"
        )

        browser.close()

        print(
            "✅ storage_state.json created successfully"
        )


if __name__ == "__main__":
    create_storage_state()