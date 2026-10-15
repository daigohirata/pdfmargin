import argparse
import os

from pypdf import PdfReader, PdfWriter


def parse_dividers(value):
    try:
        dividers = [int(item.strip()) for item in value.split(",")]
    except ValueError:
        raise argparse.ArgumentTypeError("ページ番号はカンマ区切りの整数で指定してください")

    if not dividers or any(page <= 0 for page in dividers):
        raise argparse.ArgumentTypeError("ページ番号は1以上で指定してください")
    if any(left >= right for left, right in zip(dividers, dividers[1:])):
        raise argparse.ArgumentTypeError("ページ番号は重複せず、昇順で指定してください")
    return dividers


def split_pdf(input_pdf, output_dir, dividers):
    reader = PdfReader(input_pdf)
    page_count = len(reader.pages)

    if any(page > page_count for page in dividers):
        raise ValueError("分割ページ番号が入力PDFのページ数を超えています")

    os.makedirs(output_dir, exist_ok=True)
    input_name = os.path.splitext(os.path.basename(input_pdf))[0]
    end_pages = list(dividers)
    if not end_pages or end_pages[-1] < page_count:
        end_pages.append(page_count)

    output_files = []
    first_page = 1
    for last_page in end_pages:
        writer = PdfWriter()
        for page_index in range(first_page - 1, last_page):
            writer.add_page(reader.pages[page_index])

        output_path = os.path.join(
            output_dir, "{}_{}-{}.pdf".format(input_name, first_page, last_page)
        )
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        output_files.append(output_path)
        first_page = last_page + 1

    return output_files


def main():
    parser = argparse.ArgumentParser(
        description="指定したページ番号でPDFを分割します"
    )
    parser.add_argument("-i", "--input-file", required=True, help="入力PDFのパス")
    parser.add_argument("-o", "--output-dir", required=True, help="出力先ディレクトリ")
    parser.add_argument(
        "-d",
        "--dividers",
        required=True,
        type=parse_dividers,
        metavar="PAGES",
        help="各分割ファイルの最終ページ（例: 12,14,67,90）",
    )
    args = parser.parse_args()

    try:
        output_files = split_pdf(args.input_file, args.output_dir, args.dividers)
    except (OSError, ValueError) as error:
        parser.error(str(error))

    for output_file in output_files:
        print("Created: {}".format(output_file))


if __name__ == "__main__":
    main()