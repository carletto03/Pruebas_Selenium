from selenium import webdriver
from login_page import LoginPage

def test_ejecucion_pom():

    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)

        login.ingresar_credenciales(
            "locked_out_user", "secret_sauce"
        )

        login.click_login()

        mensaje = login.obtener_error()

        print("Resultado de la prueba:", mensaje)

        assert "locked out" in mensaje

    finally:
        driver.quit()


if __name__ == "__main__":
    test_ejecucion_pom()
