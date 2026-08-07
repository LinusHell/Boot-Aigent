import os
from dotenv import load_dotenv
from openai import OpenAI

import argparse



    

def main() -> None:
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key == None:
        raise RuntimeError('No api_key found!')

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )   

    parser = argparse.ArgumentParser(description="Boots-Aigent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    response = client.chat.completions.create(model='openrouter/free',messages = messages)
    response_usage = response.usage
    if response_usage is None:
        raise RuntimeError('Response has no usage. Check if API request went through.')
        
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response_usage.prompt_tokens}")
        print(f"Response tokens: {response_usage.completion_tokens}")    
    print(response.choices[0].message.content)
    


if __name__ == "__main__":
    main()
