import os
import json
from networkx.readwrite import json_graph


class DependencyAnalyzer:
    def __init__(self, directory) -> None:
        self.files_directory = directory
        self.files_to_analyze_list = []

        self.dependency_graph = None
        self.node_link_data = None

    def get_files(self, directory, extension):
        self.files_directory = directory

        self.files_to_analyze_list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    self.files_to_analyze_list.append(os.path.join(root, file))

    def get_relative_path(self, file, files_directory):
        return os.path.relpath(file, files_directory)

    def join_path(self, directory_name, file_name):
        return os.path.join(directory_name, file_name)

    def generate_graph_to_json_format(self):
        self.node_link_data = json_graph.node_link_data(self.dependency_graph)

    def save_graph_to_json(self, json_file_name):
        if None != self.node_link_data:
            json_path = self.join_path(self.files_directory,
                                       json_file_name)
            with open(json_path, 'w') as f:
                json.dump(self.node_link_data, f, indent=2)

    def get_node_link_data(self):
        return self.node_link_data
