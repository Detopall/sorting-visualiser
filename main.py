from asyncio import TimerHandle
import pygame
pygame.init()
import random
import math
import time
from draw_information import *
from list_generation import *
from sorting_algos import *



def main():
	clock = pygame.time.Clock()
	run = True
	n = 50
	min_val = 0
	max_val = 100

	lst = generate_starting_list(n, min_val, max_val)
	draw_info = DrawInformation(800, 600, lst)
	sorting = False
	ascending = True
 
	sorting_alg, sorting_alg_name = bubble_sort, "Bubble Sort"
	sorting_alg_generator = None

	while run:
		clock.tick(60) #fps
		draw(draw_info, sorting_alg_name, ascending)
  
		if sorting:
			try:
				next(sorting_alg_generator)
			except StopIteration:
				sorting = False
		else:
			draw(draw_info, sorting_alg_name, ascending)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type != pygame.KEYDOWN:
				continue
			if event.key == pygame.K_r:
				lst = generate_starting_list(n, min_val, max_val)
				draw_info.set_list(lst)
				sorting = False
			elif event.key == pygame.K_SPACE and sorting == False:
				sorting = True
				sorting_alg_generator = sorting_alg(draw_info, ascending)
			elif event.key == pygame.K_a and not sorting:
				ascending = True
			elif event.key == pygame.K_d and not sorting:
				ascending = False
			elif event.key == pygame.K_i and not sorting:
				sorting_alg, sorting_alg_name = insertion_sort, "Insertion Sort"
			elif event.key == pygame.K_b and not sorting:
				sorting_alg, sorting_alg_name = bubble_sort, "Bubble Sort"
			elif event.key == pygame.K_s and not sorting:
				sorting_alg, sorting_alg_name = selection_sort, "Selection Sort"
			elif event.key == pygame.K_h and not sorting:
				sorting_alg, sorting_alg_name = shell_sort, "Shell Sort"
			elif event.key == pygame.K_q and not sorting:
				sorting_alg, sorting_alg_name = quick_sort, "Quick Sort"
    
	pygame.quit()

if __name__ == "__main__":
    main()