import subprocess
import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 15), reason="lazy imports are new in 3.15")
def test_lazy_imports_all():
    # With `-X lazy_imports=all` the imports in `httpcore/__init__.py` are lazy,
    # so its namespace holds placeholders until a name is first looked up.
    code = "import httpcore; assert httpcore.Request.__module__ == 'httpcore'"
    subprocess.run([sys.executable, "-X", "lazy_imports=all", "-c", code], check=True)
