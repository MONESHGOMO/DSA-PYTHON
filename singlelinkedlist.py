# -*- coding: utf-8 -*-
"""SingleLinkedList.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Wg2s7tkx-rSLLvXJ_fYfgXda9-992Nwz
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete_from_beg(self):
        if self.is_empty():
            print("Error: List is empty")
            return None
        data = self.head.data  # get the first node from the list
        self.head = self.head.next  # update the second node to the head
        return data  # return the 1st node as a output and delete

    def delete_from_end(self):
        if self.is_empty():
            print("Error: List is empty")
            return None
        current = self.head  # head to the current
        if current.next is None:  # check if only one node in a list
            data = current.data  # if that true current (data) store to the data
            self.head = None  # set head to none, and make the list empty
            return data
        while current.next.next is not None:
            current = current.next
        data = current.next.data
        current.next = None
        return data

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print('None')


# Example usage with dynamic input
def main():
    linked_list = SinglyLinkedList()

    while True:
        print("\nSingly Linked List Operations:")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete from Beginning")
        print("4. Delete from End")
        print("5. Search for an Element")
        print("6. Check if List is Empty")
        print("7. Get List Size")
        print("8. Display List")
        print("9. Quit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            item = input("Enter item to insert at beginning: ")
            linked_list.insert_at_beg(item)
            print(f"{item} inserted at the beginning of the list.")
        elif choice == '2':
            item = input("Enter item to insert at end: ")
            linked_list.insert_at_end(item)
            print(f"{item} inserted at the end of the list.")
        elif choice == '3':
            item = linked_list.delete_from_beg()
            if item is not None:
                print(f"Deleted item from beginning: {item}")
        elif choice == '4':
            item = linked_list.delete_from_end()
            if item is not None:
                print(f"Deleted item from end: {item}")
        elif choice == '5':
            item = input("Enter item to search: ")
            found = linked_list.search(item)
            if found:
                print(f"{item} found in the list.")
            else:
                print(f"{item} not found in the list.")
        elif choice == '6':
            if linked_list.is_empty():
                print("List is empty.")
            else:
                print("List is not empty.")
        elif choice == '7':
            size = linked_list.size()
            print(f"Size of the list: {size}")
        elif choice == '8':
            print("List elements:")
            linked_list.display()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()

