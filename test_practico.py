
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    # Caso 1: Login exitoso
    print("Ejecutando Caso 1: Login exitoso")

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url

    print("Caso 1 completado correctamente")

    # Caso 2: Agregar producto al carrito
    print("Ejecutando Caso 2: Agregar al carrito")

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    carrito = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    ).text

    assert carrito == "1"

    print("Caso 2 completado correctamente")

    # Caso 3: Login fallido
    print("Ejecutando Caso 3: Login fallido")

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(
        By.CSS_SELECTOR, "[data-test='error']"
    ).text

    assert "locked out" in error

    print("Caso 3 completado correctamente")

except Exception as e:
    print("Error durante la prueba:", e)

finally:
    driver.quit()
