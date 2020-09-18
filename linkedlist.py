class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node(data={})'.format(self.data)


class LinkedList:
    """
LinkedList:

    Initialize as follows:
            l_list = LinkedList()

    Functions:
            1) insert_at_beginning(data)
            2) insert_at_end(data)
            3) delete_node(data)
            4) is_contain(data)
            5) __repr__()
    """

    def __init__(self):
        self.__head = None
        self.__currentnode = None

    def insert_at_beginning(self, data):
        node = Node(data)

        if self.__head == None:
            self.__head = node
            self.__currentnode = node
        else:
            node.next = self.__head
            self.__head = node

        return self

    def insert_at_end(self, data):
        node = Node(data)

        if self.__head == None:
            self.__head = node
            self.__currentnode = node
        else:
            self.__currentnode.next = node
            self.__currentnode = node

        return self

    def __search(self, data):
        pointer = self.__head
        if pointer.data == data:
            return None, pointer

        while pointer.next:
            if pointer.next.data == data:
                return pointer, pointer.next  # return previous node
            pointer = pointer.next
        return None, None

    def get_node(self, data):
        prev_node, search_node = self.__search(data)
        return search_node

    def delete_node(self, data):
        if self.__head == None:
            print('You did not added any value')
            return

        if self.__head == self.__currentnode:  # if one node exists
            self.__head = None
            self.__currentnode = None
            return

        prev_node, search_node = self.__search(data)

        if prev_node == search_node == None:
            print('LinkedList does not contains %s' % data)
            return

        if prev_node == None and search_node != None:  # if the search_node is first node
            self.__head = self.__head.next
            return

        prev_node.next = search_node.next  # else
        del search_node

        return self

    def is_contain(self, data):
        pointer = self.__head
        while pointer:
            if pointer.data == data:
                print('LinkedList contains %s' % data)
                return
            pointer = pointer.next
        print('LinkedList does not contains %s' % data)

    def reverse(self):
        if self.__head is None:
            return

        self.__currentnode = self.__head
        currentnode = self.__head
        nextnode = currentnode.next
        currentnode.next = None

        while nextnode is not None:
            third_node = nextnode.next
            nextnode.next = currentnode
            currentnode = nextnode
            nextnode = third_node

        self.__head = currentnode

        return self

    def __repr__(self):
        pointer = self.__head
        data_list = []

        while pointer:
            data_list.append(pointer.data)
            pointer = pointer.next

        return f"LinkedList({data_list})"

    def print_head(self):
        print('head:', self.__head.data)

    def sort(self):
        """
        MergeSort()
        """
        pass


def main():
    l_list = LinkedList()

    l_list.insert_at_end(11)
    l_list.insert_at_end(22)
    l_list.insert_at_end(33)
    l_list.insert_at_end(44)
    l_list.insert_at_beginning(111)
    l_list.insert_at_beginning(222)
    l_list.insert_at_beginning(333)
    l_list.insert_at_beginning(444)
    l_list.print_head()
    print(l_list)

    l_list.reverse()
    l_list.print_head()
    print(l_list)

    l_list.delete_node(44)
    l_list.delete_node(444)
    l_list.delete_node(22)
    l_list.delete_node(4)

    print(l_list)
    l_list.is_contain(10)
    l_list.is_contain(11)


if __name__ == '__main__':
    main()
