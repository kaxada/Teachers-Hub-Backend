class ModuleValidator:
    def __init__(self, data):
        self.data = data


    def validate_module_fields(self):
        """Validates module details"""
        module_fields = ["module_title","module_description","module_content"]
        for field in module_fields:
            if not self.data[field]:
                return field + " cannot be blank"
            if field not in self.data.keys():
                return field + " is missing"
            if not isinstance(self.data[field], str):
                return "Enter string value at {}".format(field)

    def is_valid(self):
        """combines all field validation"""
        if isinstance(self.validate_module_fields(), str):
            return self.validate_module_fields()
        else:
            return "valid"
