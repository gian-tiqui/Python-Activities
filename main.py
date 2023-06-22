from OOP.Computer import Ram, Processor, GPU, Computer

if __name__ == '__main__':

    my_computer = Computer(Processor("i5"), GPU("NVIDIA"), Ram(16000))

    print(my_computer)
