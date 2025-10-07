import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()

    args = sys.argv[1:]
    verbose = False

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if "--verbose" in args:
        verbose = True
        args.remove("--verbose")

    user_prompt = " ".join(args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, user_prompt, verbose)

def generate_content(client, messages, user_prompt, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt),
    )
    #if verbose:
    #    print("User prompt:", user_prompt)
    #    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    #    print("Response tokens:", response.usage_metadata.candidates_token_count)
    #    print("Response:")
    #if response.function_calls:
    #    for function_call in response.function_calls:
    #        print(f"Calling function: {function_call.name}({function_call.args})")
    #else:
    #    print(response.text)
    if response.function_calls:    
        for function_call in response.function_calls:
            result = call_function(function_call, verbose)
            if not result.parts[0].function_response.response:
                raise Exception("fatal error")
            if verbose:
                print(f"-> {result.parts[0].function_response.response}")

if __name__ == "__main__":
    main()
