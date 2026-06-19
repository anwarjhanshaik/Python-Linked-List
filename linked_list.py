class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class SLL:
  def __init__(self, head = None):
    self.head = head
    self.size = 0
    current = self.head
    while current:
      self.size += 1
      current = current.next
  
  def __len__(self):
    return self.size
  
  def __iter__(self):
    current = self.head
    while current:
      yield current.data 
      current = current.next
    
  def __str__(self):
    if self.is_empty():
      return "List is empty"
    self.check_and_fix_cycle()
    result = []
    for node_data in self:
      result.append(f"{node_data}")
    return " --> ".join(result) + " --> None"
  
  def is_empty(self):
    return self.head == None 
  
  def search(self, item):
    current = self.head
    while current:
      if current.data == item:
        return current 
      current = current.next
    return 
  
  def find_index(self, item):
    index = 0
    current = self.head
    while current:
      if current.data == item:
        return index
      index += 1
      current = current.next
    return -1
  
  def find_middle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow
  
  def has_cycle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False
  
  def get_at_index(self, index):
    if (self.is_empty() or (index < 0) or (index >= len(self))):
      raise IndexError("Out of range")
    temp = 0
    current = self.head
    while current:
      if temp == index:
        return current
      temp += 1
      current = current.next
  
  def insert_at_index(self, index, item):
    if index < 0:
      raise IndexError("Index cannot be negative")
    if index == 0:
      self.insert_at_start(item)
      return 
    if index >= len(self):
      self.insert_at_last(item)
      return 
    prev = self.get_at_index(index - 1)
    node = Node(item, prev.next)
    prev.next = node
    self.size += 1
    
  def insert_at_start(self, item):
    node = Node(item, self.head)
    self.head = node
    self.size += 1
  
  def insert_at_last(self, item):
    node = Node(item)
    if self.is_empty():
      self.head = node
      self.size += 1
      return 
    current = self.head
    while current.next:
      current = current.next
    current.next = node
    self.size += 1
  
  def insert_after(self, address, item):
    if address:
      node = Node(item, address.next)
      address.next = node
      self.size += 1
  
  def remove_at_start(self):
    if self.is_empty():
      return 
    self.head = self.head.next
    self.size -= 1
    
  def remove_at_last(self):
    if self.is_empty():
      return 
    if not self.head.next:
      self.head = None
      self.size -= 1
      return 
    current = self.head
    while current.next.next:
      current = current.next
    current.next = None
    self.size -= 1
  
  def remove_item(self, item):
    if self.is_empty():
      return 
    if self.head.data == item:
      self.head = self.head.next
      self.size -= 1
      return 
    current = self.head
    while current.next:
      if current.next.data == item:
        current.next = current.next.next
        self.size -= 1
        return 
      current = current.next
  
  def clear(self):
    self.head = None
    self.size = 0
  
  def remove_at_index(self, index):
    if ((index < 0) or (index >= len(self))):
      raise IndexError("Index out of range")
    if index == 0:
      self.remove_at_start()
      return 
    prev = self.get_at_index(index-1)
    prev.next = prev.next.next
    self.size -= 1
  
  def delete_duplicates(self):
    if self.is_empty():
      return 
    current = self.head
    seen = set([current.data])
    while current.next:
      if current.next.data in seen:
        current.next = current.next.next
        self.size -= 1
      else:
        seen.add(current.next.data)
        current = current.next
  
  def deleteEntaireInstanceOfItem(self, item):
    if self.is_empty():
      return
    
    while self.head and self.head.data == item:
      self.head = self.head.next
      self.size -= 1
    current = self.head
    while current and current.next:
      if current.next.data == item:
        current.next = current.next.next
        self.size -= 1
      else:
        current = current.next
  
  def delete_middle(self):
    if self.is_empty():
      return 
    if not self.head.next:
      self.head = None
      self.size = 0
      return 
    prev = None
    slow = self.head
    fast = self.head 
    while fast and fast.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next
    prev.next = slow.next
    self.size -= 1
  
  def check_and_fix_cycle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        slow = self.head
        if slow == fast:
          while fast.next != slow:
            fast = fast.next
        else:
          while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
        self.size = 0
        current = self.head
        while current:
          self.size += 1
          current = current.next
        return True
    return False
    
  def reverse_list(self):
    if self.is_empty():
      return 
    if not self.head.next:
      return self.head
    prev = None
    current = self.head
    next = None
    while current:
      next = current.next
      current.next = prev
      prev = current 
      current = next
    self.head = prev
    return prev
  
# ==========================================
# SIMPLE TEST SCRIPT 
# ==========================================

# 1. Create a brand new empty list
my_list = SLL()
print("--- Step 1: Created an empty list ---")
print(f"Is the list empty? {my_list.is_empty()}")
print(f"List size: {len(my_list)}")
print()

# 2. Add some numbers to the list
print("--- Step 2: Adding items to the list ---")
my_list.insert_at_start(10)  # List is now: 10
my_list.insert_at_last(30)   # List is now: 10 -> 30
my_list.insert_at_index(1, 20)  # Inserts 20 at index 1: 10 -> 20 -> 30

# 3. Search for numbers in the list
print("--- Step 3: Searching for items ---")
index_of_20 = my_list.find_index(20)
print(f"Where is number 20? Found at index: {index_of_20}")

index_of_99 = my_list.find_index(99)
print(f"Where is number 99? Found at index: {index_of_99} (-1 means it does not exist)")
print()

# 4. Find the middle element
print("--- Step 4: Finding the middle node ---")
middle_node = my_list.find_middle()
if middle_node:
    print(f"The middle element is: {middle_node.data}")
print()

# 5. Remove items from the list
print("--- Step 5: Removing items ---")
print("Removing the first item (10)...")
my_list.remove_at_start()
print(my_list)

print("Removing the last item (30)...")
print(my_list)
print(f"Final list size: {len(my_list)}")
print()

# 6. Test reversing the list
print("--- Step 6: Reversing a new list ---")
my_list.clear()
my_list.insert_at_last(1)
my_list.insert_at_last(2)
my_list.insert_at_last(3)
print("Original list:")
print(my_list)

print("Reversing the list...")
my_list.reverse_list()
print(my_list)

  
