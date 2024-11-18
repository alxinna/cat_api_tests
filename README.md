# Cat API Test Automation Framework
This repository contains a test suite for TheCatAPI, which provides access to random cat images, breed information, and more.

## Setup Instructions
### Prerequisites:
- Python 3.x
- pip (Python package installer)
### 1. Clone the repository:
```commandline
git clone https://github.com/alxinna/cat_api_tests.git
cd cat_api_tests
```

### 2. Install dependencies:

Make sure to create a virtual environment (optional but recommended) and install the required dependencies.
```commandline
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Setting up the API Key
TheCatAPI requires an API key for some endpoints. To set up your API key:

1. Sign up for an API key at TheCatAPI.
2. Create .env file in root directory of the project and replace YOUR_API_KEY in the .env file with your actual API key.
Example .env file:
```commandline
API_KEY=your-api-key-here
```

## Test Cases Overview:
**test_search_images**: Verifies the functionality of searching for cat images using the /images/search endpoint with different parameters.

**test_get_image_by_id**: Validates that an individual image can be retrieved by its ID via the /images/{image_id} endpoint.

**test_favourite_post_get_delete**: Tests the functionality of favoriting a cat image, retrieving the favorite by its id, and deleting a favorite via POST, GET, and DELETE requests.
### Test Cases
#### 1. test_search_images

**Objective**: Verify that searching for cat images via the /images/search endpoint works as expected.

**Steps**:

1. Send a GET request to /images/search with parameters size, mime_types, has_breeds and limit.
2. Ensure the id, url, width, height, and breeds fields are present and correct.


#### 2. test_get_image_by_id
**Objective**: Validate that an individual image can be retrieved by its ID via /images/{image_id}.

**Steps**:

1. Send a GET request to /images/{image_id} using a valid image ID.
2. Validate that the id in the response matches the requested image_id.

#### 3. test_favourite_post_get_delete
**Objective**: Verify the functionality of favoriting a cat image, retrieving the favorite by id, and deleting a favorite.

**Steps**:

1. POST: Send a POST request to /favourites to favorite a cat image.
2. Verify that the image is added to the favorites list after the POST request.
3. GET: Retrieve the list of favorite images using the /favourites/:favourite_id endpoint.
4. Verify that a favourite has the same image_id as in POST request.
5. DELETE: Send a DELETE request to remove the favorite image from the list.
6. Confirm that the image is removed from the favorites list after the DELETE request.

## Running the Tests
### 1. Run All Tests with pytest:
```commandline
pytest --html=report.html
```
This command will run all the tests in the repository and generate an HTML report named report.html in the current directory.

### 2. Run Specific Test:
To run a specific test case, use different marks:
```commandline
pytest -m "api_tests"
```
Replace api_tests with the name of the mark which is used in test cases you want to run.
