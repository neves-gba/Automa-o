# Automação de Tarefas

# 1 - Acessar a plataforma de cadastro - https://dlp.hashtagtreinamentos.com/python/intensivao/login
  
import pyautogui # pyautogui - biblioteca de automação
import time

# Tempo de espera entre a execução de cada comando
pyautogui.PAUSE = 0.9
# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# pausa de 2 segundos, para esperar a pagina carregar
time.sleep(2)

# Passo 2: Fazer login

###script para localizar a posição do mouse na tela, executar separadamente
###import time
###import pyautogui
###time.sleep(5)
###print(pyautogui.position())
###pyautogui.scroll(200)

# selecionar o campo de email
pyautogui.click(x=838, y=517) #incluir as coordenadas exibidas no print acima
pyautogui.write("emailteste@gmail.com")
# Passar para o próximo campo
pyautogui.press("tab")
# Escrever a senha
pyautogui.write("senha")
# botão de login
pyautogui.click(x=938, y=700)

# 3 - Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# 4 - Cadastrar 1 produto


#executar os comandos para cada linha da tabela
for linha in tabela.index:
    #selecionar o 1º campo
    pyautogui.click(x=821, y=366)
        
    # preencher os campos
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # enviar informações cadastradas
    pyautogui.press("enter")
    pyautogui.scroll(12000)

# 5 - O processo vai se repetir o processo de cadastro até que todos estejam na plataforma





