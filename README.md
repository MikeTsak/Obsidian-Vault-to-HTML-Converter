# Obsidian Vault to HTML Converter

This script takes Markdown files from an Obsidian Vault and converts them into HTML format. It maintains the folder structure, converts images, and applies a dark theme for a user-friendly reading experience in a web browser.

## Features

- **Markdown Conversion**: Converts `.md` files into `.html` format while preserving the original folder structure.
- **Asset Handling**: Transfers associated media and document assets to the output directory.
- **Image Management**: Ensures that images from a specified path are copied correctly, supporting various image formats.
- **Dark Theme**: Implements a dark mode style across all HTML pages for a consistent and modern user interface.
- **Automatic Indexing**: Generates an `index.html` that provides a directory listing for easy navigation through the converted files.

## Prerequisites

- Python 3
- `markdown2` library (Install with `pip install markdown2`)

## Usage

1. Set the `obsidian_root` and `image_root` variables in the script to point to your Obsidian Vault and image directories.
2. Run the script with Python to convert all Markdown files in the specified directory.
3. Access the generated HTML files from the `html_output` directory.

## Installation

Clone this repository to your local machine, then install the required Python dependencies:

```bash
git clone https://github.com/your-username/obsidian-to-html.git
cd obsidian-to-html
pip install -r requirements.txt
```

## Running the Script

To execute the conversion process, run:
```
python Obsidian_to_html.py
```
After running the script, the html_output folder will contain all the HTML files, assets, and an index.html for navigation.

## Configuration

Configure the paths in the script:

- obsidian_root: Path to your Obsidian Vault directory.
- image_root: Path to your images directory.
These paths are crucial for the script to find and convert your files.

## Output
The script generates the following in the html_output directory:

A mirror of your Obsidian Vault's folder structure with HTML files.
An `img` folder containing all non-Markdown files that were in the same directories as your Markdown files.
An `index.html` file that provides a navigable index of all converted files.

## Me
[Visit my personal website](http://www.miketsak.gr)
