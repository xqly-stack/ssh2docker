import os
import argparse
import time

            
def copyKeys(keyName: str, container_user: str, container_name: str):
    
    container_name: str = container_name
    container_user: str = container_user
    keyName: str = keyName
    
    # Assuming the keys have the same name and are in the same directory namely in ".ssh"
    dir_prefix = "$HOME/.ssh/"
    ssh_key_priv = f"{dir_prefix}{keyName}"
    ssh_key_pub = f"{ssh_key_priv}.pub"
    
    # Inserting the keys into the devcontainer (Docker must be installed to perform these actions)
    priv: str = f'docker cp {ssh_key_priv} {container_name}:/home/{container_user}/.ssh/'
    pub: str = f'docker cp {ssh_key_pub} {container_name}:/home/{container_user}/.ssh/'

    # Execute
    print(f"\nExecuting:\n{priv}\n")
    os.system(priv)
    time.sleep(2)
    print(f"\nExecuting:\n{pub}\n")
    os.system(pub)


if __name__=="__main__":
    
    parser = argparse.ArgumentParser(description='Copy GitHub SSH-Keys to any given devcontainer')
    parser.add_argument('keyName', type=str, help='The Key Name (No File Extension / No File Path)')
    parser.add_argument('container_user', type=str, help='The user inside the decontainer')
    parser.add_argument('container_name', type=str, help='The actual container to copy the files to')
    args = parser.parse_args()
    
    copyKeys(keyName=args.keyName, container_name=args.container_name, container_user=args.container_user)    