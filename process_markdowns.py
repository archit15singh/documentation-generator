# Filename: process_markdowns.py

from pathlib import Path

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

if __name__ == "__main__":
    folder_path = '/workspaces/documentation-generator/generated_documentation/pilot'
    master_document_path = '/workspaces/documentation-generator/pilot.md'
    process_markdown_files(folder_path, master_document_path)
