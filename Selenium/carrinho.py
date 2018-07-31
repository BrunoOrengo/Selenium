from selenium import webdriver

class Carrinho:

    #Construtor da classe Carrinho
    def __init__(self, driver):
        self.driver = driver

    #Metodo que armazena o nome do produto
    def setProduto(self):
        self.produto = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div/div[3]/h1")
        self.produto = self.produto.text
        print("Produto: " + self.produto)

    #Metodo que armazena o preco do produto
    def setPreco(self):
        self.preco = self.driver.find_element_by_class_name("our_price_display")
        self.preco = self.preco.text
        print("Preco: " + self.preco)

    #Metodo que armazena o preco do carrinho
    def setPrecoCarrinho(self):
        self.preco_carrinho = self.driver.find_element_by_id("total_product_price_2_7_0")
        self.preco_carrinho = self.preco_carrinho.text
        print("Preco do carrinho: " + self.preco_carrinho)

    #Metodo que armazena o preco total da compra    
    def setPrecoTotal(self):
        self.preco_total = self.driver.find_element_by_id("total_price")
        self.preco_total = self.preco_total.text
        print("Preco total (com valor da entrega): " + self.preco_total)

    #Metodo que retorna o produto para validacao
    def getProduto(self):
        return self.produto

    #Metodo que retorna o preco para validacao
    def getPreco(self):
        return self.preco_total
