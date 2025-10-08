class BubbleSorter:
    def __init__(self,data):
        self.data = data

    def bubble_sort(self):
        for i in range(len(self.data)-1):
            for j in range(len(self.data)-1-i):
                if self.data[j] > self.data[j+1]:
                    self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
            print(f"After round {i+1}: {self.data}")
    
    def display(self):
        print("Current data:", self.data)

if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(nums)
    
    print("Before sorting:")
    sorter.display()
    print("")
    sorter.bubble_sort()

    print("\nAfter sorting:")
    sorter.display()