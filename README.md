Opensshserver
=============

An ansible role to install and configure OpenSSH server.

Requirements
------------

None

Role Variables
--------------

  - `opensshserver_permitrootlogin` (default: `no`)
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
