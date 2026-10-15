# pdfmargin
CLI tools to add margins to and split PDF files.

## Installation
```
$ git clone https://github.com/daigohirata/pdfmargin ~/pdfmargin
$ cd ~/pdfmargin
$ pip install .
```

## Usage
```
# Display all available options
$ pdfmargin --help

# Process multiple PDFs (the shell expands *.pdf); each result is saved beside its input
$ pdfmargin -i /path/to/pdfs/*.pdf -s right

# Explicitly list multiple input files
$ pdfmargin --input-files first.pdf second.pdf -s right

# For a single input, optionally choose the output file
$ pdfmargin -i input.pdf -o output.pdf -s right

# Split after pages 12, 14, 67, and 90; any remaining pages are saved as a final file
$ dividedpdf -i input.pdf -o output_dir/ -d 12,14,67,90
# The same command is also available as `dividepdf`
```

Split output files are named with their page ranges, such as `input_1-12.pdf`,
`input_13-14.pdf`, and `input_15-67.pdf`. The output directory is created if needed.

## Uninstallation

To uninstall `pdfmargin`, run the following command:

```bash
pip uninstall pdfmargin