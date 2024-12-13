class MemoryManager:
    def __init__(self, size):
        """
        Initialize the memory manager.z
        :param size: Total size of the memory array.
        """
        self.memory = [0] * size
        self.size = size
        self.last_position = 0

    def allocate(self, block_size):
        """
        Allocates memory using the Next Fit algorithm.
        :param block_size: Size of the memory block to allocate.
        :return: Starting index of allocated block, or -1 if allocation fails.
        """
        start = self.last_position
        for i in range(self.size):
            idx = (start + i) % self.size
            if self._can_allocate(idx, block_size):
                self._allocate_memory(idx, block_size)
                self.last_position = (idx + block_size) % self.size
                return idx
        return -1  # Allocation failed

    def deallocate(self, start, block_size):
        """
        Deallocates a memory block.
        :param start: Starting index of the block to deallocate.
        :param block_size: Size of the memory block.
        """
        for i in range(start, start + block_size):
            self.memory[i % self.size] = 0

    def _can_allocate(self, start, block_size):
        """
        Checks if memory can be allocated at a given position.
        :param start: Starting index.
        :param block_size: Size of the memory block.
        :return: True if memory can be allocated, False otherwise.
        """
        if start + block_size > len(self.memory):  # Check for out-of-bounds
            return False
            # Check each memory cell in the specified range
        return all(cell == 0 for cell in self.memory[start:start + block_size])
    
   

    def _allocate_memory(self, start, block_size):
        """
        Allocates memory at a given position.
        :param start: Starting index.
        :param block_size: Size of the memory block.
        """
        for i in range(block_size):
            self.memory[start + i] = 1

    def memory_status(self):
        """
        Returns the current memory allocation status.
        :return: List representing memory allocation (0 = free, 1 = allocated).
        """
        return self.memory
