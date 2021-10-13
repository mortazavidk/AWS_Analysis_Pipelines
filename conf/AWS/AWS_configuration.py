import hydra
from conf.common.configuration import AWSUserCredentials

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""

@hydra.main(config_path = None, config_name = "AWSUserCredentialsStore")
def set_AWS_user_credentials(AWS_user_credential:AWSUserCredentials) -> None:
   
   global AWS_ACCESS_KEY_ID
   global AWS_SECRET_ACCESS_KEY

   AWS_ACCESS_KEY_ID = AWS_user_credential.Access_key_ID
   AWS_SECRET_ACCESS_KEY = AWS_user_credential.Secret_Access_Key 


set_AWS_user_credentials()
