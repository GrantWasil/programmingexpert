import unittest

class FileSystem:

    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        self._validate_path(path)
        dirs = path.split("/")[1:]
        current_dir = self.root
        while len(dirs) > 0:
            if len(dirs) == 1:
                current_dir.add_node(Directory(dirs[0]))
                dirs.pop()
            else:
                if dirs[0] in current_dir.children:
                    current_dir = current_dir.children[dirs[0]]
                    dirs.pop(0)
                else:
                    raise ValueError("That's a no no")

    def create_file(self, path, contents):
        self._validate_path(path)
        dirs = path.split("/")[1:]
        bottom_node = self._find_bottom_node(dirs)
        try:
            file = File(dirs[-1])
            file.write_contents(contents)
            bottom_node.add_node(file)
        except:
            raise ValueError("That's a no no")

    def read_file(self, path):
        self._validate_path(path)

    def delete_directory_or_file(self, path):
        # Write your code here.
        pass

    def size(self):
        # Write your code here.
        pass

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")

    def _find_bottom_node(self, node_names):
        current_dir = self.root
        for node in node_names:
            if node in current_dir.children:
                current_dir = current_dir.children[node]
            else:
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


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)




class TestProgram(unittest.TestCase):
    def test_case_1(self):
        fs = FileSystem()
        fs.create_directory("/dir1")
        fs.create_directory("/dir2")
        fs.create_directory("/dir1/dir3")
        with self.assertRaises(ValueError):
            fs.create_directory("/dir3/dir4")
        print(fs)

    def test_case_2(self):
        fs = FileSystem()
        fs.create_file("/tim.txt", "Tim is great!")
        print(fs)
        with self.assertRaises(ValueError):
            fs.create_file("/dir1/simon.txt", "ProgrammingExpert is fun!")
        self.assertEqual("Tim is great!", fs.read_file("/tim.txt"))
        print(fs)

    def test_case_3(self):
        fs = FileSystem()
        fs.create_file("/tim.txt", "12345")
        self.assertEqual(fs.size(), 5)
        fs.create_file("/alex.txt", "67890")
        self.assertEqual(fs.size(), 10)
        print(fs)

    def test_case_4(self):
        fs = FileSystem()
        fs.create_directory("/dir1")
        fs.create_directory("/dir1/dir2")
        fs.create_directory("/dir1/dir2/dir3")
        fs.create_file("/dir1/dir2/file1.txt", "1")
        fs.create_file("/dir1/dir2/dir3/file2.txt", "1")
        self.assertEqual(fs.size(), 2)
        print(fs)

    def test_case_5(self):
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
        print(fs)

    def test_case_6(self):
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
        print(fs)

if __name__ == "__main__":
    unittest.main()