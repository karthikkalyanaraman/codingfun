import mock

"""Mocks a True for infinite loop

"""

class MockTrue(object):
    """MockTrue class for mocking True

    """

    def __init__(self, total_iterations=1):
        self.total_iterations = total_iterations
        self.current_iteration = 0

    def __nonzero__(self):
        if self.current_iteration < self.total_iterations:
            self.current_iteration += 1
            return bool(1)
        return bool(0)
