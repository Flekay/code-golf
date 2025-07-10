import re

try:
    import python_minifier
except ImportError:
    python_minifier = None

class PythonGolfer:
    """
    Python code golfer/minifier using the same logic as the JS/HTML frontend.
    Tries to minify using python_minifier first, then applies golfing.
    """

    @staticmethod
    def char_count(s: str) -> int:
        return len(s)

    @staticmethod
    def bytes_count(s: str) -> int:
        # Python 3 strings are Unicode, so we encode to bytes first
        return len(s.encode('utf-8'))

    @staticmethod
    def minify_code(code: str) -> str:
        # Try to minify using python_minifier if available
        if python_minifier:
            try:
                code = python_minifier.minify(code)
            except Exception:
                pass
        # Remove blank lines and trailing spaces at end of lines
        code = re.sub(r'^\s*[\r\n]', '', code, flags=re.MULTILINE)
        code = re.sub(r'\s*$', '', code, flags=re.MULTILINE)
        return code

    @staticmethod
    def golf_code(code: str) -> str:
        # First minify using python_minifier if possible
        code = PythonGolfer.minify_code(code)

        # Remove blank lines and trailing spaces at end of lines
        code = re.sub(r'^\s*[\r\n]', '', code, flags=re.MULTILINE)
        code = re.sub(r'\s*$', '', code, flags=re.MULTILINE)

        # Fix "+ " and ". " substrings
        if "+ " in code or ". " in code:
            code = code.replace("+ ", " +").replace(". ", " .")

        # Pad to even length
        if len(code) % 2 != 0:
            code += " "

        # Only ASCII allowed
        if any(ord(c) > 127 for c in code):
            raise ValueError("All chars in your code must be in the ASCII table.")

        # Encode as per JS logic
        buffer = []
        for i in range(0, len(code), 2):
            c1 = ord(code[i])
            c2 = ord(code[i+1])
            buffer.append(chr((c2 << 8) | c1))

        encoded = ''.join(buffer)
        return f"exec(bytes('{encoded}','u16')[2:])"
