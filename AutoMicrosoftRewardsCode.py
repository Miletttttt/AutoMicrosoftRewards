import pyautogui
import time 
import pyperclip
import random

# =====================
# Entrar no REWARDS
# =====================

pyautogui.press("win")
time.sleep(1)
#muda para o teu navegador!
pyautogui.write("brave")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://rewards.bing.com")
pyautogui.press("enter")

# =====================
# Resgatar CONJUNTO DIÁRIO
# =====================

time.sleep(2)

pyautogui.click(x=450, y=450)
time.sleep(.75)
pyautogui.scroll(-300)
time.sleep(1)
pyautogui.click(x=550, y=600)
time.sleep(1)
pyautogui.click(x=100, y=18)
time.sleep(1)
pyautogui.click(x=1150,y=650)
time.sleep(1)
pyautogui.click(x=100, y=18)
time.sleep(1)
pyautogui.click(x=1550,y=650)

search = [
    "Star Wars",
    "Harry Potter",
    "Avatar",
    "Hobbit",
    "Senhor dos Aneis",
    "Homem-Aranha",
    "Batman",
    "Superman",
    "Vingadores",
    "Homem de Ferro",
    "Capitao America",
    "Thor",
    "Hulk",
    "Pantera Negra",
    "Doutor Estranho",
    "Flash",
    "Liga da Justica",
    "Deadpool",
    "X-Men",
    "Wolverine",
    "Naruto",
    "Dragon Ball",
    "One Piece",
    "Attack on Titan",
    "Demon Slayer",
    "Jujutsu Kaisen",
    "Death Note",
    "Tokyo Ghoul",
    "Fullmetal Alchemist",
    "Bleach",
    "Minecraft",
    "Fortnite",
    "GTA 5",
    "Red Dead Redemption 2",
    "The Last of Us",
    "God of War",
    "Call of Duty",
    "FIFA",
    "Free Fire",
    "League of Legends",
    "Valorant",
    "CS GO",
    "Roblox",
    "Among Us",
    "Terraria",
    "Cyberpunk 2077",
    "Elden Ring",
    "Dark Souls",
    "Skyrim",
    "The Witcher",
    "Stranger Things",
    "Breaking Bad",
    "Game of Thrones",
    "The Walking Dead",
    "Peaky Blinders",
    "The Boys",
    "Wednesday serie",
    "Loki serie",
    "Wandavision",
    "Black Mirror",
    "Rick and Morty",
    "Simpsons",
    "Family Guy",
    "South Park",
    "filmes 2025",
    "melhores series",
    "noticias tecnologia",
    "inteligencia artificial",
    "como programar",
    "python tutorial",
    "jogos novos",
    "filmes lancamento",
    "curiosidades espaco",
    "buracos negros",
    "planetas do sistema solar",
    "viagem no tempo",
    "teoria da relatividade",
    "historia do Brasil",
    "segunda guerra mundial",
    "imperio romano",
    "mitologia grega",
    "dinossauros",
    "animais perigosos",
    "como estudar melhor",
    "dicas produtividade",
    "como ganhar dinheiro online",
    "negocios digitais",
    "marketing digital",
    "como fazer exercicios",
    "treino em casa",
    "alimentacao saudavel",
    "receitas faceis",
    "como dormir melhor"
]

extra = ["curiosidades", "historia", "explicaçao", "teoria", "review"]

# ==========================================
# Resgatar PONTOS COM PESQUISA =====================
# ==========================================

# =====================
# Escrever no local do clique
# =====================

pyautogui.sleep(1.5)

pyautogui.click(x= 264, y = 22) 
pyautogui.click(x= 600, y= 60)
pyautogui.write("https://www.bing.com/?FORM=Z9FD1")
pyautogui.sleep(1)
pyautogui.press('enter')

# =====================
# Escrever, começo
# =====================

pyautogui.sleep(2)

termo = random.choice(search)
complemento = random.choice(extra)

pyautogui.click(x=880, y=325)
pyautogui.write(f"{termo} {complemento}")
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(1.5)

# =====================
# Escrever aleatoriamente
# =====================
for i in range(90):
    
    termo = random.choice(search)
    complemento = random.choice(extra)
    
    pyautogui.click(x=355, y=165)

    pyautogui.hotkey("ctrl", "a")  # seleciona tudo
    pyautogui.press("backspace")

    time.sleep(random.uniform(.75, .8))
    pyautogui.write(f"{termo} {complemento}")
    
    time.sleep(random.uniform(.75, .8))
    pyautogui.press("enter")

    time.sleep(.8)