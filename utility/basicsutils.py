import inspect
import logging
from abc import ABC
import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass
