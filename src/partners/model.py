class Organization:

    """Describes the attributes of an organization."""
    def __init__(self, **kwargs):
        """Initializes the organization model."""
        self.organization_name = kwargs.get('organization_name')

