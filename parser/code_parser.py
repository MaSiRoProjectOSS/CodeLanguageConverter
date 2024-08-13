import json
from parser.property_info import PropertyInfo
from parser.method_info import MethodInfo
from parser.class_info import ClassInfo


class CodeParser:
    def __init__(self, original_code):
        self.original_code = original_code
        self.original_code_lines = original_code.split("\n")
        self.class_info = None
        self.class_methods_structure_info = ""
        self.class_properties_structure_info = ""

    def create_class_info(self, name, methods, properties, super_class_names):
        class_info = ClassInfo()
        class_info.name = name
        class_info.methods.append(methods)
        if (class_info.methods[0] == None):
            class_info.methods = class_info.methods[1:]
        class_info.properties.append(properties)
        if (class_info.properties[0] == None):
            class_info.properties = class_info.properties[1:]
        class_info.super_class_names.append(super_class_names)
        if (class_info.super_class_names[0] == None):
            class_info.super_class_names = class_info.super_class_names[1:]
        return class_info

    def create_property_info(self, name, data_type, initial_value, is_static, is_public):
        property_info = PropertyInfo()
        property_info.name = name
        property_info.data_type = data_type
        property_info.initial_value = initial_value
        property_info.is_static = is_static
        property_info.is_public = is_public
        return property_info

    def create_method_info(self, name, return_data_types,
                           return_names, argument_names,
                           argument_types, is_static, is_public, position):
        method_info = MethodInfo()
        method_info.name = name

        method_info.return_data_types.append(return_data_types)
        if (method_info.return_data_types[0] == None):
            method_info.return_data_types = method_info.return_data_types[1:]
        method_info.return_names.append(return_names)
        if (method_info.return_names[0] == None):
            method_info.return_names = method_info.return_names[1:]
        method_info.argument_names.append(argument_names)
        if (method_info.argument_names[0] == None):
            method_info.argument_names = method_info.argument_names[1:]
        method_info.argument_types.append(argument_types)
        if (method_info.argument_types[0] == None):
            method_info.argument_types = method_info.argument_types[1:]
        method_info.is_static = is_static
        method_info.is_public = is_public
        method_info.original_code_position = position

        return method_info

    def add_class_info_to_self(self, class_info: ClassInfo):
        self.class_info = class_info

    def add_property_info_to_self(self, property_info: PropertyInfo):
        if (self.class_info != None):
            self.class_info.properties.append(property_info)
            if (self.class_info.properties[0] == None):
                self.class_info.properties = self.class_info.properties[1:]

    def add_method_info_to_self(self, method_info: MethodInfo):
        if (self.class_info != None):
            self.class_info.methods.append(method_info)
            if (self.class_info.methods[0] == None):
                self.class_info.methods = self.class_info.methods[1:]

    def set_super_class_names(self, super_class_names):
        if (super_class_names is str and self.class_info != None):
            self.class_info.super_class_names.append(
                super_class_names)
            if (self.super_class_names[0] == None):
                self.super_class_names = self.super_class_names[1:]

        elif super_class_names is None:
            pass

        else:
            for i, val in enumerate(super_class_names):
                self.super_class_names.append(val)
                if (self.super_class_names[0] == None):
                    self.super_class_names = self.super_class_names[1:]

    def get_class_info(self):
        return self.class_info

    def update_class_methods_info_from_file(self, file_full_path: str):
        with open(file_full_path, 'r') as file:
            self.class_methods_structure_info = file.read()

        self.update_class_methods_data()

    def update_class_methods_data(self):
        json_data = json.loads(self.class_methods_structure_info)

        methods = json_data["methods"]

        for i, original_method in enumerate(self.class_info.methods):
            for j, import_method in enumerate(methods):
                if (original_method.name == import_method["name"]):
                    self.class_info.methods[i].return_data_types = import_method["return_data_types"]
                    self.class_info.methods[i].return_names = import_method["return_names"]
                    self.class_info.methods[i].argument_names = import_method["argument_names"]
                    self.class_info.methods[i].argument_types = import_method["argument_types"]

    def fill_blanks_in_class_methods_info(self, class_methods_structure_info: str):
        self.class_methods_structure_info = class_methods_structure_info

        self.fill_blanks_in_class_methods_data()

    def fill_blanks_in_class_methods_data(self):
        json_data = json.loads(self.class_methods_structure_info)

        methods = json_data["methods"]

        for i, original_method in enumerate(self.class_info.methods):
            for j, import_method in enumerate(methods):
                if (original_method.name == import_method["name"]):
                    if (self.class_info.methods[i].return_data_types == None):
                        self.class_info.methods[i].return_data_types = import_method["return_data_types"]
                    if (self.class_info.methods[i].return_names == None):
                        self.class_info.methods[i].return_names = import_method["return_names"]
                    if (self.class_info.methods[i].argument_names == None):
                        self.class_info.methods[i].argument_names = import_method["argument_names"]
                    if (self.class_info.methods[i].argument_types == None):
                        self.class_info.methods[i].argument_types = import_method["argument_types"]

    def update_class_properties_info_from_file(self, file_full_path: str):
        with open(file_full_path, 'r') as file:
            self.class_properties_structure_info = file.read()

        self.update_class_properties_data()

    def update_class_properties_info(self, class_properties_structure_info: str):
        self.class_properties_structure_info = class_properties_structure_info

        self.update_class_properties_data()

    def update_class_properties_data(self):
        json_data = json.loads(self.class_properties_structure_info)

        properties = json_data["properties"]

        for i, original_property in enumerate(self.class_info.properties):
            for j, import_property in enumerate(properties):
                property = properties["property_" + str(j + 1)]
                if (original_property.name == property["name"]):
                    import_property = properties["property_" + str(j + 1)]
                    if ("data_type" in import_property):
                        self.class_info.properties[i].data_type = property["data_type"]
                    if ("initial_value" in import_property):
                        self.class_info.properties[i].initial_value = property["initial_value"]
                    if ("is_public" in import_property):
                        self.class_info.properties[i].is_public = property["is_public"]
                    if ("is_static" in import_property):
                        self.class_info.properties[i].is_public = property["is_static"]

    def fill_blanks_in_class_properties_data(self):
        json_data = json.loads(self.class_properties_structure_info)

        properties = json_data["properties"]

        for i, original_property in enumerate(self.class_info.properties):
            for j, import_property in enumerate(properties):
                property = properties["property_" + str(j + 1)]
                if (original_property.name == property["name"]):
                    import_property = properties["property_" + str(j + 1)]
                    if ("data_type" in import_property) and (import_property["data_type"] == None):
                        self.class_info.properties[i].data_type = property["data_type"]
                    if ("initial_value" in import_property) and (import_property["initial_value"] == None):
                        self.class_info.properties[i].initial_value = property["initial_value"]
                    if ("is_public" in import_property) and (import_property["is_public"] == None):
                        self.class_info.properties[i].is_public = property["is_public"]
                    if ("is_static" in import_property) and (import_property["is_static"] == None):
                        self.class_info.properties[i].is_public = property["is_static"]

    def add_class_properties_info_from_file(self, file_full_path: str):
        with open(file_full_path, 'r') as file:
            self.class_methods_structure_info = file.read()

        self.add_class_properties_data()

    def add_class_properties_info(self, class_methods_structure_info: str):
        self.class_methods_structure_info = class_methods_structure_info

        self.add_class_properties_data()

    def add_class_properties_data(self):
        json_data = json.loads(self.class_methods_structure_info)

        properties = json_data["properties"]

        for i, import_property in enumerate(properties):
            name = None
            data_type = None
            initial_value = None
            is_static = None
            is_public = None

            property = properties["property_" + str(i + 1)]
            if "name" in property:
                name = property["name"]
            if "data_type" in property:
                data_type = property["data_type"]
            if "initial_value" in property:
                initial_value = property["initial_value"]
            if "is_static" in property:
                is_static = property["is_static"]

            properties_info = self.create_property_info(
                name, data_type, initial_value, is_static, is_public)
            self.add_property_info_to_self(properties_info)

    def get_class_methods_structure_info(self):
        return self.class_methods_structure_info

    def set_class_methods_structure_info(self, class_methods_structure_info):
        self.class_methods_structure_info = class_methods_structure_info

    def get_class_properties_structure_info(self):
        return self.class_properties_structure_info

    def set_class_properties_structure_info(self, class_properties_structure_info):
        self.class_properties_structure_info = class_properties_structure_info
