import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    opciones = Options()
    opciones.add_argument("--headless")
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")

    navegador = webdriver.Chrome(options=opciones)
    navegador.maximize_window()

    yield navegador

    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:

        driver = item.funcargs.get("driver")

        if driver:
            captura = driver.get_screenshot_as_base64()

            imagen = (
                '<div><img src="data:image/png;base64,'
                + captura
                + '" style="width:600px;"></div>'
            )

            extras = getattr(reporte, "extras", [])
            extras.append(pytest_html.extras.html(imagen))
            reporte.extras = extras
