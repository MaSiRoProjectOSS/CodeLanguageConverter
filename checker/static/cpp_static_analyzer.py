from checker.static.static_analyzer import StaticAnalyzer


class CppStaticAnalyzer(StaticAnalyzer):
    def __init__(self, class_info) -> None:
        super().__init__(class_info)

    def check_cpp_header_static_analysis(self, header_file):
        static_analysis_error_flag = False
        static_analysis_error_message = ""
        code_lines = header_file.split("\n")

        # check method declaration
        for i, method_info in enumerate(self.class_info.methods):
            method_name = self.replace_python_init_to_constructor(
                self.class_info.name, method_info)
            method_declaration_code = " " + method_name + "("

            code_exist_flag = False
            for j, line in enumerate(code_lines):
                if method_declaration_code in line:
                    code_exist_flag = True
                    break

            if False == code_exist_flag:
                static_analysis_error_flag = True
                static_analysis_error_message += "error: " \
                    + "The declaration of " \
                    + "\"" + method_declaration_code + "\"" \
                    + " is not found in the code." + "\n"

        return static_analysis_error_flag, static_analysis_error_message

    def check_cpp_source_static_analysis(self, source_file):
        static_analysis_error_flag = False
        static_analysis_error_message = ""
        code_lines = source_file.split("\n")

        # check method definition
        for i, method_info in enumerate(self.class_info.methods):
            method_name = self.replace_python_init_to_constructor(
                self.class_info.name, method_info)
            method_definition_code = self.class_info.name \
                + "::" + method_name + "("

            code_exist_flag = False
            for j, line in enumerate(code_lines):
                if method_definition_code in line:
                    code_exist_flag = True
                    break

            if False == code_exist_flag:
                static_analysis_error_flag = True
                static_analysis_error_message += "error: " \
                    + "The definition of " \
                    + "\"" + method_definition_code + "\"" \
                    + " is not found in the code." + "\n"

        return static_analysis_error_flag, static_analysis_error_message

    def replace_python_init_to_constructor(self, class_info_name, method_info):
        method_name = ""
        if method_info.name == "__init__":
            method_name = class_info_name
        else:
            method_name = method_info.name

        return method_name
