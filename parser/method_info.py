class MethodInfo:
    def __init__(self):
        self.name = ""
        self.return_data_types = [None]
        self.return_names = [None]
        self.argument_names = [None]
        self.argument_types = [None]
        self.is_static = False
        self.is_public = False
        self.original_code_position = 0
