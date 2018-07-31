from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Validacao:

    #Construtor da classe Validacao
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    #Metodo que guarda o endereco de entrega
    def setEndereco(self):
        self.endereco_entrega = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/form/div/div[2]/div[1]/ul/li[3]")
        self.endereco_entrega = self.endereco_entrega.text
        print("Endereco de entrega: " + self.endereco_entrega)

    #Metodo que guarda o preco total da compra
    def setPrecoTotal(self):
        self.totalPrice = self.driver.find_element_by_id("total_price")
        self.totalPrice = self.totalPrice.text
        print("Preco total da compra: " + self.totalPrice)
        

    #Metodo que valida se o produto foi corretamente adicionado ao carrinho
    def validaProduto(self):
        self.driver.save_screenshot("Produto.png")
        try:
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".layer_cart_product > h2:nth-child(2)"), "Product successfully added to your shopping cart"))
            print("Produto corretamente adicionado ao carrinho")
            return True
                  
        except:
            print("Produto nao adicionado ao carrinho")
            return False

    #Metodo que valida se o endereco esta correto
    def validaEndereco(self, endereco):
        self.driver.save_screenshot("EnderecoEntrega.png")
        if self.endereco_entrega != endereco:
            print("Endereco de entrega nao correspondo ao cadastrado")
            return False
        
        else:
            print("Endereco de entrega validado")
            return True

    #Metodo que valida se o preco total da compra esta correto
    def validaPreco(self, preco):
        self.driver.save_screenshot("PrecoTotal.png")
        if self.totalPrice != preco:
            print("Preco incorreto")
            return False
        
        else:
            print("Preco validado")
            return True
        
    #Metodo que valida se a compra foi finalizada com sucesso
    def validaCompra(self):
        self.driver.save_screenshot("CompraFinalizada.png")
        try:
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cheque-indent > strong:nth-child(1)"), "Your order on My Store is complete."))
            print("Compra finalizada com sucesso")
        except:
           print("Compra nao foi finalizada com sucesso")
