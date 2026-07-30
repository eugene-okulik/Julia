from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_confirm_alert_accept(page: Page):
    def alert_accept(alert: Dialog):
        alert.accept()
    page.on("dialog", alert_accept)
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role("link", name="Click").click()
    expect(page.locator("#result-text")).to_have_text("Ok")


def test_open_new_tab_and_verify_text(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Click").click()
    new_page = new_page_info.value
    expect(new_page.locator("#result-text")).to_have_text(
        "I am a new page in a new tab"
    )
    expect(page.get_by_role("link", name="Click")).to_be_enabled()


def test_click_color_change_after_red(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    button = page.locator("#colorChange")
    expect(button).to_have_css("color", "rgb(220, 53, 69)", timeout=10000)
    button.click()
