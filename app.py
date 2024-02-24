from typing import List
import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI
from pathlib import Path
from tqdm import tqdm

# Load environment variables
load_dotenv()

# Constants
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
COST_PER_THOUSAND_TOKENS = 0.01
# Global list to store cost estimates
cost_estimates = []

def estimate_cost(total_tokens):
    """
    Estimates the cost of a request based on the total tokens used.

    :param total_tokens: Number of tokens used in the response.
    :return: Estimated cost.
    """
    estimated_cost = (total_tokens / 1000) * COST_PER_THOUSAND_TOKENS
    cost_estimates.append(estimated_cost)
    print(f"Total Estimated Cost: ${sum(cost_estimates):.4f}")
    return estimated_cost

def print_response(response):
    """
    Prints the response details including the estimated cost.

    :param response: Response object from the Azure OpenAI call.
    """
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
                print(f"Tool function arguments: {json.loads(tool_call.function.arguments)}")
                print(f"Tool function name: {tool_call.function.name}")
                print(f"Tool type: {tool_call.type}")
        else:
            print("Tools not required")
    print("*" * 200)

def make_openai_call(client, messages, json_response=False):
    """
    Makes a call to the Azure OpenAI API and prints the response.

    :param client: AzureOpenAI client object.
    :param messages: List of message dictionaries for the API call.
    :param json_response: Flag to request response in JSON format.
    :return: Content of the first choice message.
    """
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        response_format={"type": "json_object"} if json_response else {"type": "text"},
        messages=messages,
        temperature=0,
        seed=42,
    )
    print_response(response)
    return response.choices[0].message.content


def iterate_files(directory, suffix):
    base_path = Path(directory)
    file_paths = []  # Initialize an empty list to store file paths
    for file in base_path.rglob('*' + suffix):  # Filter files by suffix
        if file.is_file():
            file_paths.append(file)  # Add the file path to the list
    return file_paths

def update_file_path(file_path: Path, old_segment: str, new_segment: str) -> Path:
    """
    Update a file path by replacing the old segment with a new segment.

    :param file_path: The original file path as a PosixPath object.
    :param old_segment: The path segment to be replaced.
    :param new_segment: The new path segment to replace the old one.
    :return: The updated file path as a PosixPath object.
    """
    # Convert the PosixPath to a string and replace the target substring
    new_str_path = str(file_path).replace(old_segment, new_segment)
    
    # Convert back to PosixPath
    updated_path = Path(new_str_path)
    
    return updated_path

def get_ai_response(client, prompt):
    """
    Fetches a response from the AI based on system instructions and a user question.

    :param client: The OpenAI client or equivalent API client instance.
    :param system_instruction: Instructions or context provided to the AI.
    :param question: The user's question to the AI.
    :return: The AI's response.
    """
    messages = [
        {"role": "user", "content": prompt},
    ]

    response = make_openai_call(client, messages)
    print("prompt:", prompt)
    print("Response:", response)
    return response

def create_folder_for_path(file_path: Path):
    """
    Ensures that the directory for a given file path is created if it doesn't already exist.

    :param file_path: The file path as a PosixPath object.
    """
    # Get the parent directory of the current path
    directory = file_path.parent
    
    # Create the directory if it doesn't exist
    directory.mkdir(parents=True, exist_ok=True)

def prepend_title_to_file_content(file_path):
    """
    Reads a file's content and prepends the file name as a title to it, then returns the modified content.

    :param file_path: The path to the file whose content is to be read.
    :return: A string containing the file name as a title followed by the original file content.
    """
    # Extract the file name to use as a title
    title = str(Path(file_path))

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Prepend the file name as a title to the content
        modified_content = title + '\n\n' + content  # Adding two newlines as a separator
        
        return modified_content
    except FileNotFoundError:
        return "File not found."

def write_content_to_file(file_path: Path, content: str, suffix: str):
    """
    Writes the given content to a file at the specified path with a new suffix, ensuring that the directory exists.

    :param file_path: The original path to the file where content will be written.
    :param content: The content to write to the file.
    :param suffix: The new file suffix (extension) to apply to the file path.
    """
    # Ensure the parent directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Modify the file path to use the new suffix
    new_file_path = file_path.with_suffix(suffix)

    # Write the content to the file with the new suffix
    with new_file_path.open('w', encoding='utf-8') as file:
        file.write(content)
    print(f"Content written to {new_file_path}")


def remove_markdown_code_blocks(content):
    """
    Removes the markdown code block syntax from the content.

    :param content: The content of a markdown file as a string.
    :return: The content with the markdown code block syntax removed.
    """
    return content.replace("```markdown", "").replace("```", "").strip()

def append_content_to_master(master_path, content):
    """
    Appends the given content to the master document.

    :param master_path: The path to the master document.
    :param content: The content to append to the master document.
    """
    with open(master_path, 'a', encoding='utf-8') as master_file:
        master_file.write(content + "\n\n")

def process_markdown_files(folder_path, master_document_path):
    """
    Processes all markdown files in the given folder (and subfolders), removing the specific
    markdown code block syntax and appending their content along with the file path to a master document.

    :param folder_path: The path to the folder containing markdown files.
    :param master_document_path: The path to the master document to append contents to.
    """
    folder_path = Path(folder_path)
    master_document_path = Path(master_document_path)

    # Ensure the master document is empty before starting
    master_document_path.write_text('')

    for md_file in folder_path.rglob('*.md'):
        content = md_file.read_text(encoding='utf-8')
        content = remove_markdown_code_blocks(content)
        file_info_and_content = f"File Path: {md_file}\n\n{content}\n\n---\n\n"
        append_content_to_master(master_document_path, file_info_and_content)

    print(f"All markdown files have been processed and appended to {master_document_path}")

def main(target_project):
    """
    Main function to initiate the API call and process the response.
    """
    documentation_task_description = """
    Your task is to write a very detailed technical description of what this file does and how it is used in the project.
    Do not add any preamble or conclusion to your response, respond with only the detailed technical documentation and description in markdown format.
    Think step by step.

    Input code file: 
    {}
    """

    if not all([AZURE_OPENAI_API_VERSION, AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT]):
        print("Missing required environment variables.")
        return

    client = AzureOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
    )

    file_paths = iterate_files(target_project, '.py')
    
    for file_path in tqdm(file_paths):
        print("*" * 100)
        print(f"running for file path: {file_path}")
        file_content = prepend_title_to_file_content(file_path)
        print(f"length of content: {len(file_content)}")
        documentation = get_ai_response(client=client, prompt=documentation_task_description.format(file_content))
        updated_path = update_file_path(file_path, 'target_code', 'generated_documentation')
        create_folder_for_path(updated_path)
        write_content_to_file(updated_path, documentation, '.md')



if __name__ == "__main__":
    target_project = '/workspaces/documentation-generator/target_code/prompttools'
    main(target_project)
    folder_path = '/workspaces/documentation-generator/generated_documentation/prompttools'
    master_document_path = '/workspaces/documentation-generator/prompttools.md'
    process_markdown_files(folder_path, master_document_path)
    total_estimated_cost = sum(cost_estimates)
    print(f"Total Estimated Cost: ${total_estimated_cost:.4f}")
