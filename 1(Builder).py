class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"CPU: {self.cpu}, GPU: {self.gpu}, RAM: {self.ram}, Storage: {self.storage}"


class ComputerBuilder:
    def reset(self):
        self.computer = Computer()

    def set_cpu(self):
        pass

    def set_gpu(self):
        pass

    def set_ram(self):
        pass

    def set_storage(self):
        pass

    def get_result(self):
        return self.computer

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.reset()

    def set_cpu(self):
        self.computer.cpu = "Intel Core i9"

    def set_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"

    def set_ram(self):
        self.computer.ram = "32GB DDR5"

    def set_storage(self):
        self.computer.storage = "2TB NVMe SSD"


class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.reset()

    def set_cpu(self):
        self.computer.cpu = "Intel Core i5"

    def set_gpu(self):
        self.computer.gpu = "Integrated Graphics"

    def set_ram(self):
        self.computer.ram = "16GB DDR4"

    def set_storage(self):
        self.computer.storage = "512GB SSD"


class Director:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_computer(self):
        self.builder.reset()
        self.builder.set_cpu()
        self.builder.set_gpu()
        self.builder.set_ram()
        self.builder.set_storage()
        return self.builder.get_result()


if __name__ == "__main__":
    gaming_builder = GamingComputerBuilder()
    director = Director(gaming_builder)
    gaming_pc = director.build_computer()
    print("Gaming PC:", gaming_pc)

    office_builder = OfficeComputerBuilder()
    director = Director(office_builder)
    office_pc = director.build_computer()
    print("Office PC:", office_pc)
