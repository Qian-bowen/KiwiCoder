from kiwi.util import TreeNode, TreeAryN


class Step(TreeNode):
    def __init__(self, step_num: str):
        """
            step_num: step hierarchy, e.g. 1.2.1
        """
        super().__init__(step_num)
        self.step_num = step_num


class StepController:
    def __init__(self):
        self.step_tree = TreeAryN()
        self.step_graph = None

    @staticmethod
    def parse_step_spec(step_spec: str) -> (str, [str], [str]):
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

    def _build_step_graph(self) -> None:
        if self.step_graph is not None:
            return
