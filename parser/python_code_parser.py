from parser.code_parser import CodeParser
from common.common_parameter import CommonParameter


class PythonCodeParser(CodeParser):
    def __init__(self, original_code):
        super().__init__(original_code)
        self.class_declared_text = None
        self.class_declared_line = None

        self.class_declared_indent_amount = None

    def parse_class_outline(self):
        self.get_class_declaration()

        class_info = self.create_class_info(
            self.get_class_name(self.class_declared_text),
            None, None, None)
        self.add_class_info_to_self(class_info)

        self.class_declared_indent_amount = self.get_class_declared_indent_amount(
            self.class_declared_text)

        super_class_names = self.get_super_class_names(
            self.class_declared_text)
        self.set_super_class_names(super_class_names)

        self.set_method_outline()

        return self.class_info

    def get_class_declaration(self):
        class_declared_text = [None]
        class_declared_line = [None]
        for i, val in enumerate(self.original_code_lines):
            if (val.startswith("class") or
                    (val.startswith(" ") and " class " in val)):
                class_declared_text.append(val)
                class_declared_line.append(i)

        if (len(class_declared_text) == 1):
            raise ValueError("No class declaration found in the code")

        if (len(class_declared_text) > 2):
            raise ValueError("Multiple class declaration found in the code")

        self.class_declared_text = class_declared_text[1]
        self.class_declared_line = class_declared_line[1]

    def get_super_class_names(self, class_declared_text):
        super_class_names = None

        after_bra = class_declared_text.split("(")
        if (len(after_bra) > 1):
            between_bracket = after_bra[1].split("):")[0]
            super_class_names = between_bracket.split(",")

        return super_class_names

    def get_class_name(self, class_declared_text):
        class_name = class_declared_text.split("(")[0].split("class ")[1]
        if class_name.endswith(":"):
            class_name = class_name[:-1]

        return class_name

    def get_class_declared_indent_amount(self, class_declared_line):
        class_indent = 0
        split_Text = class_declared_line.split("class ")
        if (len(split_Text) > 1):
            class_indent = len(split_Text[0])

        return class_indent

    def set_method_outline(self):
        method_id_text = ""
        for i in range(CommonParameter.python_space_amount):
            method_id_text += " "
        if (self.class_declared_indent_amount != None and
                self.class_declared_indent_amount > 0):
            for i in range(self.class_declared_indent_amount):
                method_id_text += " "

        method_id_text += "def "

        search_code_lines = self.original_code_lines[self.class_declared_line:]

        for i, val in enumerate(search_code_lines):
            if val.startswith(method_id_text):
                method_name, argument_names = self.get_method_outline_from_line(
                    val, method_id_text)
                method_info = self.create_method_info(
                    method_name,
                    None, None,
                    argument_names,
                    None, None, None,
                    self.class_declared_line + i + 1)
                self.add_method_info_to_self(method_info)

    def get_method_outline_from_line(self, method_declared_line, method_id_text):
        split_text = method_declared_line.split(method_id_text)
        method_name = split_text[1].split("(")[0]

        split_text = method_declared_line.split(method_name + "(")
        argument_names = split_text[1].split(")")[0]
        argument_names = argument_names.split(",")

        for i, val in enumerate(argument_names):
            if val.find(": "):
                argument_names[i] = val.split(": ")[0]

        if argument_names[0] == "self":
            argument_names = argument_names[1:]

        for i, val in enumerate(argument_names):
            argument_names[i] = val.replace(" ", "")

        return method_name, argument_names
