# tests/test_base.py
import pytest

class TestBase:
    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self, setup):
        self.driver = setup
        yield
        # Any additional teardown can be added here
