from dataclasses import dataclass, field
from typing import List, Dict

'''
Author: Nikhil Pothuru

All the data classes that represent manifest segments 
'''
@dataclass
class Section:
    foldername: str
    prefix: str
    links: Dict[str, str] = field(default_factory=lambda: {})

@dataclass
class Manifest:
    root: str
    sections: List[Section] = field(default_factory=list)

