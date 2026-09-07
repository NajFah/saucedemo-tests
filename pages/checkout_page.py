from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_btn = page.locator("#continue")
        self.finish_btn = page.locator("#finish")
        self.back_to_products_btn = page.locator("#back-to-products")

    def chekout_to_ferst_step(self):
        self.checkout_button.click()

     
         
    def first_step_checkout(self, fname: str, lname: str, zipp: str):
        self.first_name.fill(fname)
        self.last_name.fill(lname)
        self.postal_code.fill(zipp)
        self.continue_btn.click()


    def chekout_to_finish_step(self):
        self.finish_btn.click()
        

    def back_to_products(self):
        self.back_to_products_btn.click()

