import json
import cmd
import re


class KnowledgeBase():
    def __init__(self, kbase_file):
        self.kbase_file = kbase_file
        self.tagdict = {}
        
    def add_dot(self, kdot):
        if kdot.tag in self.tagdict:
            self.tagdict[kdot.tag].append({"priority": kdot.prio, "content": kdot.content})
        elif re.match(" *", kdot.tag):
            raise ValueError("Tag is not allowed to contain whitespace!")
        else:
            self.tagdict[kdot.tag] = [{"priority": kdot.prio, "content": kdot.content}]
        
            
    def del_dot_in_tag(self, tag, idx):
        del self.tagdict[tag][idx]
            
    def save_base(self):
        with open(self.kbase_file, "w") as outfile:
            json.dump(self.tagdict, outfile, indent=4)
    
    def load_base(self):
        with open(self.kbase_file) as infile:
            self.tagdict = json.load(infile)

    def search_base(self, search_term):
        search_results = []
        for tag in self.tagdict.keys():
            for dot in self.tagdict[tag]:
                match = re.search((search_term), dot["content"], flags=re.I)
                if match:
                    search_results.append(dot["content"])
        return search_results
        
        
class KDot():
    def __init__(self, tag="general", content="", prio=5):
        self.tag = tag
        self.content = content
        self.prio = prio
    
