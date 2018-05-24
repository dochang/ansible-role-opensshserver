Opensshserver
=============

[![Build Status](https://travis-ci.org/dochang/ansible-role-opensshserver.svg?branch=master)](https://travis-ci.org/dochang/ansible-role-opensshserver)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-dochang.opensshserver-blue.svg)](https://galaxy.ansible.com/dochang/opensshserver/)

An ansible role to configure OpenSSH server.

Requirements
------------

None

Role Variables
--------------

  - `opensshserver_permitrootlogin` (default: `prohibit-password`)
  - `opensshserver_permitemptypasswords` (default: `no`)
  - `opensshserver_passwordauthentication` (default: `no`)
  - `opensshserver_gssapiauthentication` (default: `no`)
  - `opensshserver_pubkeyauthentication` (default: `yes`)

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - role: dochang.opensshserver
          opensshserver_passwordauthentication: no

License
-------

MIT

Author Information
------------------

Desmond O. Chang <dochang@gmail.com>
