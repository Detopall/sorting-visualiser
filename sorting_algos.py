from turtle import right
from draw_information import *
import time

def bubble_sort(draw_info, ascending=True):
	start = time.time()
	lst = draw_info.lst
	for i in range(len(lst)-1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j]
			num2 = lst[j + 1]
			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				draw_lst(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
				yield True
	end = time.time()
	print("Time consumed in working: ", end - start)
	return lst

def insertion_sort(draw_info, ascending=True):
    start = time.time()
    lst = draw_info.lst
    for i in range(1, len(lst)):
        current = lst[i]
        
        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending
            
            if not ascending_sort and not descending_sort:
                break
            
            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_lst(draw_info, {i: draw_info.GREEN, i - 1: draw_info.RED}, True)
            yield True
    end = time.time()
    print("Time consumed in working: ", end - start)
    return lst


def selection_sort(draw_info, ascending=True):
	start = time.time()
	lst = draw_info.lst
	for i in range(len(lst)):
		min_index = i
		for j in range(i + 1, len(lst)):
			if (lst[j] > lst[min_index] and not ascending) or (lst[j] < lst[min_index] and ascending):
				min_index = j

		(lst[i], lst[min_index]) = (lst[min_index], lst[i])
		draw_lst(draw_info, {i: draw_info.GREEN, min_index: draw_info.RED}, True)
		yield True
	end = time.time()
	print("Time consumed in working: ", end - start)
	return lst


def shell_sort(draw_info, ascending=True):
	start = time.time()
	lst = draw_info.lst
	length = len(lst)
	gap = length // 2

	while gap > 0:
		j = gap
		while j < length:
			i = j - gap
			while i >= 0:
				if (lst[i+gap] < lst[i] and not ascending) or (lst[i+gap] > lst[i] and ascending):
					break
				else:
					lst[i+gap], lst[i] = lst[i], lst[i+gap]
				i -= gap
			j += 1
		gap //= 2
		draw_lst(draw_info, {j: draw_info.GREEN, gap: draw_info.RED}, True)
		yield True
	end = time.time()
	print("Time consumed in working: ", end - start)
	return lst

