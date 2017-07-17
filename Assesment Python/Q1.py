try:
	raise RuntimeError()
except RuntimeError:
	print("Yayy! Runtime error has been raised!")