import ast
import sys
import os

def generate_docstring(func_node):
    """Generate a simple docstring for a function node."""
    args = [arg.arg for arg in func_node.args.args]
    doc_lines = [
        f'"""',
        f'{func_node.name}({', '.join(args)})',
        '',
        'Args:'
    ]
    for arg in args:
        doc_lines.append(f'    {arg}: Description.')
    doc_lines.extend([
        '',
        'Returns:',
        '    Description.',
        '"""'
    ])
    return '\n'.join(doc_lines)

def add_docstrings_to_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        source = f.read()
    tree = ast.parse(source)
    new_lines = source.splitlines()
    offset = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not ast.get_docstring(node):
                docstring = generate_docstring(node)
                indent = ' ' * node.col_offset
                insert_line = node.body[0].lineno - 1 + offset
                docstring_lines = [indent + line if i > 0 else indent + line for i, line in enumerate(docstring.split('\n'))]
                for i, line in enumerate(docstring_lines):
                    new_lines.insert(insert_line + i, line)
                offset += len(docstring_lines)
    new_source = '\n'.join(new_lines)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_source)
    print(f"Docstrings added to {file_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <python_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)
    add_docstrings_to_file(file_path)

if __name__ == "__main__":
    main()
