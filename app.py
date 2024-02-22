from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()



def estimate_cost(total_tokens):
    COST_PER_THOUSAND_TOKENS = 0.01
    return (total_tokens / 1000) * COST_PER_THOUSAND_TOKENS
    
def print_response(response):
    print(f"Response ID: {response.id}")
    total_tokens = response.usage.total_tokens
    print(f"Total Tokens Used: {total_tokens}")
    cost_estimate = estimate_cost(total_tokens)
    print(f"Estimated cost for completion: ${cost_estimate:.4f}")

    for choice in response.choices:
        print("*" * 200)
        print(f"Finish Reason: {choice.finish_reason}")
        print(f"Choice Index: {choice.index}")
        print(f"Message Content: {choice.message.content}")
        print(f"Message Role: {choice.message.role}")
        print(f"Function Call: {choice.message.function_call}")

        if choice.message.tool_calls:
            for tool_call in choice.message.tool_calls:
                print("-" * 100)
                print(f"Tool call ID: {tool_call.id}")
                print(
                    f"Tool function arguments: {json.loads(tool_call.function.arguments)}"
                )
                print(f"Tool function name: {tool_call.function.name}")
                print(f"Tool type: {tool_call.type}")
        else:
            print(f"Tools not required")
    print("*" * 200)

def make_openai_call(client, messages, json_response=False):
    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        response_format=(
            {"type": "json_object"} if json_response else {"type": "text"}
        ),
        messages=messages,
        temperature=0,
        seed=42,
    )
    print_response(response)
    return response.choices[0].message.content


AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
)

system_instructions = "you are an ai assistant"
question = "who are you?"
messages = [{"role": "system", "content": system_instructions}]
messages.append({"role": "user", "content": question})

response = make_openai_call(client, messages)
