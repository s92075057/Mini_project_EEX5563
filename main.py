from memory_manager import MemoryManager

def main():
    print("Welcome to the Next Fit Memory Allocation Simulation!")
    memory_size = int(input("Enter the total memory size: "))
    manager = MemoryManager(memory_size)

    while True:
        print("\nMenu:")
        print("1. Allocate Memory")
        print("2. Deallocate Memory")
        print("3. Show Memory Status")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            block_size = int(input("Enter block size to allocate: "))
            index = manager.allocate(block_size)
            if index != -1:
                print(f"Memory allocated starting at index {index}.")
            else:
                print("Memory allocation failed.")
        elif choice == "2":
            start = int(input("Enter starting index to deallocate: "))
            block_size = int(input("Enter block size to deallocate: "))
            manager.deallocate(start, block_size)
            print("Memory deallocated.")
        elif choice == "3":
            status = manager.memory_status()
            print(f"Memory Status: {status}")
        elif choice == "4":
            print("Exiting the simulation. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
