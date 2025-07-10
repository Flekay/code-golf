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
                minified = python_minifier.minify(code)
                if len(minified) < len(code):
                    code = minified
            except Exception:
                pass
        # Remove blank lines and trailing spaces at end of lines
        code = re.sub(r'^\s*[\r\n]', '', code, flags=re.MULTILINE)
        code = re.sub(r'\s*$', '', code, flags=re.MULTILINE)
        return code

    @staticmethod
    def crt(a, n):
        """Chinese Remainder Theorem implementation"""
        s, p = 0, 1
        for x in n:
            p *= x
        for x, y in zip(a, n):
            q = p // y
            s += q * x * pow(q, -1, y)
        return s % p

    @staticmethod
    def compress_1_2(code: str) -> str:
        """1:2 compression - original method"""
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

    @staticmethod
    def compress_1_3(code: str) -> str:
        """1:3 compression using Chinese Remainder Theorem"""
        # Replace newline with placeholder
        code = code.replace('\n', chr(127))

        # Pad to multiple of 3
        while len(code) % 3 != 0:
            code += ' '

        compressed = ''
        for i in range(0, len(code), 3):
            chunk = code[i:i+3]
            a = [ord(c) - 32 for c in chunk]
            try:
                result = PythonGolfer.crt(a, [101, 102, 103])
                # Ensure the result is within valid Unicode range
                if result > 0x10FFFF or (0xD800 <= result <= 0xDFFF):
                    raise ValueError("Invalid Unicode character generated")
                compressed += chr(result)
            except (ValueError, OverflowError):
                raise ValueError("CRT compression failed for chunk")

        return f"exec(''.join(chr(ord(c)%i+32)for c in'{compressed}'for i in b'efg').replace('\\x7f','\\n'))"

    @staticmethod
    def compress_1_4(code: str) -> str:
        """1:4 compression using Chinese Remainder Theorem"""
        # Replace newline with placeholder
        code = code.replace('\n', chr(127))

        # Pad to multiple of 4
        while len(code) % 4 != 0:
            code += ' '

        compressed = ''
        for i in range(0, len(code), 4):
            chunk = code[i:i+4]
            a = [ord(c) - 32 for c in chunk]
            try:
                result = PythonGolfer.crt(a, [101, 102, 103, 104])
                # Ensure the result is within valid Unicode range
                if result > 0x10FFFF or (0xD800 <= result <= 0xDFFF):
                    raise ValueError("Invalid Unicode character generated")
                compressed += chr(result)
            except (ValueError, OverflowError):
                raise ValueError("CRT compression failed for chunk")

        return f"exec(''.join(chr(ord(c)%i+32)for c in'{compressed}'for i in b'efgh').replace('\\x7f','\\n'))"

    @staticmethod
    def compress_1_5(code: str) -> str:
        """1:5 compression using Chinese Remainder Theorem"""
        # Replace newline with placeholder
        code = code.replace('\n', chr(127))

        # Pad to multiple of 5
        while len(code) % 5 != 0:
            code += ' '

        compressed = ''
        for i in range(0, len(code), 5):
            chunk = code[i:i+5]
            a = [ord(c) - 32 for c in chunk]
            try:
                result = PythonGolfer.crt(a, [101, 102, 103, 104, 105])
                # Ensure the result is within valid Unicode range
                if result > 0x10FFFF or (0xD800 <= result <= 0xDFFF):
                    raise ValueError("Invalid Unicode character generated")
                compressed += chr(result)
            except (ValueError, OverflowError):
                raise ValueError("CRT compression failed for chunk")

        return f"exec(''.join(chr(ord(c)%i+32)for c in'{compressed}'for i in b'efghi').replace('\\x7f','\\n'))"

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

        # Try all compression methods and return the shortest
        results = []

        try:
            result_1_2 = PythonGolfer.compress_1_2(code)
            results.append(result_1_2)
        except Exception as e:
            print(f"1:2 compression failed: {e}")

        try:
            result_1_3 = PythonGolfer.compress_1_3(code)
            results.append(result_1_3)
        except Exception as e:
            print(f"1:3 compression failed: {e}")

        try:
            result_1_4 = PythonGolfer.compress_1_4(code)
            results.append(result_1_4)
        except Exception as e:
            print(f"1:4 compression failed: {e}")

        try:
            result_1_5 = PythonGolfer.compress_1_5(code)
            results.append(result_1_5)
        except Exception as e:
            print(f"1:5 compression failed: {e}")

        if not results:
            raise ValueError("All compression methods failed")

        # Return the shortest result
        return min(results, key=len)
