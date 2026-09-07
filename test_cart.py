from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_product_to_cart(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    expect(inventory_page.shopping_cart_badge).to_have_text("1")

    inventory_page.go_to_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(inventory_page.inventory_item_name).to_have_text("Sauce Labs Backpack")

    inventory_page.remove_backpack_from_panel() 
    expect(inventory_page.shopping_cart_badge).to_have_count(0)