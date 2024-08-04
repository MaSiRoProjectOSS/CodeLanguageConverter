import os
from common.common_parameter import CommonParameter
from converter.communicator import Communicator


class CodeConverter(Communicator):
    def __init__(self, input_code_ext_type, input_code_file_name,
                 save_folder_path, parser, node_link_Data) -> None:
        super().__init__()
        self.skelton_code = ""
        self.source_file = ""

        self.input_code_ext_type = input_code_ext_type
        self.input_code_file_name = input_code_file_name
        self.save_folder_path = save_folder_path
        self.parser = parser
        self.node_link_Data = node_link_Data

        self.compile_check_and_revise_iteration_max = CommonParameter.compile_check_and_revise_iteration_max
        self.static_analysis_and_revise_iteration_max = CommonParameter.static_analysis_and_revise_iteration_max

    def create_generative_ai_clients_dual(self,
                                          pre_prompt_first: str,
                                          pre_prompt_second: str):
        self.communicator_first_id = self.create_generative_ai_client(
            pre_prompt_first)
        self.communicator_second_id = self.create_generative_ai_client(
            pre_prompt_second)

    def send_and_receive_generative_ai_message_first(self, input_message: str):
        return self.send_and_receive_ai_client_message(self.communicator_first_id, input_message)

    def send_and_receive_generative_ai_message_second(self, input_message: str):
        return self.send_and_receive_ai_client_message(self.communicator_second_id, input_message)

    def get_skelton(self):
        return self.skelton_code

    def get_source_file(self):
        return self.source_file

    def generate_other_class_import_info(self, convert_code_ext_type):
        other_class_import_message = ""
        other_class_import_list = self.get_other_class_import_list()
        file_full_path = ""

        if len(other_class_import_list) == 0:
            other_class_import_message = ""
        elif len(other_class_import_list) >= 1:
            other_class_import_message = CommonParameter.other_classes_imported_message + "\n"
            for each_list in other_class_import_list:
                class_name = each_list[0]
                other_class_file_name = self.get_converted_skelton_file_name(
                    each_list[1], convert_code_ext_type)
                file_full_path = os.path.join(
                    self.save_folder_path, other_class_file_name)

                other_class_import_message += "Imported class name: " + class_name + "\n"

                if os.path.exists(file_full_path):
                    other_code = self.read_other_code(file_full_path)
                    other_class_import_message += "The code is below." "\n\n" + other_code + "\n\n"

        else:
            other_class_import_message = ""

        return other_class_import_message, other_class_import_list

    def get_other_class_import_list(self):
        other_class_import_list = []
        file_name_ext = self.input_code_file_name + \
            CommonParameter.get_ext_from_type(self.input_code_ext_type)

        if None != self.node_link_Data:
            link_data = self.node_link_Data['links']
            for link in link_data:
                if file_name_ext == link['source']:
                    class_name = self.convert_file_name_to_class_name(
                        link['target'])
                    other_class_import_list.append(
                        [class_name, link['target']])

        return other_class_import_list

    def convert_file_name_to_class_name(self, file_name_ext):
        base_name = file_name_ext.rsplit('.', 1)[0]

        class_name = ''.join(word.capitalize()
                             for word in base_name.split('_'))

        return class_name

    def get_converted_skelton_file_name(self, file_name_ext, language_type):
        base_name = file_name_ext.rsplit('.', 1)[0]
        return base_name + CommonParameter.get_skelton_ext_from_type(language_type)

    def read_other_code(self, file_full_path):
        with open(file_full_path, 'r', encoding='utf-8') as file:
            other_code = file.read()

        return other_code
