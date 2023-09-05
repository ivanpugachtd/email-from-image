from PIL import Image
from image_to_email import ImageHandler, DataExtractor
from utils import ArgumentParser, EmailSaver
from pytesseract import pytesseract


if __name__ == "__main__":
    try:
        argument_parser = ArgumentParser()
        args = argument_parser.get_args()
        
        image_path, output_path = args.input, args.output
        image_handler = ImageHandler(image_path)
        result_saver = EmailSaver(output_path)
        
        image = image_handler.load_image()
        text_from_image = pytesseract.image_to_string(image)
        extracted_emails = DataExtractor(text_from_image).extract_all_by("email")
        if not extracted_emails:
            print("No emails found")
        
        result_saver.save_emails(extracted_emails)
    except Exception as e:
        print(e)
    