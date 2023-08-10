from containers.args_kwargs import Container

if __name__ == '__main__':

    container = Container()

    container.set_dict(one=1, two=2)

    print(container.dict_)
