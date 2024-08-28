class Stack:
    def __init__(self, limit):
        self.stack = []
        self.limit = limit

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.limit

    def push(self, item):
        if self.is_full():
            print("Stack overflow! Cannot push more elements.")
        else:
            self.stack.append(item)
            print(f"Pushed {item} to stack.")

    def pop(self):
        if self.is_empty():
            print("Stack underflow! The stack is empty.")
        else:
            item = self.stack.pop()
            print(f"Popped {item} from stack.")
            return item

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements are:", self.stack)

def main():
    limit = int(input("Enter the limit for the stack: "))
    stack = Stack(limit)

    while True:
        print("\n1. Insert")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to push: ")
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.display()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()