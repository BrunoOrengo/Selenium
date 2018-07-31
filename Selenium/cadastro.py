from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string

class Cadastro:

    email = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)]) + "@teste.com"
    generoID = "id_gender1"
    nome = "John"
    sobrenome = "David"
    senha = "senhaTeste"
    dia_nascimento = "4"
    mes_nascimento = "11"
    ano_nascimento = "1997"
    endereco = "Rua Teste"
    cidade = "Cidade Teste"
    estado = "Wyoming"
    postcode = "00000"
    cel = "992861927"

    #Construtor da classe Cadastro
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        

    #Metodo que registra o email da conta
    def registEmail(self):

        #registra email
        print("Email a ser registrado: " + self.email)
        EmailBox = self.driver.find_element_by_id("email_create")
        EmailBox.send_keys(self.email)
        Prosseguir = self.driver.find_element_by_name("SubmitCreate")
        Prosseguir.click()

    #Metodo que registra os dados da conta
    def registro(self):

        #seleciona o genero 
        Genero = self.wait.until(EC.element_to_be_clickable((By.ID, "id_gender1")))
        Genero.click()
        print("Genero masculino marcado")
        
        #insere o primeiro nome
        NomeBox = self.driver.find_element_by_id("customer_firstname")
        NomeBox.send_keys(self.nome)
        print("Primeiro nome inserido")
        
        #insere o sobrenome
        LastNameBox = self.driver.find_element_by_id("customer_lastname")
        LastNameBox.send_keys(self.sobrenome)
        print("Sobrenome inserido")

        #insere a senha
        SenhaBox = self.driver.find_element_by_id("passwd")
        SenhaBox.send_keys(self.senha)
        print("Senha inserida")

        #define dia de nascimento
        selDia = Select(self.driver.find_element_by_id("days"))
        selDia.select_by_value(self.dia_nascimento)
        print("Dia de nascimento selecionado")

        #define mes de nascimento
        selMes = Select(self.driver.find_element_by_id("months"))
        selMes.select_by_value(self.mes_nascimento)
        print("Mes de nascimento selecionado")

        #define ano de nascimento
        selAno = Select(self.driver.find_element_by_id("years"))
        selAno.select_by_value(self.ano_nascimento)
        print("Ano de nascimento selecionado")

        #define rua
        EnderecoBox = self.driver.find_element_by_id("address1")
        EnderecoBox.send_keys(self.endereco)
        print("Rua definida")

        #define cidade
        CidadeBox = self.driver.find_element_by_id("city")
        CidadeBox.send_keys(self.cidade)
        print("Cidade definida")

        #define o estado
        selEstado = Select(self.driver.find_element_by_id("id_state"))
        selEstado.select_by_visible_text(self.estado)
        print("Estado definido")

        #define codigo postal
        PostCodeBox = self.driver.find_element_by_id("postcode")
        PostCodeBox.send_keys(self.postcode)
        print("Codigo postal definido")

        #define numero celular
        CelBox = self.driver.find_element_by_id("phone_mobile")
        CelBox.send_keys(self.cel)
        print("Celular definido")

        #registra conta
        Submit = self.driver.find_element_by_id("submitAccount")
        Submit.click()
        print("Conta registrada")

    #Metodo que retorna o endereco para validacao
    def getEndereco(self):
        return self.endereco
 
