from .endpoints import endPoints
from .client import App
from .message import Message

class Transaction():


    def __init__(self):
        pass
    

    def issueSila(self,payload,user_private_key):
        """issues sila erc20token for dollar amount on ethereum blockchain to kyced ethereum addresses (price one cent per token)
           the handle address signatures need to be verified
        Args:
            payload : includes user handle and amount
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        header=HttpClient.setHeader(user_private_key)
        path=endPoints["issueSila"]
        
            
        response=HttpClient.post(path,payload,header)

        return response



    

    def redeemSila(payload,header):
        """redeems sila erc20token for dollar amount on ethereum blockchain to kyced ethereum addresses (price one cent per token)
           the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        
        path=endPoints["redeemSila"]
            
        response=HttpClient.post(path,payload,header)

        return response



    def transferSila(payload,header):
        """ transfer sila from one ethereum address to another using sila api
           the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        
        path=endPoints["transferSila"]
            
        response=HttpClient.post(path,payload,header)

        return response