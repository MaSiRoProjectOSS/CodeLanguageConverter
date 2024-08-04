import re
import networkx as nx
from converter.analyzer.dependency.dependency_analyzer import DependencyAnalyzer


class PythonDependencyAnalyzer(DependencyAnalyzer):
    def __init__(self, files_directory):
        super().__init__(files_directory)

        self.extension = ".py"
        self.dependency_graph_file_name = "python_dependency_graph.json"

    def get_python_files(self):
        self.get_files(self.files_directory, self.extension)

    def extract_python_imports(self, file_path):
        imports = []
        with open(file_path, 'r') as file:
            content = file.read()

            imports.extend(re.findall(r'^import (\S+)', content, re.MULTILINE))
            imports.extend(re.findall(
                r'^from (\S+) import', content, re.MULTILINE))

        return imports

    def build_dependency_graph(self):
        self.dependency_graph = nx.DiGraph()

        for file in self.files_to_analyze_list:
            file_name = self.get_relative_path(file, self.files_directory)
            imports = self.extract_python_imports(file)
            for imp in imports:
                imp_file = imp.replace('.', '/') + self.extension
                for to_file in self.files_to_analyze_list:
                    if imp_file in to_file:
                        self.dependency_graph.add_edge(file_name, imp_file)

        self.generate_graph_to_json_format()

    def save_python_dependency_graph(self):
        self.save_graph_to_json(self.dependency_graph_file_name)
