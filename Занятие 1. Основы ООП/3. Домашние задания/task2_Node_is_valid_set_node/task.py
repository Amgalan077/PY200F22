from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    # def set_next(self, node: Optional['Node']):
    #     self.next = node
    #  
    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        if isinstance(node,Node):
            return True
        raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        #
        if self.is_valid(next_):
            self.next = next_



if __name__ == '__main__':
    first_node = Node(1)
    second_node = Node(2)
    first_node.set_next(second_node)
    

    print(first_node)
    print(second_node)
