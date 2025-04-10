# cli_test_model.py

import argparse
from helpers.ai_model_wrapper import AIModelWrapper

def main():
    parser = argparse.ArgumentParser(description="Test AI model wrapper via CLI")
    parser.add_argument("--backend", type=str, required=True, help="Backend (openai or huggingface)")
    parser.add_argument("--prompt", type=str, required=True, help="Prompt to generate response from")
    parser.add_argument("--api_key", type=str, help="API key for OpenAI (required if using openai backend)")

    args = parser.parse_args()
    wrapper = AIModelWrapper(backend=args.backend, api_key=args.api_key)
    result = wrapper.generate(args.prompt)
    print("\nGenerated Response:\n", result)

if __name__ == "__main__":
    main()
