# TODO написать класс Glass согласно условию
class Glass:
    def __init__(self, material):
        self.material = material

    def get_material(self):
        return self.material


if __name__ == "__main__":
    obj = Glass('metal')
    print(obj.get_material())
