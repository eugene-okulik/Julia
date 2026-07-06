from playwright.sync_api import Page


def test_get_by_role(page: Page):
    page.goto("https://demoqa.com/automation-practice-form/")
    page.get_by_placeholder("First Name").fill("John")
    page.get_by_placeholder("Last Name").fill("Test")
    page.get_by_placeholder("name@example.com").fill("johntest@example.com")
    page.locator("#gender-radio-1").check()
    page.get_by_placeholder("Mobile Number").fill("123456789")
    page.locator("#dateOfBirthInput").fill("05 Jul 2000")
    page.locator("#subjectsInput").fill("Python")
    page.locator("#hobbies-checkbox-1").check()
    page.get_by_placeholder("Current Address").fill("meksykańska 84")
    page.locator("#state input").fill("NCR")
    page.locator("#state input").press("Enter")
    page.locator("#city input").fill("Noida")
    page.locator("#city input").press("Enter")
    page.get_by_role("button", name="Submit").click()
