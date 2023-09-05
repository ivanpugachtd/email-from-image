This simple script allows user to path image and get txt file with extracted from image email addresses.


Installation:
1. Clone the Repository
git clone https://github.com/ivanpugachtd/email-from-image.git

2. Create a Virtual Environment
python3 -m venv <venv_name>

3. Activate the Virtual Environment
source <venv_name>/bin/activate

4. Install Tesseract
for Mac users, simply run: brew install tesseract

5. Install Dependencies
pip install -r requirements.txt

6. Usage
The application functions as a script and uses command-line arguments. For additional details, you can refer to the help command:
python main.py -h

7. Example of usage
There are several example images in the images/ folder. Here's how to use the script:
python main.py --input images/5.png --output output/5.txt