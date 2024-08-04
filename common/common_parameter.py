from common.language_type import LanguageType
from generative_ai.generative_ai_type import GenerativeAIType


class CommonParameter:
    generate_class_info_iteration_max = 3
    generative_ai_communication_iteration_max = 3
    compile_check_and_revise_iteration_max = 5
    static_analysis_and_revise_iteration_max = 3

    generative_ai_type = GenerativeAIType.ollama

    with open('./common/prompt/analyze_python_code_properties_pre_prompt.txt', 'r', encoding='utf-8') as file:
        analyze_python_code_properties_pre_prompt = file.read()
    with open('./common/prompt/analyze_python_code_methods_pre_prompt.txt', 'r', encoding='utf-8') as file:
        analyze_python_code_methods_pre_prompt = file.read()

    with open('./common/prompt/analyze_cs_code_pre_prompt.txt', 'r', encoding='utf-8') as file:
        analyze_cs_code_pre_prompt = file.read()

    with open('./common/prompt/example_python_code_to_json.txt', 'r', encoding='utf-8') as file:
        example_python_code_to_json = file.read()
    with open('./common/prompt/example_omit_description_of_detailed_processing.txt', 'r', encoding='utf-8') as file:
        example_omit_description_of_detailed_processing = file.read()

    with open('./common/prompt/generate_cpp_header_from_python_code_pre_prompt.txt', 'r', encoding='utf-8') as file:
        generate_cpp_header_from_python_code_pre_prompt = file.read()
    with open('./common/prompt/generate_cpp_source_from_python_code_pre_prompt.txt', 'r', encoding='utf-8') as file:
        generate_cpp_source_from_python_code_pre_prompt = file.read()

    with open('./common/prompt/generate_cpp_header_from_cs_code_pre_prompt.txt', 'r', encoding='utf-8') as file:
        generate_cpp_header_from_cs_code_pre_prompt = file.read()
    with open('./common/prompt/generate_cpp_source_from_cs_code_pre_prompt.txt', 'r', encoding='utf-8') as file:
        generate_cpp_source_from_cs_code_pre_prompt = file.read()

    with open('./common/prompt/generate_cs_skelton_from_python_code_pre_prompt.txt', 'r', encoding='utf-8') as file:
        generate_cs_skelton_from_python_code_pre_prompt = file.read()
    with open('./common/prompt/generate_cs_body_from_python_code_pre_prompt.txt', 'r', encoding='utf-8') as file:
        generate_cs_body_from_python_code_pre_prompt = file.read()

    with open('./common/prompt/generate_python_skelton_from_cs_code_pre_prompt.txt', 'r', encoding='utf-8') as file:
        generate_python_skelton_from_cs_code_pre_prompt = file.read()
    with open('./common/prompt/generate_python_body_from_cs_code_pre_prompt.txt', 'r', encoding='utf-8') as file:
        generate_python_body_from_cs_code_pre_prompt = file.read()

    with open('./common/prompt/generate_cpp_header_from_python_diff_pre_prompt.txt', 'r', encoding='utf-8') as file:
        generate_cpp_header_from_python_diff_pre_prompt = file.read()
    with open('./common/prompt/generate_cpp_source_from_python_diff_pre_prompt.txt', 'r', encoding='utf-8') as file:
        generate_cpp_source_from_python_diff_pre_prompt = file.read()

    with open('./common/prompt/cpp_header_compile_error_and_rewrite_message.txt', 'r', encoding='utf-8') as file:
        cpp_header_compile_error_and_rewrite_message = file.read()
    with open('./common/prompt/cpp_source_compile_error_and_rewrite_message.txt', 'r', encoding='utf-8') as file:
        cpp_source_compile_error_and_rewrite_message = file.read()

    with open('./common/prompt/cpp_header_static_analysis_error_and_rewrite_message.txt', 'r', encoding='utf-8') as file:
        cpp_header_static_analysis_error_and_rewrite_message = file.read()
    with open('./common/prompt/cpp_source_static_analysis_error_and_rewrite_message.txt', 'r', encoding='utf-8') as file:
        cpp_source_static_analysis_error_and_rewrite_message = file.read()

    with open('./common/prompt/other_classes_imported_message.txt', 'r', encoding='utf-8') as file:
        other_classes_imported_message = file.read()

    json_format_example_message = "Json format example is below:"
    omit_description_example_message = "The example of creating skelton code is below:"
    class_structure_message = "The analyzed class structure is below:"
    imports_of_python_code_message = "The imports of Python code are below:"
    imports_of_cs_code_message = "The imports of C# code are below:"
    original_code_message = "The original code is below:"
    header_file_name_message = "The header file name is below:"
    header_file_message = "The header file is below:"
    skelton_code_message = "The skelton code is below:"

    original_python_code_message = "Info 1, Original Python code is below."
    original_cpp_header_message = "Info 2, Original C++ header code is below."
    original_cpp_source_message = "Info 2, Original C++ source code is below."
    modified_python_code_message = "Info 3, Modified Python code is below."
    modified_header_code_message = "Info 4, Modified C++ header code is below."

    python_space_amount = 4
    json_space_amount = 1

    python_methods_structure_info_file_name = "python_methods_structure_info.json"
    python_properties_structure_info_file_name = "python_properties_structure_info.json"
    python_import_info_file_name = "python_import_info.txt"

    python_export_libraries_text = "#include \"python_libraries.hpp\""
    python_export_libraries_link_text = "python_libraries.cpp"
    python_export_libraries_file_names = [
        "python_libraries.hpp", "python_libraries.cpp"]
    python_export_libraries_path = "export_libraries/"

    @staticmethod
    def get_ext_from_type(language_type):
        if LanguageType.CPP == language_type:
            return ".cpp"
        elif LanguageType.CS == language_type:
            return ".cs"
        elif LanguageType.Python == language_type:
            return ".py"

    @staticmethod
    def get_skelton_ext_from_type(language_type):
        if LanguageType.CPP == language_type:
            return ".hpp"
        elif LanguageType.CS == language_type:
            return ".cs"
        elif LanguageType.Python == language_type:
            return ".py"
