def assert_valid_response(response, expected_fields):
    """
    Validates the response structure for cat images or any other response.

    Args:
        response (list): The list of items to validate (e.g., cat images).
        expected_fields (dict): A dictionary where keys are field names to check,
                                 and values are the expected data type or validation rule.

    Raises:
        AssertionError: If any validation fails.
    """

    # Check if the response is not empty
    assert len(response) > 0, "Response is empty"

    type_map = {
        "str": str,
        "int": int,
        "list": list
    }

    for item in response:
        # Validate presence of expected fields and their data types
        for field, expected_type in expected_fields.items():
            assert field in item, f"Missing '{field}' in response"
            assert isinstance(item[field],
                              type_map.get(expected_type)), f"'{field}' should be of type {expected_type.__name__}, but found {type(item[field]).__name__}"

        # Additional validation for 'breeds' if it exists
        if 'breeds' in item:
            for breed in item['breeds']:
                # Validate breed fields if present
                assert "id" in breed and isinstance(breed["id"], str), "Breed 'id' is missing or not a string"
                assert "name" in breed and isinstance(breed["name"], str), "Breed 'name' is missing or not a string"
                assert "life_span" in breed and isinstance(breed["life_span"],
                                                           str), "Breed 'life_span' is missing or not a string"
