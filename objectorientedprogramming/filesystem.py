import unittest

class FileSystem:
    all_created_files = []

    def __init__(self):
        print("Creating new FileSystem")
        self.root = Directory("/")
        print(f"Check if all_created_files is empty. Current val: {FileSystem.all_created_files}")
        FileSystem.all_created_files = []
        print(f"Check if all_created_files is empty. New val: {FileSystem.all_created_files}")

    def create_directory(self, path):
        print("\n***Creating Directory***")
        FileSystem._validate_path(path)
        dirs = path[1:].split("/")

        dir_to_create = dirs[-1]
        print(f"Directory to create: {dir_to_create}")
        paths_to_traverse = dirs[:-1]
        print(f"Location to create it in: {paths_to_traverse}")
        last_dir = self._find_bottom_node(paths_to_traverse)
        print(f"The node to put {dir_to_create} in: \n{last_dir}")
        last_dir.add_node(Directory(dir_to_create))
        print(f"Created directory at: \n{last_dir}")

    def create_file(self, path, contents):
        print("\n***Creating file***")
        FileSystem._validate_path(path)
        path_names = path[1:].split("/")

        file_to_create = path_names[-1]
        print(f"File to create: {file_to_create}")
        paths_to_traverse = path_names[:-1]
        print(f"Location to create it in: {paths_to_traverse}")
        last_dir = self._find_bottom_node(paths_to_traverse)
        print(f"The node to put {file_to_create} in: \n{last_dir}")

        file = File(file_to_create)
        file.write_contents(contents)
        print(f"Created file: {file}")
        last_dir.add_node(file)
        print(f"Adding {file.name} to: \n{last_dir}")
        print(f"Current state of all_created_files {FileSystem.all_created_files}")
        print(f"Adding {file.name} to all_created_files")
        FileSystem.all_created_files.append(file)
        print(f"New state of all_created_files: {FileSystem.all_created_files}")
        
    def read_file(self, path):
        print("\n***Reading file***")
        FileSystem._validate_path(path)
        path_names = path[1:].split("/")

        file_to_read = path_names[-1]
        print(f"File to read: {file_to_read}")
        paths_to_traverse = path_names[:-1]
        print(f"Location to read it from: {paths_to_traverse}")
        last_dir = self._find_bottom_node(paths_to_traverse)
        print(f"The node the file should be in is: \n{last_dir}")

        if file_to_read not in last_dir.children:
            print(f"ERROR: The {file_to_read} was not found in {last_dir.name}")
            raise ValueError(f"The {file_to_read} was not found in {last_dir.name}")
        
        print(f"Returning: {last_dir.children[file_to_read]} contents")
        return last_dir.children[file_to_read].contents


    def delete_directory_or_file(self, path):
        print("\n***Delting file or directory***")
        FileSystem._validate_path(path)
        path_names = path[1:].split("/")

        object_to_delete = path_names[-1]
        print(f"Object to delete: {object_to_delete}")
        paths_to_traverse = path_names[:-1]
        print(f"Location to delete it from: {paths_to_traverse}")
        last_dir = self._find_bottom_node(paths_to_traverse)
        print(f"The node the object should be in is: \n{last_dir}")

        print(f"Checking to see if {object_to_delete} exists in {last_dir} as a child")
        if object_to_delete not in last_dir.children:
            print(f"ERROR: The {object_to_delete} was not found in {last_dir.name}")
            raise ValueError(f"The {object_to_delete} was not found in {last_dir.name}")
        
        found_object_to_delete = last_dir.children[object_to_delete]
        print(f"Checking to see if the {found_object_to_delete.name} is of type File")
        if isinstance(found_object_to_delete, File):
            print(f"Removing {found_object_to_delete.name} from {FileSystem.all_created_files}")
            FileSystem.all_created_files.remove(found_object_to_delete)
            print(f"State of all_created_files after removal {FileSystem.all_created_files}")

        print(f"Checking to see if the {found_object_to_delete.name} is of type Directory")
        if isinstance(found_object_to_delete, Directory):
            
            print(f"Checking to see if {found_object_to_delete.name} has any children")
            if len(found_object_to_delete.children) > 0:
                print(f"Found children in {found_object_to_delete}. Must delete those objects first. Here is current path: {path}")
                print(f"Children {found_object_to_delete.children}")
                children_to_delete = []
                for key, _ in found_object_to_delete.children.items():
                    children_to_delete.append(path + '/' + key)
                    print(f"Adding a deletion path to children_to_delete. Path: {path + '/' + key}")
                for path in children_to_delete:
                    self.delete_directory_or_file(path)
            else:
                print(f"No children found in {found_object_to_delete}. Continuing forward.")
        
        print(f"Deleting: {last_dir.children[object_to_delete]}")
        last_dir.delete_node(object_to_delete)


    def size(self):
        print("Determining size of all currently created files")
        print(f"Current state of all_created_files {FileSystem.all_created_files}")
        total_size = 0
        if len(FileSystem.all_created_files) == 0:
            return total_size
        for file in FileSystem.all_created_files:
            print(f"Adding the size of {file.name} which is {len(file)} to total_size which is currently: {total_size}")
            total_size += len(file)
            
        print(f"Returning total_size at: {total_size}")
        return total_size
        

    def __str__(self):
        return f"\n*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")

    def _find_bottom_node(self, node_names):
        print("\n***Finding bottom node***")
        current_dir = self.root
        print(f"Current directory:\n {current_dir}")
        print(f"Node names to traverse: {node_names}")
        for node in node_names:
            print(f"Current node in node_names: {node}")
            if not isinstance(current_dir, Directory):
                print(f"ERROR: {current_dir.name} is not of type Directory")
                raise ValueError(f"{current_dir} must be of type Directory")
            
            if not node in current_dir.children:
                print(f"ERROR: {node} was not found in {current_dir.name}")
                raise ValueError(f"{node} not found in {current_dir.name}")
            
            print(f"Setting {current_dir.name} to {current_dir.children[node].name}")
            current_dir = current_dir.children[node]
        print(f"Returning directory: \n{current_dir}")
        return current_dir

