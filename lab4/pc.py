class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_ram(self, ram):
        self.ram = ram

    def set_storage(self, storage):
        self.storage = storage

    def display_info(self):
        print(
            f'Computer Configuration:\nCPU: {self.cpu}\nRAM: {self.ram}\nStorage: {self.storage}\n')

# Builder interface
class Builder:
    def build_cpu(self):
        pass

    def build_ram(self):
        pass

    def build_storage(self):
        pass

    def get_result(self):
        pass

# ConcreteBuilder
class GamingComputerBuilder(Builder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.set_cpu('Gaming CPU')

    def build_ram(self):
        self.computer.set_ram('16GB DDR4')

    def build_storage(self):
        self.computer.set_storage('1TB SSD')

    def get_result(self):
        return self.computer

# Director
class ComputerDirector:
    def construct(self, builder):
        builder.build_cpu()
        builder.build_ram()
        builder.build_storage()


# Client
if __name__ == '__main__':
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector()

    director.construct(gaming_builder)
    gaming_computer = gaming_builder.get_result()

    gaming_computer.display_info()