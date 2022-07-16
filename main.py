import pygame
import random
from sorting_algorithms import algorithms, constants

algorithms = algorithms.Algorithms()

def main():
	
	print(
	"""
			1) Bubble Sort
			2) Merge Sort
			3) Insertion Sort
			4) Permutation Sort
			5) Exit Program
	""")

	while True:
		try:
			algo_selected = int(input("Select algorithm: "))
			break
		except:
			print("Invalid input type, try again.")
			continue
		

	FPS = 60
	clock = pygame.time.Clock()
	WINDOW = pygame.display.set_mode(constants.SIZE)

	datas = []
	data_range = 1000

	for counter in range(data_range):
		datas.append(random.randint(1, constants.HEIGHT))

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		WINDOW.fill(constants.BLACK)

		for counter in range(data_range):
			rectWidth = constants.WIDTH / data_range
			rectHeight = datas[counter]
			rectX = counter * rectWidth
			rectY = constants.HEIGHT - rectHeight

			pygame.draw.rect(WINDOW, constants.LEMON, (rectX, rectY, rectWidth, rectHeight))


		if algo_selected == 1:
			pygame.display.set_caption("Bubble Sort")

			datas = algorithms.bubble_sort(datas)
		elif algo_selected == 2:
			pygame.display.set_caption("Merge Sort")
			datas = algorithms.merge_sort(datas)
		elif algo_selected == 3:
			pygame.display.set_caption("Insertion Sort")
			datas = algorithms.insertion_sort(datas)
		elif algo_selected == 4:
			pygame.display.set_caption("Permutation Sort")
			datas = algorithms.permutation_sort(datas)
		elif algo_selected == 5:
			print("Exiting")
			running = False
		else:
			print("Algorithm not found")
			running = False
		
		clock.tick(FPS)
		pygame.display.update()
	

if __name__ == "__main__":
	main()