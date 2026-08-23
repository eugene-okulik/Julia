import re
from playwright.sync_api import Page


def test_change_response(page: Page):

    def handle_response(route):
        response = route.fetch()
        data = response.json()

        family_type = data["body"]["digitalMat"][0]["familyTypes"][0]

        # Меняем название внутри табы
        family_type["productName"] = "яблокофон 17 про"

        route.fulfill(
            response=response,
            json=data
        )

    # Отлавливаем запрос с информацией о товарах
    page.route(
        re.compile("digital-mat"),
        handle_response
    )

    # Открываем страницу
    page.goto("https://www.apple.com/shop/buy-iphone")

    # Кликаем на iPhone 17 Pro
    page.locator(".rf-hcard-content-title").filter(
        has_text="iPhone 17 Pro"
    ).click()

    # Находим заголовок в попапе
    heading = page.get_by_role(
        "heading",
        name="яблокофон 17 про"
    )

    # Проверяем, что заголовок равен тому,
    # на который мы заменили
    assert heading.inner_text() == "яблокофон 17 про"
