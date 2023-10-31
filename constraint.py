# Abstract class for link constraints
import re


class Constraint:
    def __init__(self) -> None:
        pass


    def check_response_integrity(self, response)-> str:
        """Checks that that a generated response abides by the constraints of the link. If not, returns a feedback string for allowing the link's result to be improved.

        Args:
            response (str): Result from the link execution

        Raises:
            NotImplementedError: Abstract method

        Returns:
            str: Feedback string for allowing the link's result to be improved. If empty, the link's result is considered valid.
        """

        raise NotImplementedError
    
class MinWordCount(Constraint):
    """The minimum word count constraint checks that the generated response is not too short. Used for instance in summarization tasks.
    """    
    def __init__(self, min_length:int) -> None:
        """The minimum word count constraint checks that the generated response is not too short. Used for instance in summarization tasks.

        Args:
            min_length (int): The minimum number of words for the generated response to be considered valid.
        """        
        self.min_length = min_length

    def check_response_integrity(self, response)-> str:
        feedback = ""
        words = re.split("[.!?\n ,;:]", response)
        if len(words)<self.min_length:
            feedback += f"Your response was too short by at least {self.min_length-len(words)} words. Make sure it is at least {self.min_length} words long."

        return feedback
    
class VerbatimSimilarity(Constraint):
    """The vertabim similarity constraint checks that the generated response is not too dissimilar to the reference text. used for instance in transcription tasks.: 
    """    

    def __init__(self, reference_text:str, sim_threshold:float=0.7) -> None:
        """The vertabim similarity constraint checks that the generated response is not too dissimilar to the reference text. used for instance in transcription tasks.

        Args:
            reference_text (str): The text to compare the generated response to
            sim_threshold (float): The minimum similarity score for the generated response to be considered valid. Defaults to 0.7.
        """        
        self.reference_text = reference_text

    def check_response_integrity(self, response)-> str:
        
        feedback = ""
        pass
        
        feedback+="Your rephrased too much of the original text. Try to rephrase it less."
        return feedback
