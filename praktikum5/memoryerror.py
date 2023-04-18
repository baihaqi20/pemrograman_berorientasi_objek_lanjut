try:
    data = [0] * 1000000000000
except MemoryError:
    print("MemoryError terjadi! Program mencoba mengalokasikan memori yang lebih besar daripada yang tersedia di sistem.")
