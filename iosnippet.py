import atexit
import io
import sys

_INPUT = sys.stdin.read().splitlines()
input = iter(_INPUT).__next__
_OUTPUT = io.StringIO()
sys.stdout = _OUTPUT


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT.getvalue())