import os
import subprocess
from common.common_parameter import CommonParameter


class CppCompileChecker:
    def __init__(self, build_directory):
        self.cpp_build_command = "g++"
        self.cpp_message_compile_only = "-c"
        self.check_cpp_compiler_exists_keyword = "gcc version "
        self.main_cpp_file_name = "cpp_compile_checker_main.cpp"
        self.cpp_exe_file_name_option = "-o"
        self.cpp_compile_checker_exe_name = "cpp_compile_checker_exe"

        self.build_directory = os.path.abspath(build_directory)

        self.compiler_exists = self.check_mingw_compiler_exists()

    def check_mingw_compiler_exists(self):
        version_message = subprocess.run(
            "g++ -v", capture_output=True, text=True)

        message = version_message.stderr.split("\n")

        if self.check_cpp_compiler_exists_keyword in message[-1] == -1:
            compiler_exists = False
        else:
            compiler_exists = True

        return compiler_exists

    def compile_cpp_file_and_get_error_message(self, cpp_file_name):
        message = self.compile_cpp_file(cpp_file_name)

        message_lines = message.split("\n")
        message_out = ""
        for i, line in enumerate(message_lines):
            if " error: " in line:
                message_out += line + "\n"

        return message_out

    def link_cpp_file_and_get_undefined_multiple_message(self, cpp_file_name):
        message = self.link_cpp_file(cpp_file_name)

        message_lines = message.split("\n")
        message_out = ""
        for i, line in enumerate(message_lines):
            if " undefined reference to " in line:
                message_out += line + "\n"
            elif " multiple definition of " in line:
                message_out += line + "\n"

        return message_out

    def compile_cpp_file(self, cpp_file_name):
        current_directory = os.getcwd()
        os.chdir(self.build_directory)

        command = self.cpp_build_command + " " \
            + self.cpp_message_compile_only + " " \
            + cpp_file_name

        subprocess_output = subprocess.run(
            command, capture_output=True, text=True)

        os.chdir(current_directory)

        run_message = subprocess_output.stderr

        return run_message

    def link_cpp_file(self, cpp_file_name):
        self.create_main_cpp_file()
        self.add_cpp_file_header_include_to_main_cpp_file(cpp_file_name)

        current_directory = os.getcwd()
        os.chdir(self.build_directory)

        command = self.cpp_build_command + " " \
            + self.main_cpp_file_name + " " \
            + cpp_file_name + " " \
            + CommonParameter.python_export_libraries_link_text + " " \
            + self.cpp_exe_file_name_option + " " \
            + self.cpp_compile_checker_exe_name

        subprocess_output = subprocess.run(
            command, capture_output=True, text=True)

        os.chdir(current_directory)

        run_message = subprocess_output.stderr

        return run_message

    def is_compiler_exists(self):
        return self.compiler_exists

    def create_main_cpp_file(self):
        current_directory = os.getcwd()
        os.chdir(self.build_directory)

        with open(self.main_cpp_file_name, "w") as file:
            file.write("int main(void) {\n")
            file.write("    return 0;\n")
            file.write("}\n")

        os.chdir(current_directory)

    def add_cpp_file_header_include_to_main_cpp_file(self, cpp_file_name):
        header_name = cpp_file_name.split(".")[0] + ".hpp"

        current_directory = os.getcwd()
        os.chdir(self.build_directory)

        main_cpp_file = ""
        with open(self.main_cpp_file_name, "r") as file:
            main_cpp_file = file.read()
        with open(self.main_cpp_file_name, "w") as file:
            text = "#include \"" + header_name + "\"\n\n" + main_cpp_file
            file.write(text)

        os.chdir(current_directory)
