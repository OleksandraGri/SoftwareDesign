import re

class SmartTextReader:
    def read(self, file_path):
        print(f"Simulating reading from file: {file_path}")
        # Можна замінити цей код на просто повернення якогось тексту для тесту
        return "Simulated content from file."

class SmartTextChecker(SmartTextReader):
    def read(self, file_path):
        print(f"Opening file: {file_path}")
        content = super().read(file_path)
        print(f"File content: {content}")
        return content

class SmartTextReaderLocker(SmartTextReader):
    def __init__(self, pattern):
        self.pattern = re.compile(pattern)

    def read(self, file_path):
        if not self.pattern.match(file_path):
            print("Access denied!")
        else:
            return super().read(file_path)
