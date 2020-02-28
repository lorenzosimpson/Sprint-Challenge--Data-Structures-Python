from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if we're at capacity:
        if self.storage.__len__() < self.capacity:
            # keep adding to the end of the list
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        # if we hit capacity
        elif self.storage.__len__() == self.capacity:
            # if we're at the last thing in the list, we know the first thing is the oldest
            if self.current.next == None:
                # remove thing at head
                self.storage.remove_from_head()
                # the new head we just added is now the current, so we can go on
                self.storage.add_to_head(item)
                # always set current to whatever we just changed
                self.current = self.storage.head
            # else we're not at the end of the list
            else:
                # the next thing to delete is gonna come after whatever we just updated
                #delete it
                self.current.next.delete()
                # insert the new node after it (where the deleted one just was)
                self.current.insert_after(item)
                # and keep moving forward
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = [item for item in self.storage.iter()]

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
