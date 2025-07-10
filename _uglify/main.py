import os
from src.PythonGolfer import PythonGolfer

def should_skip(name):
    return name.startswith('.') or name.startswith('_')

def find_py_files(root):
    py_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Remove dirs to skip from traversal
        dirnames[:] = [d for d in dirnames if not should_skip(d)]
        for fname in filenames:
            if should_skip(fname):
                continue
            if fname.endswith('.py') and not fname.endswith('.min.py'):
                py_files.append(os.path.join(dirpath, fname))
    return py_files

def delete_min_files(root):
    # Walk through the project directory and delete .min.py files
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith('.min.py'):
                os.remove(os.path.join(dirpath, fname))
                print(f"Deleted: {os.path.join(dirpath, fname)}")

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(root, ".."))  # Go up to project root
    delete_min_files(root)  # Delete old .min.py files before minification
    py_files = find_py_files(root)
    for path in py_files:
        with open(path, encoding='utf-8') as f:
            original = f.read()
        try:
            golfed = PythonGolfer.golf_code(original)
        except Exception as e:
            print(f"Skipping {path}: {e}")
            continue
        if len(golfed) < len(original):
            min_path = path[:-3] + ".min.py"
            with open(min_path, "w", encoding='utf-8') as f:
                f.write(golfed)
            print(f"Minified: {path} -> {min_path} ({len(original)} -> {len(golfed)})")
        else:
            print(f"No gain: {path} ({len(original)} chars)")

if __name__ == "__main__":
    main()
