import requests

def test_status_code_is_200():
    """Test if the API returns status code 200."""
    print("Running test: test_status_code_is_200")
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Expected 200, but got {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

def test_response_has_fact_and_length_properties():
    """Test if the API response contains 'fact' and 'length' properties."""
    print("Running test: test_response_has_fact_and_length_properties")
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Expected 200, but got {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    json_data = response.json()
    
    assert "fact" in json_data, "'fact' key not found in response"
    assert "length" in json_data, "'length' key not found in response"

# Final print to confirm script ran
print("Script finished running.")
