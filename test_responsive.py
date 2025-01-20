import requests

def test_response_time_and_content_type():
    """Test if the response time is less than 500ms and Content-Type is application/json."""
    print("Running test: test_response_time_and_content_type")
    
    url = "https://catfact.ninja/fact"
    response = requests.get(url)

    # Print the actual response time and content type for visibility
    print(f"Response Time: {response.elapsed.total_seconds()} seconds")
    content_type = response.headers.get("Content-Type", "")
    print(f"Content-Type: {content_type}")

    # Check response time is less than 500ms
    assert response.elapsed.total_seconds() < 0.5, f"Response time exceeded 500ms: {response.elapsed.total_seconds()}s"

    # Check Content-Type is application/json
    assert "application/json" in content_type, f"Expected Content-Type 'application/json', but got '{content_type}'"

# Final print to confirm the script ran
print("Script finished running.")
