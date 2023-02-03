from abc import ABC, abstractmethod

class BioOp(ABC):
    def __init__(
        self,
        op_detail:str
    ):
        self.op_detail=op_detail

    def get_detail(self)->str:
        return "op text"

    @abstractmethod
    def run(self)->None:
        pass

    @abstractmethod
    def mock_run(self)->None:
        pass
    
    
class First_Step_Op(BioOp):
     def __init__(
        self,
        op_detail:str
    ):
        super().__init__(op_detail=op_detail)

    def run(self)->None:
        pass

    def mock_run(self)->None:
        pass

    

class Start_Protocol_Op(BioOp):
     def __init__(
        self,
        op_detail:str
    ):
        super().__init__(op_detail=op_detail)

    def run(self)->None:
        pass

    def mock_run(self)->None:
        pass