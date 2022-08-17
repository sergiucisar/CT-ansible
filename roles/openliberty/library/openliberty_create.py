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

CREATE_server_COMMAND = "{0}/bin/openliberty create {1}/{2} --user {3} --password {4} --require-login"


def create_server(openliberty_home, ansible_module, name, path, user, password):
    """Call openliberty bin command to create a server

    :param openliberty_home: openliberty home
    :param ansible_module: ansible module
    :param name: server name
    :param name: server path
    :param user: server user
    :param password: server password
    :return: command, ouput command message, error command message
    """

    changed = False
    cmd = CREATE_server_COMMAND.format(openliberty_home, path, name, user, password)
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
        "user": {"required": True, "type": "str"},
        "password": {"required": True, "type": "str", "no_log": True},
        "openliberty_home": {"default": "/opt/openliberty", "type": "str"}
    }

    ansible_module = AnsibleModule(argument_spec=fields)

    name = ansible_module.params["name"]
    path = ansible_module.params["path"]
    openliberty_home = ansible_module.params["openliberty_home"]
    user = ansible_module.params["user"]
    password = ansible_module.params["password"]

    changed, cmd, out, err = create_server(openliberty_home, ansible_module, name, path, user, password)

    ansible_module.exit_json(changed=changed, cmd=cmd, name=name, stdout=out, stderr=err)

if __name__ == '__main__':
    main()
