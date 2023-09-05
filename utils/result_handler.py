import os
from typing import List


class EmailSaver:
    def __init__(self, output_path: str):
        self.output_path = output_path
        
    @property
    def output_path(self):
        return self._output_path
    
    @output_path.setter
    def output_path(self, value):
        if not value.endswith(".txt"):
            raise ValueError("Output path must end with .txt")
        if not os.path.exists(os.path.dirname(value)):
            raise ValueError(f"Output directory '{os.path.dirname(value)}' does not exist")
        self._output_path = value
        

    def save_emails(self, email_list: List[str]) -> None:
        if not email_list:
            raise ValueError("Email list is empty")
        
        with open(self.output_path, 'w') as f:
            for email in email_list:
                f.write(f"{email}\n")
                
        print(f"Extracted {len(email_list)} email addresses and saved to '{self.output_path}'.")
        