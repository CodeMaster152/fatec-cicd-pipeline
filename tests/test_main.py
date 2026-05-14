import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import soma


def test_soma():
    assert soma(2, 3) == 5