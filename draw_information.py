from audioop import avg
import math
from turtle import clear
import pygame

class DrawInformation:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	BACKGROUND_COLOR = WHITE

	GRADIENTS = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]

	FONT = pygame.font.SysFont('comicsans', 20)
	LARGE_FONT = pygame.font.SysFont('comicsans', 30)

	SIDE_PADDING = 100
	TOP_PADDING = 150
	
	def __init__(self, width, height, lst):
			self.width = width
			self.height = height

			self.window = pygame.display.set_mode((width, height))
			pygame.display.set_caption("Sorting Algorithm Visualization")
			self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst
		self.min_val = min(lst)
		self.max_val = max(lst)

		self.block_width = round((self.width - self.SIDE_PADDING) / len(lst))
		self.block_height = math.floor((self.height - self.TOP_PADDING) / (self.max_val - self.min_val))
		self.start_x = self.SIDE_PADDING // 2
  


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    
    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.RED)
    
    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 3, draw_info.BLACK)
    
    sorting = draw_info.FONT.render("H - Shell Sort > S - Selection Sort > I - Insertion Sort > B - Bubble Sort", 3, draw_info.BLACK)
    
    avg_time = draw_info.FONT.render("Shell ~0.083s > Selection ~0.83s > Insertion ~10.13s > Bubble ~10.30s", 3, draw_info.BLACK)
        
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))
    
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 45))
    
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 80))
    
    draw_info.window.blit(avg_time, (draw_info.width/2 - avg_time.get_width()/2, 115))
    
    draw_lst(draw_info)
    pygame.display.update()
    
    
def draw_lst(draw_info, color_positions={}, clear_bg=False):
	lst = draw_info.lst
	
	if clear_bg:
		clear_background(draw_info)
	show_list(lst, draw_info, color_positions)
	
	if clear_bg:
		pygame.display.update()
	
        
def clear_background(draw_info):
        clear_rect = (draw_info.SIDE_PADDING//2, draw_info.TOP_PADDING, draw_info.width - draw_info.SIDE_PADDING, draw_info.height)
        
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)
    

def show_list(lst, draw_info, color_positions):
	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width
		y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
		color = draw_info.GRADIENTS[i % 3]
		
		if i in color_positions:
			color = color_positions[i]
		
		pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))