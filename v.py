import os
from dataclasses import dataclass, field
import time

@dataclass()
class DevEnvSetup():

    containerName: str
    user_email: str
    user_name: str
    dir_prefix: str = field(init=False)
    ssh_key_priv: str
    ssh_key_pub: str = field(init=False)  
    cont_user: str 

    def __post_init__(self: object) -> None:
        # Assuming the keys have the same name and are in the same directory
        self.dir_prefix = "$HOME/.ssh/"
        self.ssh_key_priv = f"{self.dir_prefix}{self.ssh_key_priv}"
        self.ssh_key_pub = f"{self.ssh_key_priv}.pub"
    
    # Redundant if already configured 
    def gitConfig(self: object) -> None:
        # Creating os commands to then be executed by the script
        git_email: str = f'git config user.email "{self.user_email}"'
        git_user: str = f'git config user.name "{self.user_name}"'
        # Execute
        print(f"Executing:\n{git_email}")
        os.system(git_email)
        time.sleep(2)  # Adding time to prevent any potential errors
        print(f"Executing:\n{git_user}")
        os.system(git_user)
    
    def keyConfig(self: object) -> None:

        # Execute
        print(f"Executing:\n{priv}")
        os.system(priv)
        time.sleep(2)
        print(f"Executing:\n{pub}")
        os.system(pub)

def main():
    name: str = input("Container-ID [Docker]:\t")
    email: str = input("Email [GitHub]:\t")
    uname: str = input("Username [GitHub]:\t")
    sshkeypriv: str = input("SSH-Key [Name | NoDir!]:\t")
    contuser: str = input("User inside the Container:\t")

    env = DevEnvSetup(cont_user=contuser, containerName=name, user_email=email, user_name=uname, ssh_key_priv=sshkeypriv) 

    env.gitConfig()
    env.keyConfig()
    
if __name__ == "__main__":

    main()