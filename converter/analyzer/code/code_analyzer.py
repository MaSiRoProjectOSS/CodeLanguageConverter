import os
from common.common_parameter import CommonParameter
from converter.communicator import Communicator


class CodeAnalyzer(Communicator):
    def __init__(self, dependency_analyzer) -> None:
        super().__init__()
        self.import_info = ""
        self.original_code = ""

        self.save_folder_path = ""

        self.parser = None
        self.class_properties_structure_info_file_path = ""
        self.class_methods_structure_info_file_path = ""

        self.dependency_analyzer = dependency_analyzer

        self.generate_class_info_iteration_max = CommonParameter.generate_class_info_iteration_max

    def read_original_code(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as file:
            self.original_code = file.read()

    def get_original_code(self):
        return self.original_code

    def eliminate_comment_from_json_text(self, json_text):
        json_text_lines = json_text.split("\n")

        for i, text in enumerate(json_text_lines):
            if text.startswith("{"):
                break
            else:
                continue
        json_text_lines = json_text_lines[i:]

        output_text = ""
        for i, text in enumerate(json_text_lines):
            index = text.find("//")
            if index != -1:
                text = text[:index]

            index = text.find("# ")
            if index != -1:
                text = text[:index]

            output_text += text + "\n"

        return output_text

    def get_parser(self):
        return self.parser

    def update_class_properties_methods_from_file(self):
        properties_file_path = os.path.abspath(
            self.class_properties_structure_info_file_path)
        self.parser.update_class_properties_info_from_file(
            properties_file_path)

        methods_file_path = os.path.abspath(
            self.class_methods_structure_info_file_path)
        self.parser.update_class_methods_info_from_file(
            methods_file_path)

    def get_dependency_node_link_data(self):
        return self.dependency_analyzer.get_node_link_data()

    def get_class_properties_structure_info(self):
        return self.parser.get_class_properties_info()

    def get_class_methods_structure_info(self):
        return self.parser.get_class_methods_info()
