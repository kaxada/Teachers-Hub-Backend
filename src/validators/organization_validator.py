class ValidateOrganization:
    """validates the organizations added to the database

    Returns:
        [boolean] -- [returns true for valid fields and false for invalid
                    fields]
    """

    def __init__(self, data):
        self.data = data

    def validate_organization_name(self):
        """validates the organization name

        Returns:
            [True] -- [returns true for valid organization name else false]
        """
        try:
            if self.data['organization_name'] == "" or \
               not isinstance(self.data['organization_name'], str):
                return False
            else:
                return True
        except KeyError:
            return False
