import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from prompts import system_prompt
from call_functions import available_functions, call_function

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

    messages : list[ChatCompletionMessageParam] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    for _ in range(20):
        response = client.chat.completions.create(
            model='openrouter/free', 
            messages = messages, 
            tools = available_functions,
            )
        response_usage = response.usage
        if response_usage is None:
            raise RuntimeError('Response has no usage. Check if API request went through.')
            
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response_usage.prompt_tokens}")
            print(f"Response tokens: {response_usage.completion_tokens}")    

        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls is not None:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call,args.verbose)
                messages.append(result_message)
                if result_message["content"] is None:
                    raise Exception(f"Error: The tool call '{tool_call.function.name}' with arguments "
                                    f"'{tool_call.function.arguments}' was unsuccessfull."
                                    )
                if args.verbose:
                    print(f"-> {result_message['content']}")
                
                
        else:
            print(response.choices[0].message.content)
            return
    print("Exceded Ai-Agents loop iterations.")
    main.exit(1)


if __name__ == "__main__":
    main()
