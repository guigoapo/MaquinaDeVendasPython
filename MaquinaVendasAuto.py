#Simulação de máquina de vendas automática
def machi(a, b, c, d, e):
	'''Essa seria a função principal, com ela eu executo todas as outras, ela irá chamar
	as outras funções na ordem "certa" que eu estabeleci. Lá em baixo ela é chamado sendo
	passado os parâmetros, que seria a quantidade de cada produto(estoque inicial).
	'''
	allprod(a, b, c, d, e)
	co=int(input("Escolha seu produto: "))
	if co!=1 and co!=2 and co!=3 and co!=4 and co!=5:
		print("\nCódigo não conhecido!")
		again=int(input("Digite 2 para escolher o produto novamente: "))
		if again==2:
			limpaTela()
			machi(a, b, c, d, e)
		else:
			print("Você escolheu sair!!")
			exit()
	if veris(a, b, c , d, e, co)==False:
		print("Produto indisponível")
		outroProd=int(input("\nDigite 1 para escolher outro produto\nOu qualquer outro numero para sair: "))
		if outroProd==1:
			limpaTela()
			comprAG(a, b, c, d, e, co)
		else:
			print("Você escolheu sair!!")
			exit()
	elif veris(a, b, c , d, e, co)==True:
		nome, preco=comprou(co)
		dinheiroDado=dinD(co)
		troco=dinheiroDado-preco
		if troco==0:
			print(f"\nValor pago: R${dinheiroDado:.2f}")
			print("Sem troco! Você pagou o valor EXATO (/O.O)/")
		elif troco>0:
			print(f"\nValor pago: R${dinheiroDado:.2f}")
			print(f"Valor do seu troco: R${troco:.2f}")
			print("\nPegue seu troco: ")
			troco1(dinheiroDado-preco)
		print()
		comprAG(a, b, c, d, e, co)
###################################################################################
def precos(co, vlu=0):
	'''
	Função para pegar o código "prod" do produto "x" e passar seu
	valor correspondente. ESSA FUNÇÃO FOI FEITA APENAS PARA FACILITAR A OUTRA FUNÇÃO
	dinD ELA DA O VALOR DE ACORDO COM O CÓDIGO ESCOLHIDO PELO CLIENTE.
	'''
	if co==1:
		vlu=5.00
	elif co==2:
		vlu=3.50
	elif co==3:
		vlu=4.50
	elif co==4:
		vlu=2.00
	elif co==5:
		vlu=4.00
	return vlu
###################################################################################
def allprod(a, b, c ,d, e):
	'''
	Essa função mostra os produtos que tem na máquina, caso não tenha estoque
	caíra no else e irá printar que o produto está indisponível.
	'''
	print("-"*33)
	if veris(a, b, c, d, e, 1):
		print(f"1 - Doritos            - R$5,00")
	else:
		print(f"1 - Doritos            - Indisponível")
	if veris(a, b, c, d, e, 2):
		print(f"2 - Coca-Cola          - R$3,50")
	else:
		print(f"2 - Coca-Cola          - Indisponível")
	if veris(a, b, c, d, e, 3):
		print(f"3 - Ruffles Ketchup    - R$4,50")
	else:
		print(f"3 - Ruffles Ketchup    - Indisponível")
	if veris(a, b, c, d, e, 4):
		print(f"4 - Bala Fini          - R$2,00")
	else:
		print(f"4 - Bala Fini          - Indisponível")
	if veris(a, b, c, d, e, 5):
		print(f"5 - Chicl. Plutonita   - R$4,00")
	else:
		print(f"5 - Chicl. Plutonita   - Indisponível")
	print("-"*33)
###################################################################################
def comprou(co, preco=0):
	'''Nessa função é mostrada qual produto o cliente escolheu e seu preço, ela também
	retornará o nome do produto e o preço.
	'''
	if co==1:
		print("Você escolheu Doritos!")
		print(f"Preço: R$5,00")
		return 'Doritos', 5.00
	elif co==2:
		print("Você escolheu Coca-Cola!")
		print(f"Preço: R$3,50")
		return 'Coca-Cola', 3.50
	elif co==3:                                
		print("Você escolheu Ruffles Ketchup!")
		print(f"Preço: R$4,50")
		return 'Ruffles', 4.50
	elif co==4:
		print("Você escolheu Bala Fini!")
		print(f"Preço: R$2,00")
		return 'Fini', 2.00
	elif co==5:
		print("Você escolheu Chicl. Plutonita!")
		print(f"Preço: R$4,00")
		return 'Plutonita', 4.00
	else:
		return False
