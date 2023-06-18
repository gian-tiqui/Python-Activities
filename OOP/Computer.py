class Processor:
    def __init__(self, processor: str):
        self.processor: str = processor


class Ram:
    def __init__(self, ram: int):
        self.ram: int = ram


class GPU:
    def __init__(self, driver: str):
        self.driver: str = driver


class Computer:
    def __init__(self, processor: Processor, gpu: GPU, ram: Ram):
        self.processor: Processor = processor
        self.gpu: GPU = gpu
        self.ram: Ram = ram
