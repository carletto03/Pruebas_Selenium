import pytest
from selenium.webdriver.common.by import By
from login_page import LoginPage



def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()

    assert "inventory.html" in driver.current_url


def test_login_fallido(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()

    assert "locked out" in login.obtener_error()


def test_agregar_carrito(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()

    boton = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    )
    boton.click()

    carrito = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    ).text

    assert carrito == "1"
