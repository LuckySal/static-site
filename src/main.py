import os
import shutil

from markdown_to_html_node import markdown_to_html_node

SOURCE_DIRECTORY = "static"
DESTINATION_DIRECTORY = "public"


def main():
    # Get contents of source directory
    contents_list = []
    traverse_directory(SOURCE_DIRECTORY, contents_list)

    # Clear destination directory
    if os.path.exists(DESTINATION_DIRECTORY):
        shutil.rmtree(DESTINATION_DIRECTORY)
    os.mkdir(DESTINATION_DIRECTORY)

    # Copy contents of source directory into destination
    for item in contents_list:
        dest = item.replace(SOURCE_DIRECTORY, DESTINATION_DIRECTORY, 1)
        create_directory(dest)
        shutil.copy(item, dest)


def traverse_directory(current, contents_list):
    # Recursively traverse source directory and add all file contents to the list
    dir_contents = os.listdir(current)
    for item in dir_contents:
        path = os.path.join(current, item)
        if os.path.isfile(path):
            contents_list.append(path)
        else:
            traverse_directory(path, contents_list)


def create_directory(destination):
    # Recursively create directories for given file path
    dirname = os.path.dirname(destination)
    if os.path.exists(dirname):
        return
    create_directory(dirname)
    os.mkdir(dirname)


if __name__ == "__main__":
    main()
