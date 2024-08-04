import tkinter as tk
from tkinter import filedialog
from common.language_type import LanguageType


class GetCodeFilePath:
    def __init__(self) -> None:
        pass

    def get_file_path():
        root = tk.Tk()
        root.attributes('-topmost', True)
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Select file", filetypes=[
            ("All file", "*.*")])
        if file_path == "":
            raise ValueError("file path is empty")

        file_path, file_name, file_type = GetCodeFilePath.output_file_info(
            file_path)

        return file_path, file_name, file_type

    def get_file_path_with_arg(file_path):
        file_path, file_name, file_type = GetCodeFilePath.output_file_info(
            file_path)

        return file_path, file_name, file_type

    @staticmethod
    def output_file_info(file_path):
        file_path_lines = file_path.split("/")
        file_name_ext = file_path_lines[-1].split(".")

        file_name = file_name_ext[0]

        file_type = LanguageType.CPP
        if file_name_ext[1] == "py":
            file_type = LanguageType.Python
        elif file_name_ext[1] == "cs":
            file_type = LanguageType.CS
        elif file_name_ext[1] == "cpp":
            file_type = LanguageType.CPP
        else:
            raise ValueError("invalid file extension")

        return file_path, file_name, file_type
