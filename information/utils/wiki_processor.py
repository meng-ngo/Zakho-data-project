import wikipedia

import re

class WikiStructuredContent:
    def __init__(self):
        self.title = ''
        self.summary = ''
        self.content = ''
        self.structured_content = dict()
        self.html = ''
    
    def get_title(self):
        return self.title
    
    def set_title(self, wiki_title):
        self.title = wiki_title
    
    def get_content(self):
        return self.content
    
    def set_content(self, wiki_content):
        self.content = wiki_content
        
    def process_content_string(self):
        split_content = re.split('\n+', self.content)
        pattern = re.compile('=+ .+ =+')
        current_header = 'Summary'
        for block in split_content:
            if re.match(pattern, block): 
                space_location = block.find(' ')
                current_header = block[space_location + 1: -space_location - 1]
            else: 
                self.structured_content.setdefault(current_header, [])
                self.structured_content[current_header].append(block)
                
    def get_structured_content(self):
        return self.structured_content