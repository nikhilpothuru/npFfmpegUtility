import json

import marshmallow_dataclass

from manifest.manifest import Manifest

'''
Author: Nikhil Pothuru

Deserialize the provided manifest 
'''
class ManifestDeserializer:

    @staticmethod
    def deserialize(manifestPath):
        try:
            manifest_schema = marshmallow_dataclass.class_schema(Manifest)()
            with open(manifestPath, 'r') as file:
                json_content = json.load(file)
                manifest = manifest_schema.load(json_content)
                return manifest

        except FileNotFoundError:
            print("ManifestDeserializer failed to load manifest")




