import unittest
from linked_list import LinkedList

# def foo(func):
#     def wrapper(*args,**kwargs):
#         list_test = [1,2,3]
#         ll = LinkedList(list_test)
#         return func()
#     return wrapper
class MyTestCase(unittest.TestCase):
    def test_append(self):
        """Проверить, что элемент успешно добавляется в конец связного списка, и увеличивается длина списка"""
        list_test = [1, 2, 3]
        ll = LinkedList(list_test)
        ll.append(4)
        list_test.append(4)
        self.assertEqual(list(ll), list_test)  # list(ll)

    def test_getitem(self):
        """Проверить, что возвращается правильное значение узла по указанному индексу."""
        list_test = [1, 2, 3]
        ll = LinkedList(list_test)
        self.assertEqual(ll[1], list_test[1])

    def test_setitem(self):
        """Проверить, что узел по указанному индексу правильно изменяется на заданное значение"""
        list_test = [1, 2, 3]
        ll = LinkedList(list_test)
        ll[1] = 100
        list_test[1] = 100
        self.assertEqual(list(ll), list_test)

    def test_to_list(self):
        """Проверить, что возвращается список со значениями всех узлов связного списка."""
        list_test = [1, 2, 3]
        ll = LinkedList(list_test)

        self.assertEqual(ll.to_list(), list_test)

    def test_add(self):
        list_test = [1, 2, 3]
        ll = LinkedList(list_test)
        ll += [4,5,6]
        list_test += [4,5,6]
        self.assertEqual(ll.to_list(),list_test)


if __name__ == '__main__':
    unittest.main()
