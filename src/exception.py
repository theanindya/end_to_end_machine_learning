import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename # exc_tb is the traceback object.
# exc_tb.tb_frame gives the current frame (where the error occurred).
# exc_tb.tb_frame.f_code gives details about the function/method where the error occurred.
# exc_tb.tb_frame.f_code.co_filename gives the file name of the script where the error happened.

    
    error_message="Errror occured in python script [{0}] line no [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message