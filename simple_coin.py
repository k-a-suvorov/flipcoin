try:
	
	#Загрузка модулей программы
	
	import random
	import time
	import os

	import colorama
	from colorama import Fore, Back, Style
	colorama.init()

	class randCoin():
		
		#Объект случайная монетка со всеми полями 
		
		heads = "Орел "
		tails = "Решка "
		edges = "Ребро "
		jumpCoin = 0
		string = 'Привет, давай подбросим монетку несколько раз?'
		select = ''
		switch = True
		count01 = 0
		count02 = 0
		
		# метод класса подкидывающий монетку		
		def flipp(self):
			
			global jumpCoin 
			global coont01
			global count02
			jumpCoin = random.randrange(5)
			time.sleep(1)
			if (jumpCoin == 1):
				flip.count01 += 1
				print(Fore.GREEN + flip.heads)
			elif(jumpCoin == 5):
				flip.count02 += 1
				print(Fore.YELLOW + flip.tails)
			elif (jumpCoin == 3):
				print(Fore.CYAN + flip.edges)
			else:
				print(Fore.RED + 'Монетка закатилась под стол')	
			time.sleep(2)	
			flip.clearScreen()	
		
		# Метод класса запускающий меню игры		
		def welcome(self):
			print(Fore.WHITE + flip.string)	
			flip.select = input("Кинуть монетку? 1 - Да, 2 - не\n>>> ")
			flip.select = int(flip.select)
			if (flip.select == 1):
				flip.flipCount()
				flip.clearScreen()
				flip.statictic()
			elif (flip.select ==2):	
				flip.exitCoin()
			else:
				flip.exitCoin()	
		
		# Метод класса выход из игры
		def exitCoin(self):
			global switch
			switch = False
		
		# Метод количества подкидываний монетки
		def flipCount(self):
			flip.select = input("Сколько раз подкинуть монетку? (можно до 100 раз) \n>>> ")
			flip.select = int(flip.select)
			if (flip.select <=100):
				
				for i in range(flip.select):
					flip.flipp()
			else:
				flip.exitCoin()	
		
		# Вывод статистики
		def statictic(self):
			print(F'Орлов выпало: {flip.count01}\n Решек выпало: {flip.count02}')	
		
		# Метод очистки экрана с определением типа системы - нюансы...
		def clearScreen(self):
			try:
				if (os.name == "nt"):
					os.system("cls")
				elif(os.name == "posix"):
					os.system("clear")
			except:
				print(f"Такая система не поддерживается: {os.name}")
		
	#Main cycle	
	flip = randCoin()
	flip.welcome()
	
	
except ValueError:
    print("You have some mistake of userinput Value!")
except TypeError:
   print("You have some mistake of type Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!")
except ImportError:
	print("Some modules not loaded, please check your source code!")

