import os
import argparse
# from pypdf import PdfReader, PdfWriter, PageObject
from pypdf import PdfReader, PdfWriter

def add_margin_to_pdf(input_pdf, output_pdf, margin_ratio=0.25, side="both"):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        original_width = float(page.mediabox.width)
        original_height = float(page.mediabox.height)

        margin = original_width * margin_ratio

        if side == "both":
            new_width = original_width + 2 * margin
            tx = margin
        elif side == "left":
            new_width = original_width + margin
            tx = margin
        elif side == "right":
            new_width = original_width + margin
            tx = 0
        else:
            raise ValueError("Invalid side value. Choose from 'both', 'left', 'right'.")

        # 空白ページを作成（推奨方法）
        new_page = writer.add_blank_page(width=new_width, height=original_height)

        # 既存ページを新ページにマージ（中央 or 左寄せ）
        new_page.merge_translated_page(page, tx=tx, ty=0)

    try:
        with open(output_pdf, "wb") as f:
            writer.write(f)
    except Exception as e:
        print(f"[Error] Failed to write the output file: {e}")
    else:
        print(f"The output file has been successfully saved: {output_pdf}")


def main():
    parser = argparse.ArgumentParser(description='Make margins on the side of PDF files')
    parser.add_argument('-i', '--input-file', 
                        required=True,
                        help='Path to input file')
    parser.add_argument('-o', '--output-file',
                        help='Path to output file')
    parser.add_argument('-s', '--side',
                        choices=['both', 'left', 'right'],
                        default='both',
                        help='Which side(s) to add margins: both, left, or right (default: both)')
    parser.add_argument('-r', '--margin-ratio',
                        default=0.5,
                        help='Margin ratio to original size')
    
    args = parser.parse_args()

    input_pdf = args.input_file

    if args.output_file is None:
        base, ext = os.path.splitext(input_pdf)
        output_pdf = base + '_margined' + ext
    else:
        output_pdf = args.output_file
    
    add_margin_to_pdf(
        input_pdf=args.input_file,
        output_pdf=output_pdf,
        margin_ratio=args.margin_ratio,
        side=args.side
    )

if __name__ == "__main__":
    main()
