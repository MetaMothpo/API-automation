import requests

def test_fact_length_matches_actual_length():
    """Test if the length of the fact matches the 'length' field in the response."""
    print("Running test: test_fact_length_matches_actual_length")
    url = "https://catfact.ninja/fact"
    response = requests.get(url)

    # Check if status code is 200
    if response.status_code != 200:
        print(f"Error: Expected 200, but got {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    json_data = response.json()

    # Verify the length of the fact matches the length field
    fact = json_data.get("fact", "")
    length = json_data.get("length", 0)

    print(f"Fact: {fact}")
    print(f"Expected Length: {length}")
    print(f"Actual Length: {len(fact)}")

    # Check if the length matches
    assert len(fact) == length, f"Expected length {length}, but got {len(fact)}"

# Final print to confirm the script ran
print("Script finished running.")

