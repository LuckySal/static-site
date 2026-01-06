import sys
from generate_site import generate_pages, copy_static

STATIC_DIRECTORY = "static"
DESTINATION_DIRECTORY = "docs"
CONTENT_DIRECTORY = "content"
TEMPLATE_PATH = "template.html"


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1] if sys.argv != "" else "/"
        
    # Copy files from static directory to public directory
    copy_static(STATIC_DIRECTORY, DESTINATION_DIRECTORY)

    # Generate pages from markdown and template
    print("Generating content...")
    generate_pages(
        basepath, CONTENT_DIRECTORY, DESTINATION_DIRECTORY, TEMPLATE_PATH
    )


if __name__ == "__main__":
    main()
