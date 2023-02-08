from kiwi.core import Environment
from kiwi.common import ConstWrapper


class Wrapper:
    def __init__(self, wrapper_type):
        """attach the wrapper to environment"""
        self.wrapper_type = wrapper_type
        Environment().append_wrapper(wrapper=self)

    def get_wrapper_type(self):
        return self.wrapper_type


class Step(Wrapper):
    def __init__(self, comment: str, step_spec=""):
        super().__init__(ConstWrapper.STEP_WRAPPER)
        self.comment = comment
        self.step_spec = step_spec

    @staticmethod
    def _parse_step_spec(step_spec: str) -> (str, [str], [str]):
        """
            step_spec: a string which denotes step num, wait list, and parallel list.
            step number: step hierarchy, e.g. 1.2.1
            wait list: the step must run after all the steps and its previous step finish, e.g. [1.1,2.3]
            children parallel list: the child steps of it can run in parallel. e.g [1.1,1.2,1.3] or [1.1-1.8]
            a simple example: sn:2,wt:[1.1],cp[2.1-2.3]
            this step is 2rd step, it can run after 1.1 finish, and 2.1,2.2,2.3 steps can run in parallel
        """
        step_num = None
        wait_list = []
        children_parallel_list = []

        return step_num, wait_list, children_parallel_list


class Operation(Wrapper):
    def __init__(self):
        super().__init__()
        pass
