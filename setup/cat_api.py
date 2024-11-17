from modules.helper import CatAPIHelper
from modules.root.base_api import BaseApi
from modules.routes.cat_api_routes import Routes
from modules.dataclass_collection import TestArgsApi


class CatAPISuite:
    def __init__(self, args: TestArgsApi):
        self.test_args = args
        self.__base = BaseApi()
        self.__routes = Routes()
        self.cat_api = CatAPIHelper(
            test_args=self.test_args,
            base_api=self.__base,
            routes=self.__routes
        )
