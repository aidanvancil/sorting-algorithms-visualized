import random

class Algorithms:
	def __init__(self):
		self.iterator = 1

	# Bubble Sort
	def bubble_sort(self, arr):
		for i in range(len(arr) - 1):
			if arr[i] > arr[i+1]:
				self.tempVal = arr[i+1]
				arr[i+1] = arr[i]
				arr[i] = self.tempVal
				del self.tempVal
		if arr == sorted(arr):
			random.shuffle(arr)
		return arr

	# Merge Sort
	def merge_sort(self, arr):
		if len(arr) <= 1:
			return arr
		middle = len(arr) // 2
		l_list = arr[:middle]
		r_list = arr[middle:]
		l_list = self.merge_sort(l_list)
		r_list = self.merge_sort(r_list)
		return list(self.merge(l_list, r_list))

	def merge(self, l_half,r_half):
		s = []
		while len(l_half) != 0 and len(r_half)!=0:
			if l_half[0] < r_half[0]:
				s.append(l_half[0])
				l_half.remove(l_half[0])
			else:
				s.append(r_half[0])
				r_half.remove(r_half[0])
		if len(l_half) == 0:
			s = s + r_half
		else:
			s = s + l_half
		if s == sorted(s):
			random.shuffle(s)
		return s

	# Insertion Sort
	def insertion_sort(self, arr):
		if self.iterator < len(arr): self.iterator += 1
		for j in range(self.iterator - 1, 0, -1):
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
		if arr == sorted(arr):
			random.shuffle(arr)
		return arr

	# Permutation Sort
	def permutation_sort(self, arr):
		for i in range(len(arr) - 1):
			if arr[i] > arr[i+1]:
				random.shuffle(arr)
				return arr
		return arr