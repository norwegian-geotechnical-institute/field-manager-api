import pytest
from field_manager_api.field_manager import FieldManagerAPI


def test_set_token_permission_error():
    fm = FieldManagerAPI()
    token = "your_invalid_token"  # Use an invalid or expired token
    fm.set_token(token)

    # Ensure that the PermissionError is raised when fm.get_projects is called
    with pytest.raises(
        PermissionError, match="Token authorization failed \(401 Unauthorized\)"
    ):
        fm.get_list_of_all_projects()
