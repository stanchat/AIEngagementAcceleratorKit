# validate_model_response.py

import json

def validate_response(response: str) -> bool:
    """Basic CI validation for model output."""
    if not response:
        print("❌ Empty response.")
        return False
    if len(response.split()) < 3:
        print("❌ Response too short.")
        return False
    if "error" in response.lower():
        print("❌ Response contains error message.")
        return False
    print("✅ Response looks good.")
    return True

# Example usage
if __name__ == "__main__":
    example_output = "AI will change the future of work dramatically by automating..."
    validate_response(example_output)
