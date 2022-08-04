Role Name
=========

openliberty: Openliberty

[![Build Status](https://travis-ci.org/cmihai-ansible/openliberty.svg?branch=master)](https://travis-ci.org/cmihai-ansible/openliberty)

Ansible galaxy:
---------------

[https://galaxy.ansible.com/devopstoolbox.openliberty](https://galaxy.ansible.com/devopstoolbox.openliberty)

```bash
ansible-galaxy install devopstoolbox.openliberty
```

Requirements
------------

- For RHEL, a Red Hat subscription or functional local repository.
- Ansible 2.4 or higher

Role Variables
--------------

```yaml
openliberty_packages_state: present
openliberty_remove_packages: true
openliberty_enable_service: true
openliberty_enable_selinux: true
openliberty_copy_templates: true
openliberty_firewall_configure: true
openliberty_firewall_rules:
  - service: ssh
  - port: 3389
openliberty_users:
  - user: devops
    group: docker
openliberty_selinux_booleans:
  - name: ftp_home_dir
    state: true
    persistent: true
```

Dependencies
------------

- For Red Hat, subscription-manager.

Example Playbook
----------------

```yaml
---
- name: Install openliberty on localhost
  hosts:
    - localhost
  connection: local

  tasks:
    - name: openliberty is configured
      import_role:
        name: devopstoolbox.openliberty
      vars:
        openliberty_packages_state: present
        openliberty_remove_packages: true
        openliberty_enable_service: true
        openliberty_enable_selinux: true
        openliberty_copy_templates: true
        openliberty_firewall_configure: true
        openliberty_firewall_rules:
          - service: ssh
          - port: 3389
        openliberty_users:
          - user: devops
            group: docker
        openliberty_selinux_booleans:
          - name: ftp_home_dir
            state: true
            persistent: true
      tags: openliberty
```

License
-------

MIT

Author Information
------------------

- [Mihai Criveti](https://www.linkedin.com/in/crivetimihai)
