import json

class SecretDoesNotExist(Exception):
    pass

class SecretProvider:
    """Provides secrets from the local filesystem. Use it like a dictionary.
    
    Can be replaced with something that uses Key Vault or other approaches.
    """
    def __init__(self, filename: str):
        """
        @param filename: Full file path of a JSON file with name-value pairs.
        """
        self.filename = filename
        with open(filename, 'r') as jsonfile:
            self.content = json.load(jsonfile)

    def __getitem__(self, key) -> str:
        if key not in self.content:
            raise SecretDoesNotExist(f'Secret {key} does not exist in {self.filename}')
        return self.content[key]
        