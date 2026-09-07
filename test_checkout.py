from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_full_checkout_flow(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    expect(inventory_page.shopping_cart_badge).to_have_text("1")
    inventory_page.go_to_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(inventory_page.inventory_item_name).to_have_text("Sauce Labs Backpack")

    checkout_page = CheckoutPage(page)
    checkout_page.chekout_to_ferst_step()
    checkout_page.first_step_checkout("Najim", "Fahym", "23009")
    checkout_page.chekout_to_finish_step()
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

    checkout_page.back_to_products()
    expect(inventory_page.shopping_cart_badge).to_have_count(0)