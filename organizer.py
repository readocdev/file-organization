from pathlib import Path
import shutil

class FileOranizer:
    def __init__(self, folder_path, categories):
        self.folder = Path(folder_path)
        self.categories = categories
        self.folder.mkdir(exist_ok=True)
    
    def scan_folder(self):
        return [f for f in self.folder.iterdir() if f.is_file()]
    
    def categorize_file(self, file_path):
        for category, extensions in self.categories.items():
            if file_path.suffix.lower() in extensions:
                return category
        return "Other"
    
    def move_file(self, file_path, category):
        dest_folder = self.folder / category
        dest_folder.mkdir(exist_ok=True)
        shutil.move(str(file_path), dest_folder / file_path.name)
    
    def organize(self):
        files = self.scan_folder()

        for file in files:
            category = self.categorize_file(file)
            self.move_file(file, category)
            print(f"Moved {file.name} -> {category}")
