class Course:
    def __init__(self, name, code, instructor):
        self.name = name
        self.code = code
        self.instructor = instructor

class Resource:
    def __init__(self, name, file_type, upload_date):
        self.name = name
        self.file_type = file_type
        self.upload_date = upload_date

    def add_resource(self):
        # Implement resource addition logic here
        print(f"Resource '{self.name}' added successfully.")

    def get_resource(self):
        # Implement resource retrieval logic here
        print(f"Retrieving resource: {self.name}")

    def update_resource(self):
        # Implement resource update logic here
        print(f"Resource '{self.name}' updated successfully.")

    def delete_resource(self):
        # Implement resource deletion logic here
        print(f"Resource '{self.name}' deleted successfully.")

    def upload_resource(self):
        # Implement file upload logic here
        print(f"Uploading {self.file_type} file: {self.name}")

    def download_resource(self):
        # Implement file download logic here
        print(f"Downloading {self.file_type} file: {self.name}")

# Example usage
course = Course("Mathematics", "MATH101", "Professor Smith")
resource1 = Resource("Lecture Notes", "PDF", "2024-09-27")
resource2 = Resource("Homework Assignment", "DOCX", "2024-09-28")

resource1.upload_resource()
resource2.upload_resource()

resource1.add_resource()
resource2.add_resource()

resource1.update_resource()

resource1.get_resource()

resource2.delete_resource()

resource2.download_resource()
