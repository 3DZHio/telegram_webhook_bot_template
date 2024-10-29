### LOCAL ###
## SSH ##
ssh-keygen -t ed25519 -f ~/.ssh/server -N "<PASSWORD>"


### SERVER ###
## SSH ##
echo "<PUBLIC_SSH>" >> ~/.ssh/authorized_keys
ssh <USERNAME>@<SERVER_IP>


## INSTALL DEPENDENCIES ##
# APT #
sudo apt install -y git make

# SNAP #
sudo snap refresh
sudo snap install docker


## GIT ##
ssh-keygen -t ed25519 -f ~/.ssh/git -N "<PASSWORD>" -C "<EMAIL>"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/git