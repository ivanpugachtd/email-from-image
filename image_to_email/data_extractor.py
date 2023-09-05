import re
from typing import List, Dict


class DataExtractor:
    def __init__(self, text: str):
        self.text: str = text
        self._patterns = {
            "email": r'[\w.+-]+@[\w-]+\.[\w.-]+',
        }
        
    @property
    def patterns(self) -> Dict[str, str]:
        return self._patterns
    
    def get_patterns_list(self) -> List[str]:
        return list(self._patterns.keys())
    
    def extract_all_by(self, pattern_name: str) -> List[str]:
        if not self.text:
            raise Exception("Text is empty")
        if pattern_name not in self.patterns:
            raise Exception("Pattern not found")
        
        return re.findall(self.patterns[pattern_name], self.text)