from src.users.controller import (cur, conn)


class OrganizationController:
    """Organization controller interfaces with the database."""

    def __init__(self):
        """Initializes the organizations controller class."""
        conn.create_organizations_table()

    @staticmethod
    def create_organization(data):
        """Creates an organization."""
        sql = """INSERT INTO organizations(organization_name)
                        VALUES ('{}')"""
        sql_command = sql.format(data['organization_name'])
        cur.execute(sql_command)

    @staticmethod
    def delete_organization(organization_id):
        ''' Deletes an organization '''
        sql = """ DELETE FROM organizations WHERE OrganizationID ='{}'"""
        sql_command = sql.format(organization_id)
        cur.execute(sql_command)

    @staticmethod
    def query_organization(organization_id):
        ''' selects an organization from the database '''
        sql = """ SELECT * FROM organizations  WHERE OrganizationID ='{}' """
        sql_command = sql.format(organization_id)
        cur.execute(sql_command)
        row = cur.fetchone()
        return row

    @staticmethod
    def check_duplicate_organization(data):
        """Checks if organization already exists"""
        sql = """SELECT * FROM organizations WHERE organization_name='{}'"""
        cur.execute(sql.format(data['organization_name']))
        row = cur.fetchone()
        if row:
            return True
        else:
            return False

    @staticmethod
    def update_organization(data, organization_id):
        """Updates an organization."""
        sql = """UPDATE organizations SET organization_name='{}'\
        WHERE OrganizationID='{}'"""
        sql_command = sql.format(data['organization_name'], organization_id)
        cur.execute(sql_command)
        sql = """ SELECT * FROM organizations  WHERE OrganizationID ='{}' """
        sql_command = sql.format(organization_id)
        cur.execute(sql_command)
        row = cur.fetchone()
        if row:
            return row

    @staticmethod
    def query_all_organizations():
        ''' selects all available organizations from the database '''
        organizations = []
        sql = """ SELECT * FROM organizations  """
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            organizations.append({
                "organization_id": row[0],
                "organization_name": row[1]
            })
        return organizations
