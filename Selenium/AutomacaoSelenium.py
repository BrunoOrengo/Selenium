from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from cadastro import Cadastro
from carrinho import Carrinho
from validacao import Validacao

#Cria uma nova instancia do Firefox
driver = webdriver.Firefox()

wait = WebDriverWait(driver, 10)

cadastro = Cadastro(driver)
carrinho = Carrinho(driver)
validacao = Validacao(driver)

#Vai ate a pagina inicial
driver.get("http://automationpractice.com/index.php")
print("Entrou na loja")
print (driver.title)

#Encontra e clica no produto
Produto = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div[1]/ul[1]/li[2]/div/div[1]/div/a[1]/img")
Produto.click()
print("Produto encontrado")


#Adiciona o produto ao carrinho
carrinho.setProduto()
carrinho.setPreco()
Prosseguir = driver.find_element_by_name("Submit") #Todas as instancias da variavel Prosseguir servem para avancar a compra
Prosseguir.click()
print("Produto adicionado ao carrinho")

#Garante que a janela onde diz se o produto foi corretamente adicionado ao carrinho esteja aberta antes da validacao
Prosseguir = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span")))

#Valida se o produto foi corretamente adicionado ao carrinho
if validacao.validaProduto() == False:
    driver.quit()
    
else:

    #Procede para a revisao da compra
    Prosseguir.click()
    print("Indo para o revisao da compra")


    carrinho.setPrecoCarrinho()
    #Armazena o preco total da compra para validacao (preco inicial do carrinho)
    carrinho.setPrecoTotal()



    #Procede para o checkout
    Prosseguir = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span")
    Prosseguir.click()
    print("Fazendo checkout")

    #Faz o registro do email
    cadastro.registEmail()

    #Faz o registro da conta e procede para envio
    cadastro.registro()

    #Armazena endereco de entrega para validacao
    validacao.setEndereco()

    #Valida se o endereco esta correto
    if validacao.validaEndereco(cadastro.getEndereco()) == False:
        driver.quit()
            
    else:

        #Procede para envio
        Prosseguir = driver.find_element_by_name("processAddress")
        Prosseguir.click()
        print("Indo para envio")

        #Aceita os termos de servico
        Termos = driver.find_element_by_name("cgv")
        Termos.click()

        #Procede para o pagamento
        Prosseguir = driver.find_element_by_name("processCarrier")
        Prosseguir.click()
        print("Envio feito")

        #Armazena preco total da compra para validacao(preco final do carrinho)
        validacao.setPrecoTotal()

        #Valida se o preco esta correto
        if validacao.validaPreco(carrinho.getPreco()) == False:
            driver.quit()
            
        else:

            #Finaliza o pagamento
            Prosseguir = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[1]/div/p/a")
            Prosseguir.click()
            print("Pagamento feito")

            #Finaliza a compra
            Prosseguir = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/form/p/button")
            Prosseguir.click()
            print("Finalizando compra")


            #Valida se a compra foi finalizada corretamente
            validacao.validaCompra()

            #Fecha o navegador apos fim da execucao do programa
            driver.quit()
