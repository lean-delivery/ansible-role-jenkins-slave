jenkins-slave role
==================
[![License](https://img.shields.io/badge/license-Apache-green.svg?style=flat)](https://raw.githubusercontent.com/lean-delivery/ansible-role-jenkins-slave/master/LICENSE)
[![pipeline status](https://gitlab.com/lean-delivery/ansible-role-jenkins-slave/badges/master/pipeline.svg)](https://gitlab.com/lean-delivery/ansible-role-jenkins-slave/-/commits/master)
[![pipeline status](https://gitlab.com/lean-delivery/ansible-role-jenkins-slave/badges/master/pipeline.svg)](https://gitlab.com/lean-delivery/ansible-role-jenkins-slave/-/commits/master)
[![Galaxy](https://img.shields.io/badge/galaxy-lean__delivery.jenkins__slave-blue.svg)](https://galaxy.ansible.com/lean_delivery/jenkins_slave)
![Ansible](https://img.shields.io/ansible/role/d/35589.svg)
![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F35589%2F&query=$.min_ansible_version)

This role sets up a new jenkins slave node and adds it to the jenkins master.

## Requirements
------------

- Version of the ansible for installation: >=2.8
- **Supported OS**
  - EL
    - 7
    - 8
  - Amazon Linux 2
  - Ubuntu
    - xenial
    - bionic
  - Debian
    - stretch
  - Windows
    - 2016
    - 2019

## Dependencies
------------

**Java 8** [![Build Status](https://travis-ci.org/lean-delivery/ansible-role-java.svg?branch=master)](https://travis-ci.org/lean-delivery/ansible-role-java)

## Role Variables
--------------

- required
  - `master_username`
  Jenkins master CLI user name. Default value is `admin`.
  - `master_password`
  Jenkins master CLI user password. Default value is `admin`.
  - `master_host`
  FQDN name or IP address of the jenkins master host. Default value is `{{ ansible_host }}`.
  - `master_port`
  Jenkins master http port. Default value is `8080`.

- general defaults
  - `slave_agent_name`
  Agent name of the slave node. Default value is `agent`.
  - `slave_executors_num`
  Number of executors of the slave node. Default value is `1`.
  - `slave_environments`
  Dictionary of env variables to be set on slave. Default value is `{}`
  - `slave_mode_exclusive`
  Set usage of this node. If true, node will only build jobs with matching label expressions. Default value is `false`.
  - `master_url`
  Jenkins master host URL. Default value is `http://{{ master_host }}:{{ master_port }}`.

- linux defaults
  - `slave_linux_jenkins_cred_id`
  Already exist credentials id on the jenkins master: Default value is `ci_slave`.
  - `slave_linux_jenkins_username`
  User name that is defined in `slave_linux_jenkins_cred_id`. A new user with this name to be created on the slave node. Default value is `user`.
  - `slave_linux_jenkins_password`
  Password for a new user on the slave node. Must match with the credentials password if its kind is 'Username with password'. Default value is 'password'.
  - `slave_linux_jenkins_public_key`
  Public key that to be added to authorized_keys slave user file. Private key is placed in the credentials on the jenkins master if its kind is 'SSH Username with private key'. Default value is `""`.
  - `slave_linux_home`
  Home path for deploying jenkins slave binaries. Default value is `/opt/jenkins`.
  - `slave_linux_user_group`
  Group for a new user on the slave node. Default value is `user`.
  - `slave_linux_host`
  Host where jenkins slave is installed to. Default value is `"{{ ansible_host }}"`.
  - `slave_linux_ssh_port`
  SSH port of the slave node. Default value is `22`.
  - `slave_linux_selinux_ports`
  Selinux ports of the slave node. Default value is `"{{ master_port }},49187,{{ slave_linux_ssh_port }}"`.
  - `slave_linux_labels`
  List of labels for the slave node. Default value is `['linux']`.

- windows defaults
  - `slave_windows_workdir`
  Home path for deploying jenkins slave binaries. Default value is `C:/Jenkins_Slave`.
  - `slave_windows_service`
  Windows service name. Default value is `jenkins-slave`.
  - `slave_windows_java_opts`
  Additional options to pass to java. Default value is `""`.
  - `slave_windows_labels`
  List of labels for the slave node. Default value is `['windows']`.
  - `slave_windows_service_user`
  The username to set the service to start as.
  - `slave_windows_service_password`
  The password of given username to set the service to start as.


## Example Playbook

```yaml
- name: "Install jenkins-slave on remote hosts using default 'Username with password' credentials"
  hosts: slave

  vars:
    master_host: master.example.com

  roles:
    - role: lean_delivery.jenkins_slave
```

```yaml
- name: "Install jenkins-slave on remote hosts using created 'Username with password' credentials"
  hosts: one_slave

  vars:
    master_host: master.example.com
    slave_linux_jenkins_cred_id: new_cred
    slave_linux_jenkins_username: new_user
    slave_linux_jenkins_password: new_password
    slave_agent_name: new_linux_slave

  roles:
    - role: lean_delivery.jenkins_slave
```

```yaml
- name: "Install jenkins-slave on remote hosts using created 'SSH Username with private key' credentials"
  hosts: many_slaves

  vars:
    master_host: master.example.com
    slave_linux_jenkins_cred_id: new_cred
    slave_linux_jenkins_username: new_user
    slave_linux_jenkins_public_key:
Nck6x4HPrsdfkjhwhf98239hfoijhpowifnYXRXAW1GYGC3lsq7FpWjCeN8wT5QzRsblTh6HZKqh96K3Jj6kpob8ykjhsdkfjhskdfuhksdjfhksjdfhksfjhhkjhUHKUHDKFksjdfhkjshdfXPlx2xSUINDsH2IACLjIrxSAppxITzR7fHZyLmkjsdhfkuwhe98237982fhksdfhksdfhkuhCmcvH6fdVtozo42lXt4QgKytGtiuGAT+lN+uJ4LVGOq32WiEbYKbc7WE7N

  roles:
    - role: lean_delivery.jenkins_slave
```

## Inventory example
    [master]
    master.example.com

    [one_slave]
    slave.example.com

    [many_slaves]
    slave1.example.com slave_agent_name=slave1
    slave2.example.com slave_agent_name=slave2

## License
-------
Apache [![License](https://img.shields.io/badge/license-Apache-green.svg?style=flat)](https://raw.githubusercontent.com/lean-delivery/ansible-role-jenkins-slave/master/LICENSE)

## Author Information
------------------

authors:
  - Lean Delivery Team <team@lean-delivery.com>