class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"
    
    def __repr__(self):
        return super().__str__()


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)




class TestProgram(unittest.TestCase):
    def test_case_1(self):
        print("\n\n----------Running Test Case 1----------")
        fs = FileSystem()
        fs.create_directory("/dir1")
        fs.create_directory("/dir2")
        fs.create_directory("/dir1/dir3")
        with self.assertRaises(ValueError):
            fs.create_directory("/dir3/dir4")

    def test_case_2(self):
        print("\n\n----------Running Test Case 2----------")
        fs = FileSystem()
        fs.create_file("/tim.txt", "Tim is great!")
        with self.assertRaises(ValueError):
            fs.create_file("/dir1/simon.txt", "ProgrammingExpert is fun!")
        self.assertEqual("Tim is great!", fs.read_file("/tim.txt"))

    def test_case_3(self):
        print("\n\n----------Running Test Case 3----------")
        fs = FileSystem()
        fs.create_file("/tim.txt", "12345")
        self.assertEqual(fs.size(), 5)
        fs.create_file("/alex.txt", "67890")
        self.assertEqual(fs.size(), 10)

    def test_case_4(self):
        print("\n\n----------Running Test Case 4----------")
        fs = FileSystem()
        fs.create_directory("/dir1")
        fs.create_directory("/dir1/dir2")
        fs.create_directory("/dir1/dir2/dir3")
        fs.create_file("/dir1/dir2/file1.txt", "1")
        fs.create_file("/dir1/dir2/dir3/file2.txt", "1")
        self.assertEqual(fs.size(), 2)

    def test_case_5(self):
        print("\n\n----------Running Test Case 5----------")
        fs = FileSystem()
        with self.assertRaises(ValueError):
            fs.delete_directory_or_file("/dir1")
        fs.create_directory("/dir1")
        fs.create_file("/dir1/simon.txt", "ProgrammingExpert is fun!")
        self.assertEqual(25, fs.size())
        with self.assertRaises(ValueError):
            fs.delete_directory_or_file("/dir2")
        fs.delete_directory_or_file("/dir1")
        self.assertEqual(0, fs.size())

    def test_case_6(self):
        print("\n\n----------Running Test Case 6----------")
        fs = FileSystem()
        fs.create_directory("/dir1")
        fs.create_directory("/dir1/dir2")
        fs.create_file("/dir1/dir2/file1.html", "Hello World")
        self.assertEqual(11, fs.size())
        self.assertEqual("Hello World", fs.read_file("/dir1/dir2/file1.html"))
        fs.delete_directory_or_file("/dir1")
        self.assertEqual(0, fs.size())
        with self.assertRaises(ValueError):
            fs.read_file("/dir1/dir2/file1.html")

if __name__ == "__main__":
    unittest.main()