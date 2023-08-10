class Container:
    def __init__(self):
        self.list_: list = []
        self.dict_: dict = {}

    def set_list(self, *args):
        self.list_ = list(args)

    def set_dict(self, **kwargs):
        self.dict_ = kwargs

    def modify_dict_keys(self, key, new_key):
        pass