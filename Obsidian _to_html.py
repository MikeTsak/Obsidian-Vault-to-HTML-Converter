import markdown2
import shutil
from pathlib import Path

# Configuration
obsidian_root = Path('C:/Users/mixan/Documents/D&G').resolve() #here is the path to your obsidian vault
image_root = Path('C:/Users/mixan/Documents/D&G/Img').resolve() #here is the path to your Images

output_directory = Path('.').resolve() / 'html_output'
assets_directory = output_directory / 'img'

# Make sure the output and assets directories exist
output_directory.mkdir(exist_ok=True)
assets_directory.mkdir(exist_ok=True)

def copy_assets(source_path, destination_path):
    """Copies asset files from the Obsidian vault to the output directory."""
    for item in source_path.iterdir():
        if item.is_file() and item.suffix not in ['.md', '.html']:
            destination = destination_path / item.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(item, destination)

def markdown_to_html(md_file):
    """Converts a Markdown file to an HTML file."""
    relative_path = md_file.relative_to(obsidian_root)
    html_file = output_directory / relative_path.with_suffix('.html')
    html_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Read the markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown content to HTML
    html_content = markdown2.markdown(md_content)

    # Define the header with the stylesheet link
    header_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{relative_path.stem}</title>
    <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
"""
    # Define the footer
    footer_html = """
</body>
</html>
"""

    # Write the header, converted content, and footer to the HTML file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(header_html + html_content + footer_html)
    
    return html_file


def create_index():
    """Creates an index.html file with links to all HTML files and assets."""
    with open(output_directory / 'index.html', 'w', encoding='utf-8') as index_file:
        index_file.write("<!DOCTYPE html><html><head><title>Obsidian Vault Index</title>")
        index_file.write('<link rel="stylesheet" href="style.css">')  # Link to the CSS file
        index_file.write("</head><body>")
        
        def write_directory_contents(directory, indent_level=0):
            for path in sorted(directory.iterdir()):
                relative_path = path.relative_to(output_directory)
                if path.is_dir():
                    index_file.write(f'{"  " * indent_level}<li>{path.name}/</li>\n')
                    index_file.write(f'{"  " * indent_level}<ul>\n')
                    write_directory_contents(path, indent_level + 1)
                    index_file.write(f'{"  " * indent_level}</ul>\n')
                else:
                    index_file.write(f'{"  " * indent_level}<li><a href="{relative_path}">{path.name}</a></li>\n')
        
        index_file.write("<ul>")
        write_directory_contents(output_directory)
        index_file.write("</ul></body></html>")

def copy_stylesheet():
    """Copies the style.css file to the output directory."""
    source_css = Path('style.css')  # Assuming the style.css is in the same directory as your script
    destination_css = output_directory / 'style.css'
    if source_css.exists():
        shutil.copy(source_css, destination_css)
    else:
        print("style.css not found. Please ensure it's in the same directory as the script.")

def copy_images():
    """Copies image files from a specified path to the output assets directory."""
    for image_path in image_root.glob('**/*'):  # Adjust the glob pattern if you want to be more specific
        if image_path.is_file() and image_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp']:
            relative_path = image_path.relative_to(image_root)
            destination = assets_directory / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not destination.exists():
                shutil.copy(image_path, destination)
                print(f"Copied image: {destination}")
            else:
                print(f"Image already exists: {destination}")

# Main execution
if __name__ == '__main__':
    print(f"Looking for Markdown files in {obsidian_root}")
    
    # Find all markdown files and convert to HTML
    md_files = list(obsidian_root.rglob('*.md'))
    for md_file in md_files:
        print(f"Converting Markdown file: {md_file}")
        html_file = markdown_to_html(md_file)
        # Copy assets relative to each markdown file
        copy_assets(md_file.parent, output_directory / md_file.parent.relative_to(obsidian_root))
    
    print(f"Converted {len(md_files)} Markdown files to HTML.")

    # Copy the stylesheet and images
    copy_stylesheet()
    copy_images()

    # Create the index file
    create_index()

    print("Index created with links to all HTML files and assets.")
    print("Done!")