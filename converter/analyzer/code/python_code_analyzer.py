import json
from common.common_parameter import CommonParameter
from converter.analyzer.code.code_analyzer import CodeAnalyzer
from parser.python_code_parser import PythonCodeParser


class PythonCodeAnalyzer(CodeAnalyzer):
    def __init__(self, file_name, file_path, save_folder_path, dependency_analyzer):
        super().__init__(dependency_analyzer)

        self.pre_prompt_for_code_properties_to_json = \
            CommonParameter.analyze_python_code_properties_pre_prompt + \
            "\n" + "Example about generating class properties json is below:" + "\n" + \
            CommonParameter.example_python_code_to_json
        self.properties_communicator_id = super().create_generative_ai_client(
            self.pre_prompt_for_code_properties_to_json)

        super().read_original_code(file_path)
        self.file_path = file_path
        self.file_name = file_name
        self.save_folder_path = save_folder_path

        self.pre_prompt_for_code_methods_to_json = \
            CommonParameter.analyze_python_code_methods_pre_prompt
        self.methods_communicator_id = super().create_generative_ai_client(
            self.pre_prompt_for_code_methods_to_json)

        self.parser = PythonCodeParser(self.original_code)
        self.parser.parse_class_outline()

    def get_import_info_from_code(self):
        code_lines = self.original_code.split('\n')

        import_info = ""
        for line in code_lines:
            if line.startswith('import'):
                import_info = import_info + line + "\n"

        self.import_info = import_info

        with open(self.save_folder_path + self.file_name + "_" +
                  CommonParameter.python_import_info_file_name, 'w') as file:
            file.write(self.import_info)

    def get_import_info(self):
        return self.import_info

    def generate_save_class_properties_info_from_code(self):
        for convert_count in range(0, self.generate_class_info_iteration_max):
            json_decode_error = False
            self.generate_class_properties_info_from_code()

            self.class_properties_structure_info_file_path = self.save_folder_path + self.file_name + "_" \
                + CommonParameter.python_properties_structure_info_file_name
            with open(self.class_properties_structure_info_file_path, 'w') as file:
                file.write(self.class_properties_structure_info)

            try:
                self.parser.add_class_properties_info(
                    self.class_properties_structure_info)
            except json.JSONDecodeError as e:
                print(
                    f"Class methods info generation is failed. Count: {convert_count}")
                json_decode_error = True

            if False == json_decode_error:
                break

    def generate_class_properties_info_from_code(self):
        self.class_properties_structure_info = super().send_and_receive_ai_client_message(
            self.properties_communicator_id, self.original_code)
        self.class_properties_structure_info = self.eliminate_comment_from_json_text(
            self.class_properties_structure_info)

    def generate_class_methods_info_from_parser(self):
        outline_class_info = self.parser.get_class_info()

        each_method_json = [None]
        for i, val in enumerate(outline_class_info.methods):
            each_return_data_types_json = [None]
            each_return_names_json = [None]
            for j, val2 in enumerate(val.return_data_types):
                each_return_data_types_json.append({
                    "return_data_type": val2
                })
                if each_return_data_types_json[0] == None:
                    each_return_data_types_json = each_return_data_types_json[1:]
                each_return_names_json.append({
                    "return_name": val.return_names[j]
                })
                if each_return_names_json[0] == None:
                    each_return_names_json = each_return_names_json[1:]

            for j, val2 in enumerate(val.argument_names):
                each_argument_names_json = [None]
                each_argument_types_json = [None]
                each_argument_names_json.append({
                    "argument_name": val2
                })
                if each_argument_names_json[0] == None:
                    each_argument_names_json = each_argument_names_json[1:]
                each_argument_types_json.append({
                    "argument_type": val.argument_types[j]
                })
                if each_argument_types_json[0] == None:
                    each_argument_types_json = each_argument_types_json[1:]

            each_method_json.append({
                "name": val.name,
                "return_data_types": each_return_data_types_json or "",
                "return_names": each_return_names_json or "",
                "argument_names": each_argument_names_json or "",
                "argument_types": each_argument_types_json or "",
            })
            if each_method_json[0] == None:
                each_method_json = each_method_json[1:]

        outline_methods_json = {
            "class_name": outline_class_info.name,
            "methods": each_method_json or ""
        }

        outline_methods_json = json.dumps(
            outline_methods_json, indent=CommonParameter.json_space_amount)

        return outline_methods_json

    def generate_save_class_methods_info_from_code(self):

        for convert_count in range(0, self.generate_class_info_iteration_max):
            json_decode_error = False
            self.generate_class_methods_info_from_code()

            self.class_methods_structure_info_file_path = self.save_folder_path + self.file_name + "_" \
                + CommonParameter.python_methods_structure_info_file_name

            with open(self.class_methods_structure_info_file_path, 'w') as file:
                file.write(self.class_methods_structure_info)

            try:
                self.parser.fill_blanks_in_class_methods_info(
                    self.class_methods_structure_info)
            except json.JSONDecodeError as e:
                print(
                    f"Class methods info generation is failed. Count: {convert_count}")
                json_decode_error = True

            if False == json_decode_error:
                break

    def generate_class_methods_info_from_code(self):
        outline_methods_json = self.generate_class_methods_info_from_parser()

        message = "The original Python code is below." + "\n" + \
            self.original_code + "\n" + \
            "The incomplete methods json text is below." + "\n" + \
            outline_methods_json

        self.class_methods_structure_info = super().send_and_receive_ai_client_message(
            self.methods_communicator_id, message)
        self.class_methods_structure_info = self.eliminate_comment_from_json_text(
            self.class_methods_structure_info)

    def get_class_structure_info(self):
        class_structure_info = "[Class properties information]" + "\n" + \
            self.get_class_properties_structure_info() + "\n" + "\n" + \
            "[Class methods information]" + "\n" + \
            self.get_class_methods_structure_info()

        return class_structure_info
