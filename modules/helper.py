from modules.root.base_api import BaseApi
from modules.routes.cat_api_routes import Routes
from modules.dataclass_collection import TestArgsApi


class CatAPIHelper:
    def __init__(self,
                 test_args: TestArgsApi,
                 base_api: BaseApi,
                 routes: Routes):
        self.test_args = test_args
        self.base = base_api
        self.routes = routes

    def search_images(self,
                      is_authorised: bool = False, size: str = None, mime_types: str = None, format: str = None,
                      has_breeds: bool = None, order: int = None, page: int = None, limit: int = None,
                      include_breeds: int = None, include_categories: int = None) -> dict:
        if is_authorised:
            self.test_args.default_headers['x-api-key'] = self.test_args.api_key

        response = self.base.get(
            url=f'{self.test_args.base_url}{self.routes.images.search_image}',
            params={'size': size, 'mime_types': mime_types, 'format': format,
                    'has_breeds': has_breeds, 'order': order, 'page': page, 'limit': limit,
                    'include_breeds': include_breeds, 'include_categories': include_categories},
            headers=self.test_args.default_headers
        )

        if response.status_code != 200:
            raise Exception(f'The search_images GET status code = {response.status_code}')

        return response.json

    def get_image_by_id(self, image_id: str, is_authorised: bool = None) -> dict:
        if is_authorised:
            self.test_args.default_headers['x-api-key'] = self.test_args.api_key

        response = self.base.get(
            url=f'{self.test_args.base_url}{self.routes.images.get_image_by_id.format(image_id=image_id)}',
            headers=self.test_args.default_headers
        )

        if response.status_code != 200:
            raise Exception(f'The get_image_by_id GET status code = {response.status_code}')

        return response.json

    def upload_image(self, file: str, sub_id: str = None, breed_ids: str = None, is_authorised: bool = None) -> dict:
        if is_authorised:
            self.test_args.default_headers['x-api-key'] = self.test_args.api_key

        response = self.base.post(
            url=f'{self.test_args.base_url}{self.routes.images.upload_image}',
            body={
                'file': file,
                'sub_id': sub_id,
                'breed_ids': breed_ids
            },
            headers=self.test_args.default_headers
        )

        if response.status_code != 200:
            raise Exception(f'The get_image_by_id GET status code = {response.status_code}')

        return response.json

    def post_favourites(self, image_id: str, sub_id: str = None) -> dict:
        self.test_args.default_headers['x-api-key'] = self.test_args.api_key

        response = self.base.post(
            url=f'{self.test_args.base_url}{self.routes.favourites.post_favourites}',
            body={
                "image_id": image_id,
                "sub_id": sub_id
            },
            headers=self.test_args.default_headers
        )

        if response.status_code != 200:
            raise Exception(f'The post_favourites POST status code = {response.status_code}')

        return response.json

    def get_favourite_by_id(self, favourite_id: str) -> dict:
        self.test_args.default_headers['x-api-key'] = self.test_args.api_key

        response = self.base.get(
            url=f'{self.test_args.base_url}{self.routes.favourites.get_favourite_by_id.format(favourite_id=favourite_id)}',
            headers=self.test_args.default_headers
        )

        if response.status_code != 200:
            raise Exception(f'The get_favourite_by_id GET status code = {response.status_code}')

        return response.json

    def delete_favourite_by_id(self, favourite_id: str) -> dict:
        self.test_args.default_headers['x-api-key'] = self.test_args.api_key

        response = self.base.delete(
            url=f'{self.test_args.base_url}{self.routes.favourites.delete_favourite_by_id.format(favourite_id=favourite_id)}',
            headers=self.test_args.default_headers
        )

        if response.status_code != 200:
            raise Exception(f'The delete_favourite_by_id DELETE status code = {response.status_code}')

        return response.json
