import re
import shutil
from common.language_type import LanguageType
from common.common_parameter import CommonParameter
from converter.converter.code_converter import CodeConverter
from checker.compiler.cpp_compile_checker import CppCompileChecker
from checker.static.cpp_static_analyzer import CppStaticAnalyzer


class CppCodeConverter(CodeConverter):
    def __init__(self, input_code_ext_type, input_code_file_name,
                 save_folder_path, parser, node_link_Data) -> None:
        super().__init__(input_code_ext_type, input_code_file_name,
                         save_folder_path, parser, node_link_Data)

        self.compiler_checker = CppCompileChecker(self.save_folder_path)
        self.static_analyzer = CppStaticAnalyzer(self.parser.get_class_info())

        other_class_import_message, self.other_class_import_list = self.generate_other_class_import_info(
            LanguageType.CPP)

        if self.input_code_ext_type == LanguageType.Python:
            self.pre_prompt_for_convert_Python_to_CPP_header = \
                CommonParameter.generate_cpp_header_from_python_code_pre_prompt \
                + "\n" + CommonParameter.json_format_example_message + "\n" \
                + CommonParameter.example_python_code_to_json + "\n" \
                + other_class_import_message
            self.pre_prompt_for_convert_Python_to_CPP_source = \
                CommonParameter.generate_cpp_source_from_python_code_pre_prompt
            super().create_generative_ai_clients_dual(
                self.pre_prompt_for_convert_Python_to_CPP_header,
                self.pre_prompt_for_convert_Python_to_CPP_source)

        elif self.input_code_ext_type == LanguageType.CS:
            self.pre_prompt_for_convert_CS_to_CPP_header = \
                CommonParameter.generate_cpp_header_from_cs_code_pre_prompt
            self.pre_prompt_for_convert_CS_to_CPP_source = \
                CommonParameter.generate_cpp_source_from_cs_code_pre_prompt
            super().create_generative_ai_clients_dual(
                self.pre_prompt_for_convert_CS_to_CPP_header,
                self.pre_prompt_for_convert_CS_to_CPP_source)
        else:
            raise ValueError(
                "The input_code_ext_type is not supported.")

    def create_header_file(self, class_structure_info, import_info):

        message = ""
        if self.input_code_ext_type == LanguageType.Python:
            message = "\n" + CommonParameter.class_structure_message + "\n" \
                + class_structure_info \
                + "\n" + CommonParameter.imports_of_python_code_message + "\n" \
                + import_info
        elif self.input_code_ext_type == LanguageType.CS:
            message = "\n" + CommonParameter.skelton_code_message + "\n" \
                + class_structure_info \
                + "\n" + CommonParameter.imports_of_cs_code_message + "\n" \
                + import_info
        else:
            raise ValueError(
                "The input_code_ext_type is not supported.")

        self.save_export_libraries_with_header()

        self.generate_header_code_and_check_revise(message)

    def generate_header_code_and_check_revise(self, message):

        for convert_count in range(0, self.static_analysis_and_revise_iteration_max):
            message = self.generate_header_code_and_compile_check(message)

            static_analysis_error_flag, static_analysis_error_message = self.static_analyzer.check_cpp_header_static_analysis(
                self.header_file)

            if False == static_analysis_error_flag:
                break
            else:
                print(
                    f"Retry to generate C++ header code due to static analysis error. Count: {convert_count}")

                message = message \
                    + self.header_file + "\n\n" \
                    + CommonParameter.cpp_header_static_analysis_error_and_rewrite_message + "\n\n" \
                    + static_analysis_error_message

    def generate_header_code_and_compile_check(self, message):
        for convert_count in range(0, self.compile_check_and_revise_iteration_max):

            self.header_file = super().send_and_receive_generative_ai_message_first(
                message)

            self.tailor_header_file()

            file_name_ext = self.input_code_file_name + ".hpp"
            with open(self.save_folder_path + file_name_ext, 'w') as file:
                file.write(self.header_file)

            compile_message = ""
            if True == self.compiler_checker.is_compiler_exists():
                compile_message = self.compiler_checker.compile_cpp_file_and_get_error_message(
                    file_name_ext)

            if "" == compile_message:
                break
            else:
                print(
                    f"Retry to generate C++ header code due to compile error. Count: {convert_count}")

                message = message \
                    + self.header_file + "\n\n" \
                    + CommonParameter.cpp_header_compile_error_and_rewrite_message + "\n\n" \
                    + compile_message

        if "" != compile_message:
            print("There are still compile errors in the generated C++ header code.")

        return message

    def tailor_header_file(self):
        self.header_file = self.header_file + "\n"

        self.header_file = self.avoid_multi_definition_of_header(
            self.header_file)
        self.header_file = self.add_export_libraries_in_header(
            self.header_file)

        if len(self.other_class_import_list) >= 1:
            self.header_file = self.add_other_class_import_in_header(
                self.header_file, self.other_class_import_list)

    def get_header_file(self):
        return self.header_file

    def create_source_file(self, original_code):
        message = "\n" + CommonParameter.original_code_message + "\n" \
            + original_code \
            + "\n" + CommonParameter.header_file_message + "\n" \
            + self.header_file

        self.generate_source_code_and_check_revise(message)

    def generate_source_code_and_check_revise(self, message):

        for convert_count in range(0, self.static_analysis_and_revise_iteration_max):
            message = self.generate_source_code_and_compile_check(message)

            static_analysis_error_flag, static_analysis_error_message = self.static_analyzer.check_cpp_source_static_analysis(
                self.source_file)

            if False == static_analysis_error_flag:
                break
            else:
                print(
                    f"Retry to generate C++ source code due to static analysis error. Count: {convert_count}")

                message = message \
                    + self.source_file + "\n\n" \
                    + CommonParameter.cpp_source_static_analysis_error_and_rewrite_message + "\n\n" \
                    + static_analysis_error_message

    def generate_source_code_and_compile_check(self, message):
        for convert_count in range(0, self.compile_check_and_revise_iteration_max):

            self.source_file = super().send_and_receive_generative_ai_message_second(
                message)

            self.tailor_source_file()

            file_name_ext = self.input_code_file_name + ".cpp"
            with open(self.save_folder_path + file_name_ext, 'w') as file:
                file.write(self.source_file)

            compile_message = ""
            if True == self.compiler_checker.is_compiler_exists():
                compile_message = self.compiler_checker.compile_cpp_file_and_get_error_message(
                    file_name_ext)
                if "" == compile_message:
                    compile_message = self.compiler_checker.link_cpp_file_and_get_undefined_multiple_message(
                        file_name_ext)

            if "" == compile_message:
                break
            else:
                print(
                    f"Retry to generate C++ source code due to compile error. Count: {convert_count}")

                message = message \
                    + self.header_file + "\n\n" \
                    + CommonParameter.cpp_source_compile_error_and_rewrite_message + "\n\n" \
                    + compile_message

        if "" != compile_message:
            print("There are still compile errors in the generated C++ source code.")

        return message

    def tailor_source_file(self):
        self.source_file = self.eliminate_include_text(self.source_file)
        self.source_file = self.avoid_unnecessary_comment_before_class_definition(
            self.source_file)

        self.source_file = "#include \"" + self.input_code_file_name + ".hpp\"" + "\n" \
            + "\n" \
            + self.source_file + "\n"

    def get_source_file(self):
        return self.source_file

    def avoid_multi_definition_of_header(self, original_code: str):
        hpp_pattern = re.compile(
            r'#ifndef\s+(\w+_HPP)\s+#define\s+\1', re.MULTILINE)
        match = hpp_pattern.search(original_code)

        if None == match:
            h_pattern = re.compile(
                r'#ifndef\s+(\w+_H)\s+#define\s+\1', re.MULTILINE)
            match = h_pattern.search(original_code)

        checked_text = ""
        if None != match:
            code_lines = original_code.split("\n")
            for i, line in enumerate(code_lines):
                if (i == match.start()) or (i == match.start() + 1):
                    continue
                else:
                    if line.startswith("#endif"):
                        break
                    checked_text += line + "\n"
        else:
            checked_text = original_code

        checked_text = self.eliminate_include_text(checked_text)
        checked_text = self.avoid_unnecessary_comment_before_class_declaration(
            checked_text)

        header_def_name = self.input_code_file_name.upper() + "_HPP"
        header_def_name = header_def_name.replace(" ", "_")
        header_def_name = header_def_name.replace(".", "_")

        modified_code = "#ifndef " + header_def_name + "\n#define " + header_def_name + "\n\n" + \
            checked_text + "\n\n#endif\n"

        return modified_code

    def eliminate_include_text(self, original_code: str):
        code_lines = original_code.split("\n")
        checked_text = ""
        for i, line in enumerate(code_lines):
            if line.startswith("#include"):
                continue
            else:
                checked_text += line + "\n"

        return checked_text

    def add_export_libraries_in_header(self, original_code):
        code_lines = original_code.split("\n")
        output_text = ""

        export_include_line_position = 0
        for i, line in enumerate(code_lines):
            if line.startswith("#ifndef "):
                export_include_line_position = i + 2
                break

        for i, line in enumerate(code_lines):
            if i == export_include_line_position:
                output_text += "\n" + CommonParameter.python_export_libraries_text + "\n" + line + "\n"
            else:
                output_text += line + "\n"

        return output_text

    def add_other_class_import_in_header(self, original_code, other_class_import_list):
        for each_list in other_class_import_list:
            output_text = original_code
            code_lines = output_text.split("\n")
            output_text = ""
            header_file_name = self.get_converted_header_name(each_list[1])

            other_class_import_line_position = 0
            for i, line in enumerate(code_lines):
                if line.startswith("#ifndef "):
                    other_class_import_line_position = i + 2
                    break

            for i, line in enumerate(code_lines):
                if i == other_class_import_line_position:
                    output_text += "\n" + "#include \"" + \
                        header_file_name + "\"" + "\n" + line + "\n"
                else:
                    output_text += line + "\n"

            original_code = output_text

        return output_text

    def save_export_libraries_with_header(self):
        file_names = CommonParameter.python_export_libraries_file_names

        for file_name in file_names:
            src_file_path = "./" + CommonParameter.python_export_libraries_path + file_name
            dst_folder_path = self.save_folder_path + file_name
            shutil.copy(src_file_path, dst_folder_path)

    def avoid_unnecessary_comment_before_class_declaration(self, original_code: str):
        code_lines = original_code.split("\n")
        output_text = ""
        class_started = False
        for i, line in enumerate(code_lines):
            if line.startswith("class "):
                class_started = True
                output_text += line + "\n"
            else:
                if True == class_started:
                    output_text += line + "\n"

        return output_text

    def avoid_unnecessary_comment_before_class_definition(self, original_code: str):
        code_lines = original_code.split("\n")
        output_text = ""
        class_started = False

        for i, line in enumerate(code_lines):
            if "::" in line:
                class_started = True
                output_text += line + "\n"
            else:
                if True == class_started:
                    output_text += line + "\n"

        return output_text

    def get_converted_header_name(self, file_name_ext):
        base_name = file_name_ext.rsplit('.', 1)[0]
        return base_name + ".hpp"
