from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.inventory_item_name = page.locator(".inventory_item_name")
        self.remove_auce_labs_backpack_button = page.locator("#remove-sauce-labs-backpack")

    def add_backpack_to_cart(self):
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.shopping_cart_link.click()

    def remove_backpack_from_panel(self):
        self.remove_auce_labs_backpack_button.click()
        