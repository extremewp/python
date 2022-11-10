

import pytest


@pytest.fixture(scope="function",params=['小明','小李','张三'],autouse=False)
def exect_ut():
    print('-------------------')