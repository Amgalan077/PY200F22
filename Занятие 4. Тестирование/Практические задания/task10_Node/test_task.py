import unittest

from task import Node


class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node1 = Node()
        self.assertIsNone(node1.next)  # TODO с помощью метода assertIsNone проверить следующий узел

    def test_init_node_with_next(self):
        node1 = Node()
        node2 = Node()
        node1.next = node2
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        self.assertEqual(node1.next, node2)  # TODO проверить что узлы связались

    @unittest.skip('Привет')
    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node1 = Node(1)
        self.assertEqual(node1.__repr__(), f"Node({node1.value}, {None})")
        ...  # TODO проверить метод __repr__ без следующего узла

    ...  # TODO пропустить тест с помощью декоратора unittest.skip

    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        self.assertEqual(node1.__repr__(), f"Node({node1.value}, Node({node1.next}))")

    def test_str(self):
        some_value = 5
        node = Node(some_value)
        self.assertEqual(node.__str__(), str(node.value))
        # TODO проверить строковое представление

    def test_is_valid(self):
        node1 = '123'
        with self.assertRaises(TypeError):
            Node.is_valid(node1)
        ...  # TODO проверить метод is_valid при корректных узлах

        # TODO с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
