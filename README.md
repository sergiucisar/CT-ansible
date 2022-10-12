# cetelem-infra
# Bootstraping the VMs
With below command you will need to configure the systems to use ssh-keys and create the sudo rights to execute elevated commands

ansible-playbook -i inventories/<ENV> sshkey.yml -b -k -K

ansible-playbook -i inventories/<ENV> sudoers.yml -b -k -K

With below command you will provision the VMs with a set of specific tools needed by the running services, but also adding proxy setting to be able to download packages and update the systems.

ansible-playbook -i inventories/<ENV> common.yml -b

# Pre-requisites for deployment
- application_name variable (to be used for which host/groups we want to deploy to)
- tags (to be used for choosing role to be executed)

ex.
ansible-playbook -i inventories/dc1 -t activemq -e application_name=active_mq 
#
ansible-playbook -i inventories/env -t role_name -e application_name=ansbile_hosts_to_deploy_to

# For Java please use
APP=java; ansible-playbook playbook.yml -i inventories/<ENV> -t $APP -e application_name=$APP -b

# For Redis please use
- application_name=redis_nodes
- -t redis-sentinel
APP=redis_nodes; ansible-playbook playbook.yml -i inventories/<ENV> -t redis-sentinel -e application_name=$APP -b

# For ActiveMQ please use
- application_name=
- -t activemq
APP=artemis; ansible-playbook playbook.yml -i inventories/<ENV> -t $APP -e application_name=$APP -b

# For OpenLiverty please use
- application_name=openliberty
- -t openliberty
APP=openliberty; ansible-playbook playbook.yml -i inventories/<ENV> -t $APP -e application_name=$APP -b

