#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *
import os

"""
Ansible module to create openliberty server
(c) 2017, Matthieu Rémy <remy.matthieu@gmail.com>
"""

DOCUMENTATION = '''
---
module: openliberty_create
short_description: Creates an openliberty server.
description:
    - Creates an openliberty server.
options:
    name:
        description:
            - server name
        required: true
        default: null
    path:
        description:
            - server path
        required: true
        default: null
    user:
        description:
            - user name to connect to theserver
        required: true
        default: null
    password:
        description:
            - user password to connect to the server
        required: true
        default: null
'''

EXAMPLES = '''
# Create openliberty server named 'openliberty-server' with a user / password : admin / admin
- openliberty_create: state="present" name="openliberty-server" user="admin" password="admin"
'''

CREATE_server_COMMAND = "{0}/bin/server create {1}"


def create_server(openliberty_home, ansible_module, name, path):
    """Call openliberty bin command to create a server

    :param openliberty_home: openliberty home
    :param ansible_module: ansible module
    :param name: server name
    :param name: server path
    :return: command, ouput command message, error command message
    """

    changed = False
    cmd = CREATE_server_COMMAND.format(openliberty_home, path, name)
    out = ""
    err = ""

    if not os.path.isdir(name):
        rc, out, err = ansible_module.run_command(cmd)
        changed = True

        if len(err) > 0:
            ansible_module.fail_json(msg=err)

    return changed, cmd, out, err


def main():
    fields = {
        "name": {"required": True, "type": "str"},
        "path": {"required": True, "type": "str"},
        "openliberty_home": {"default": "/opt/openliberty", "type": "str"}
    }

    ansible_module = AnsibleModule(argument_spec=fields)

    name = ansible_module.params["name"]
    path = ansible_module.params["path"]
    openliberty_home = ansible_module.params["openliberty_home"]

    changed, cmd, out, err = create_server(openliberty_home, ansible_module, name, path)

    ansible_module.exit_json(changed=changed, cmd=cmd, name=name, stdout=out, stderr=err)

if __name__ == '__main__':
    main()
