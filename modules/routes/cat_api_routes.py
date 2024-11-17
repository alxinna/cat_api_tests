from dataclasses import dataclass


@dataclass
class _Images:
    search_image: str = '/images/search'
    get_image_by_id: str = '/images/{image_id}'
    upload_image: str = '/images/upload'


@dataclass
class _Favourites:
    post_favourites: str = '/favourites'
    get_favourite_by_id: str = '/favourites/{favourite_id}'
    delete_favourite_by_id: str = '/favourites/{favourite_id}'


@dataclass
class Routes:
    images = _Images()
    favourites = _Favourites()
