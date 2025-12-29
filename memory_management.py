import sys
import tracemalloc
def list_generator(n):
    num_list = [i for i in range(n)]
    num_generator = (i for i in range(n))
    print(f"list memory management {sys.getsizeof(num_list)}")
    print(f"generator memory management {sys.getsizeof(num_generator)}")

def list_dic(n):
    num_list = [i for i in range(n)]
    num_dict = {i: i for i in range(n)}
    num_set = {i for i in range(n)}
    print(f"list memory management {sys.getsizeof(num_list)}")
    print(f"dict memory management {sys.getsizeof(num_dict)}")
    print(f"set memory management {sys.getsizeof(num_set)}")

def mem_profile_allocator():
    tracealloc = tracemalloc.start()
    data = [i**2 for i in range(100000)]
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024:.2f} KB")
    print(f"Peak memory usage: {peak / 1024:.2f} KB")
    tracemalloc.stop()

def main():
    print("Memory Management in Python")
    print("1. List vs Generator")
    print("2. List vs Dictionary vs Set")
    print("3. Memory Profiling")
    print("4. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            list_generator(100000)
        elif choice == "2":
            list_dic(100000)
        elif choice == "3":
            mem_profile_allocator()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
