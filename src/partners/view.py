from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..validators.organization_validator import ValidateOrganization
from .controller import OrganizationController
from ..users.controller import UserController

organization = Blueprint('organization', __name__)
organization_controller = OrganizationController()
user_controller = UserController()


@organization.route('/api/v1/organizations', methods=['POST'])
@jwt_required
def add_new_organization():
    """Registers an Organization."""
    data = request.get_json()

    if data:
        if not user_controller.check_admin_user():
            return jsonify({"message": "only Admins allowed"}), 401
        validate_organization = ValidateOrganization(data)
        if validate_organization.validate_organization_name():
            if not organization_controller.check_duplicate_organization(data):
                organization_controller.create_organization(data)
                return jsonify({"message": "organization added successfully"}), 200
            else:
                return jsonify({"message": "organization already exists"}), 400
        else:
            return jsonify({"message": "enter valid organization name"}), 400
    else:
        return jsonify({"message": "organization details not provided"}), 400


@organization.route('/api/v1/organizations/<organization_id>', methods=['DELETE'])
@jwt_required
def delete_organization(organization_id):
    """
    Function enables admin to delete an Organization from the database.

    """
    try:
        if not user_controller.check_admin_user():
            return jsonify({"message": "only Admins allowed"}), 401
        organization_id = int(organization_id)
        if not organization_controller.query_organization(organization_id):
            return jsonify({
                'message': 'Organization does not exist in database'
            }), 400

        organization_controller.delete_organization(organization_id)
        return jsonify({
            'message': 'Organization deleted!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The organization id should be an integer!'
        }), 400


@organization.route('/api/v1/organizations/<organization_id>', methods=['GET'])
def view_organization(organization_id):
    """
    Function enables user to view an Organization from the database.
    """
    try:
        organization_id = int(organization_id)
        if not organization_controller.query_organization(organization_id):
            return jsonify({
                'message': 'Organization does not exist in database'
            }), 400
        organization = organization_controller.query_organization(organization_id)
        return jsonify({
            'organization': {
                'organization_id': organization[0],
                'organization_name': organization[1]
            },
            'message': 'organization fetched!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The organization id should be an integer!'
        }), 400


@organization.route('/api/v1/organizations/<organization_id>', methods=['PUT'])
@jwt_required
def update_organization(organization_id):
    """
    Function enables user to modify an Organization from the database.
    """
    data = request.get_json()

    if data:
        if not user_controller.check_admin_user():
            return jsonify({"message": "only Admins allowed"}), 401
        validate_organization = ValidateOrganization(data)
        try:
            organization_id = int(organization_id)
            if not organization_controller.query_organization(organization_id):
                return jsonify({
                    'message': 'Organization does not exist in database'
                }), 400
            elif validate_organization.validate_organization_name():
                    organization_controller.update_organization(data, organization_id)
                    return jsonify({"message": "organization updated successfully"}), 200
            else:
                return jsonify({"message": "enter valid organization name"}), 400
        except ValueError:
            return jsonify({"message": "organization id should be an integer"}), 400
        except Exception:
            return jsonify({"message": "organization exists already"}), 400
    else:
        return jsonify({"message": "organization details not provided"}), 400


@organization.route('/api/v1/organizations', methods=['GET'])
def view_all_organizations():
    """
    Function enables user to view all the available organizations from the database.
    """
    if not organization_controller.query_all_organizations():
        return jsonify({
            'message': 'No available organizations in the database'
        }), 400
    organizations = organization_controller.query_all_organizations()
    return jsonify({
        'organizations': organizations,
        'message': 'organizations fetched!'
    }), 200
