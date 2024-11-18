import pytest

from modules.assertions import assert_valid_response


@pytest.mark.api_tests
class TestCoreFunctionality:

    @pytest.fixture(autouse=True)
    def __get_fixture(self, cat_api):
        self.app = cat_api

    @pytest.mark.params_from_file(filename="test_search_images.json")
    def test_search_images(self, test_parameter):
        input_data, expected_result = test_parameter["input_data"], test_parameter["expected_result"]

        response = self.app.cat_api.search_images(is_authorised=True,
                                                  size=input_data['size'],
                                                  mime_types=input_data['mime_types'],
                                                  has_breeds=input_data['has_breeds'],
                                                  limit=input_data['limit'])

        assert_valid_response(response, expected_result['expected_fields'])

    @pytest.mark.params_from_file(filename="test_get_image_by_id.json")
    def test_get_image_by_id(self, test_parameter):
        input_data = test_parameter["input_data"]

        response = self.app.cat_api.get_image_by_id(image_id=input_data['image_id'])

        assert response['id'] == input_data['image_id'], \
            f"'id' mismatch: expected '{input_data['image_id']}', but got '{response['id']}'"

    @pytest.mark.params_from_file(filename="test_favourite_post_get_delete.json")
    def test_favourite_post_get_delete(self, test_parameter):
        input_data = test_parameter["input_data"]

        post_response = self.app.cat_api.post_favourites(image_id=input_data['image_id'],
                                                         sub_id=input_data['sub_id'])

        assert post_response['message'] == 'SUCCESS', "Favourites was not posted successfully."

        get_response = self.app.cat_api.get_favourite_by_id(favourite_id=post_response['id'])

        assert get_response['image_id'] == input_data['image_id'], f"'image_id' mismatch: expected '{input_data['image_id']}', but got '{get_response['image_id']}'"

        delete_response = self.app.cat_api.delete_favourite_by_id(favourite_id=post_response['id'])
        assert delete_response['message'] == 'SUCCESS', "Favourite was not deleted successfully."