###################################################################################
def dinD(co, valorDado=0):
	'''
	O cliente coloca o dinheiro na máquina até dar o valor do produto selecionado
	só aceita notas de 20, 10, 5, 2, e moedas de 1 real, e 50 centavos
	'''	
	vlu=precos(co)
	valor = float(input("Coloque o dinheiro: "))
	valorDado+=valor
	if vlu>valorDado:
		return dinD(co, valorDado)
	else:
		return valorDado
###################################################################################
def veris(a, b, c , d, e, co):
	'''
	Essa função verifica o estoque da máquina, e irá retornar True se tiver estoque
	e Falso se não tiver estoque, ela tem um parâmetro muito importante, dado na função
	"precos" que é o co, traduzindo, o código do produto escolhido.
	'''
	if co==1:
		if a>0:
			return True
		else:
			return False
	elif co==2:
		if b>0:
			return True
		else:
			return False
	elif co==3:
		if c>0:
			return True
		else:
			return False
	elif co==4:
		if d>0:
			return True
		else:
			return False
	elif co==5:
		if e>0:
			return True
		else:
			return False
###################################################################################
def troco1(valorTro=0):
	
	'''Essa função tem o objetivo de ir dando o troco ao cliente, ela pega o valor que o cliente
	colocou na máquina e vai dando dinheiro até o troco ser igual a 0.
	'''
	if valorTro>=200:
		print('R$ 200,00')
		return troco1(valorTro-200)
	elif valorTro>=100:
		print('R$ 100,00')
		return troco1(valorTro-100)
	elif valorTro>=50:
		print('R$ 50,00')
		return troco1(valorTro-50)
	elif valorTro>=20:
		print('R$ 20,00')
		return troco1(valorTro-20)
	elif valorTro>=10:
		print('R$ 10,00')
		return troco1(valorTro-10)
	elif valorTro>=5:
		print('R$ 5,00')
		return troco1(valorTro-5)
	elif valorTro>=2:
		print('R$ 2,00')
		return troco1(valorTro-2)
	elif valorTro>=1:
		print('R$ 1,00')
		return troco1(valorTro-1)
	elif valorTro>=0.50:
		print('R$ 0,50')
		return troco1(valorTro-0.50)
	elif valorTro>=0.25:
		print('R$ 0,25')
		return troco1(valorTro-0.25)
	elif valorTro>=0.10:
		print('R$ 0,10')
		return troco1(valorTro-0.10)
	elif valorTro>=0.05:
		print('R$ 0,05')
		return troco1(valorTro-0.05)
	elif valorTro>=0.01:
		print('R$ 0,01')
		return troco1(valorTro-0.01)
	elif valorTro==0:
		return False
###################################################################################
def comprAG(a, b, c, d, e, co):
	'''Essa função será executada só depois que o processo todo da compra for finalizado
	ela perguntará se o cliente quer fazer outra compra, como imaginei uma máquina mesmo
	ela teoricamente só tem numero, aí ela será executada se for digitado 1.
	'''
	print("1 Para SIM, e 0 para NÃO")
	cpa=int(input("Deseja fazer outra compra ? "))
	if cpa==1:
		if co==1:
			return machi(a-1, b, c, d, e)
		elif co==2:
			return machi(a, b-1, c, d, e)
		elif co==3:
			return machi(a, b, c-1, d, e)
		elif co==4:
			return machi(a, b, c, d-1, e)
		elif co==5:
			return machi(a, b, c, d, e-1)
	elif cpa==0:
		print("\nObrigado pela preferência! Nos vemos em breve ;)")
		return False
###################################################################################
from os import system, name 

def limpaTela():
	'''
	Limpa a tela do terminal.
	'''
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

###################################################################################
machi(5, 5, 5, 5, 5)