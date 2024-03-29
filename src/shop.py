import undetected_chromedriver as uc
from requests import post
from faker import Faker
import time, random, pytz
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


def get_bsb_time():
    ## MANHÃ: entre 07h30-09am > 11h55am-13pm NOITE: 17h40-22h45
    hora = datetime.now().time().strftime("%H:%M")
    hora_minuto = hora.split(":")
    hora = int(hora_minuto[0])
    minuto = int(hora_minuto[1])

    if hora >= 7 and hora < 9:
        return 0
    elif hora == 9 and minuto == 0:
        return 0
    elif hora >= 11 and hora < 13:
        return 0
    elif hora == 13 and minuto == 0:
        return 0
    elif hora >= 17 and hora < 22:
        return 0
    elif hora == 22 and minuto <= 45:
        return 0
    else:
        return 1


def generate_cpf():
    url = r"https://www.4devs.com.br/ferramentas_online.php"
    r = post(url, {"acao": "gerar_cpf", "pontuacao": "s"})
    numbers = r.text
    cpf = "{}.{}.{}-{}".format(
    numbers[:3], numbers[3:6], numbers[6:9], numbers[9:]
    )
    return cpf


def generate_name():
    faker = Faker()
    name = faker.name()
    return name

def purchase_method():  
        
    options = Options()
    options.binary_location = "/usr/bin/google-chrome"
    # options.add_argument("--headless")
    
    driver = uc.Chrome(options=options)
    # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
    cpf = generate_cpf()#'135.104.987-98'
    name = generate_name()#'Julio Caio Naves Ouverney'

    #for i in range(len(useragentarray)): 
    # Setting user agent iteratively as Chrome 108 and 107 
    print(f'CPF: {cpf}, NAME: {name}')
    #driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]}) 
    #print(driver.execute_script("return navigator.userAgent;")) 

    link = "https://nvaiacharirmao.myshopify.com/products/removedor-de-cravos-e-espinhas-lt-succao-a-vacuo" 

    # 1 | open | /collections/colecao-teste/products/mini-ferro-de-passar-roupa-lt%E2%84%A2 |  |
    while True:
        try:
            driver.get(link)
            break
        except:
            continue
    # 2 | click | css=.product-form__add-button |  |
    cookie_btn = driver.find_element(By.XPATH, "(//button[@type='submit'])[2]")
    driver.execute_script("arguments[0].click();", cookie_btn)
    # driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()

    # 3 | click | linkText=FINALIZAR COMPRA |  |
    while True:
        cart_btn = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[@class="button button--primary" and @href="/cart"]')
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", cart_btn)
        driver.execute_script("arguments[0].click();", cart_btn)

        try:
            wait = WebDriverWait(driver, 30)
            wait.until(EC.presence_of_element_located((By.ID, "name")))
            break  # sair do loop quando a ação for concluída
        except:
            continue

    # driver.find_element(By.XPATH,'//a[@class="button button--primary" and @href="/cart"]').click()
    time.sleep(10)

    # 4 | type | id=name | Jose Alves |
    driver.find_element(By.ID, "name").send_keys(name)

    # 5 | type | id=email1 | julioouverney@hotmail.com |
    driver.find_element(By.ID, "email1").send_keys("julioouverney@hotmail.com")

    # 6 | type | id=cpf | 861.621.770-33 |
    driver.find_element(By.ID, "cpf").send_keys(cpf)#"861.621.770-33")

    # 7 | type | id=homephone | (00) 00000-0000 |
    driver.find_element(By.ID, "homephone").send_keys("(24) 00000-0000")

    # 8 | click | xpath=//form[@id='form-customer']/div[3]/button |  |
    while True:
        continue_btn = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Continuar')]"
        )
        driver.execute_script("arguments[0].click();", continue_btn)

        try:
            wait = WebDriverWait(driver, 30)
            wait.until(EC.presence_of_element_located((By.ID, "zipcode")))
            break  # sair do loop quando a ação for concluída
        except:
            continue

    # 9 | type | id=zipcode | 65058-579 |
    driver.find_element(By.ID, "zipcode").send_keys("65058-579")

    # 10 | type |  id=number | 2 |
    time.sleep(10)
    driver.find_element(By.ID, "number").send_keys("2")

    # 11 | click | xpath=//form[@id='form-checkout-shipment']/div[2]/div[6]/button |  |
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-block.btn-send").click()

    time.sleep(10)
    driver.find_element(
        By.CSS_SELECTOR,
        'button.btn.btn-primary.btn-block.btn-send.link-box-checkout[data-target=".box-payment"][data-url="https://seguro.ltinovacoes.com.br/checkout/payment"]',
    ).click()

    time.sleep(10)
    # 13 | click | xpath=//form/div/div[4]/label |  |
    while True:
        payment_billet = driver.find_element(By.XPATH, "//div[4]/label/div/label")
        driver.execute_script("arguments[0].scrollIntoView(true);", payment_billet)
        driver.execute_script("arguments[0].click();", payment_billet)
        # payment_billet.click()

        try:
            wait = WebDriverWait(driver, 30)
            wait.until(
                EC.presence_of_element_located(
                    (
                        By.CLASS_NAME,
                        "btn.btn-primary.btn-block.btn-send.btn-finalize.with-icon",
                    )
                )
            )
            break  # sair do loop quando a ação for concluída
        except:
            continue

    # 14 | click | xpath=(//button[@type='submit'])[3] |  |
    finalize_btn = driver.find_element(
        By.CLASS_NAME, "btn.btn-primary.btn-block.btn-send.btn-finalize.with-icon"
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", finalize_btn)
    driver.execute_script("arguments[0].click();", finalize_btn)
    driver.quit()


def execute():
    bsb_interval = get_bsb_time()
    timezone = pytz.timezone("America/Sao_Paulo")
    dt_now = datetime.now(timezone)

    if bsb_interval == 0:
        rn = random.randint(10, 54)
        ts = random.randint(40, 60)

        print(dt_now)
        print(f"Qtd de compras:", rn)
        print(f"Qtd de delay:", ts)

        for i in range(rn):
            try:
                purchase_method()
                print(i + 1)
                time.sleep(ts)
                i += 1
            except:
                i -= 1
                time.sleep(60)
                continue
    else:
        rn = random.randint(2, 15)
        ts = random.randint(30, 120)

        print(dt_now)
        print(f"Qtd de compras:", rn)
        print(f"Qtd de delay:", ts)
        # exit()
        for i in range(rn):
            try:
                purchase_method()
                print(i + 1)
                time.sleep(ts)
                i += 1
            except:
                i -= 1
                time.sleep(60)
                continue


execute()

# generate_name()
