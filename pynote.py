"""
PyNote
This module contains all the necessary classes and functions to control and
manage a lightweight personal knowledge system based on a single .json-file.
"""
import json
import re


class KnowledgeBase():
    """
    The class KnowledgeBase represents the Knowledge Base as a nested dictionary.
    the toplevel dictionary has the tags as keys. The associated Values are lists of 'knowledge dots' or 'kdots'.
    Each kdot is itself a dictionary holding 'content' and 'priority' (as of writing, priority has no use yet)
    The initializer takes as argument the filename of the .json file that will hold or already holds the base.
    """
    def __init__(self, kbase_file):
        self.kbase_file = kbase_file
        self.tagdict = {}
        
    def add_dot(self, kdot):
        """
        Adds a dot to the base. If the  specified tag exists, the dot will be appended to the tags list of dots.
        If it does not exist, the tag will be tested with a regex fir whitespace and a ValueError will be raised if it does.
        Otherwise, the tag will be created as key first and the value set to a list containing the dot.
        """
        if kdot.tag in self.tagdict:
            self.tagdict[kdot.tag].append({"priority": kdot.prio, "content": kdot.content})
        elif re.match(" *", kdot.tag):
            raise ValueError("Tag is not allowed to contain whitespace!")
        else:
            self.tagdict[kdot.tag] = [{"priority": kdot.prio, "content": kdot.content}]
        
            
    def del_dot_in_tag(self, tag, idx):
        """
        Remove a dot at index idx in the list associated with the key tag.
        """
        del self.tagdict[tag][idx]
            
    def save_base(self):
        """
        writes the dictionary cobtaining the data as json to the file specified at initializing
        """
        with open(self.kbase_file, "w") as outfile:
            json.dump(self.tagdict, outfile, indent=4)
    
    def load_base(self):
        """
        Reads the json-file specified at initialization abd decodes the json to a dict of tags.
        """
        with open(self.kbase_file) as infile:
            self.tagdict = json.load(infile)

    def search_base(self, search_term):
        """
        Returns a list of dot contents that match a certain regex (case insensitive matching of the parameter search_term)
        """
        search_results = []
        for tag in self.tagdict.keys():
            for dot in self.tagdict[tag]:
                match = re.search((search_term), dot["content"], flags=re.I)
                if match:
                    search_results.append(dot["content"])
        return search_results
        
        
class KDot():
    """
    Class for a single note, a kdot. holds tag, priority and content.
    """
    def __init__(self, tag="general", content="", prio=5):
        self.tag = tag
        self.content = content
        self.prio = prio
    
