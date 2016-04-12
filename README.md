About
-----

[![Build Status](https://jenkins.gongled.me/buildStatus/icon?job=cartomatic)](https://jenkins.gongled.me/job/cartomatic)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/cscart/server-ansible-playbooks/blob/master/COPYING)

Scenarious which helps you setup server for [CS-Cart and Multi-Vendor](https://cs-cart.com/). Current version is 2.0.

[![Cartomatic](https://raw.githubusercontent.com/cscart/server-ansible-playbooks/devel/cartomatic.png)](https://cs-cart.com)

Features
--------

- [x] HTTP/2 support
- [x] Performance tuning for highload
- [x] Deflate/GZIP compression
- [x] Google Pagespeed filters support
- [x] Well-looking error pages
- [ ] Full-page Varnish cache
- [x] SSL/TLS encryption via Let's Encrypt
- [x] Strong SSL preferencies (A+ by default on SSL Labs)
- [x] Development environment based on [Vagrant](https://vagrantup.com)
- [x] Configurations for creating your own images based on [Packer](https://packer.io)

Quick install
-------------

Log in to your server as superuser (root) via SSH and execute this command:

```
export CARTOMATIC_AUTO=true; curl -sL https://raw.githubusercontent.com/cscart/server-ansible-playbooks/master/provision/shell/cartomatic-installer | bash -s -- yourdomain.tld
```

Done. It works.

Manual install
--------------

1. Log in to your server as superuser (root) via SSH and execute this command.

    ```
    curl -sL https://raw.githubusercontent.com/cscart/server-ansible-playbooks/master/provision/shell/cartomatic-installer | bash -s
    ```

2. Clone repository into the workspace.

   ```
   git clone https://github.com/cscart/server-ansible-playbooks
   ```

3. Switch to the `provision/ansible` directory.

    ```
    cd cartomatic/provision/ansible/
    ```

4. Put custom settings into the JSON file:

    ```
    vim config/manual.json
    ```

5. Run provisioning:

    ```
    ansible-playbook lamp.yml -c local -e @config/manual.json
    ```

    Passwords will be saved in the `credentials` folder.

Components
----------

Cartomatic will install for you the latest versions of following software:

- [x] [Apache](http://httpd.apache.org)
  - [x] FastCGI + suExec
  - [ ] mod_php
- [x] [Nginx](http://nginx.org)
  - [x] As a HTTP reverse proxy
  - [ ] As a FastCGI proxy
- [x] [PHP](https://secure.php.net)
  - [x] 5.6.x
  - [ ] 7.0.x
- [x] [MariaDB](https://mariadb.com)
- [x] [Redis](http://redis.io)
- [x] [Postfix](http://www.postfix.org)
- [x] [vsFTPd](https://security.appspot.com/vsftpd.html)
- [ ] [Varnish](https://www.varnish-cache.org)
- [x] [lego](https://github.com/xenolf/lego)
- [ ] [phpMyAdmin](https://www.phpmyadmin.net)
- [ ] [Fail2Ban](http://www.fail2ban.org/)
- [ ] [OpenSSH](http://www.openssh.com)

Please keep in mind that apps are still subject to change.

Supported platforms
-------------------

* CentOS 6 x86_64
* CentOS 7 x86_64

Restrictions
------------

* Not compatible with ISPManager, cPanel, Plesk etc.
* Works well only for clean installations.

Credits
-------

* [@UlyanovskUI](https://twitter.com/UlyanovskUI) for logo design.
* Tatiana Durnova for the help with translation.

License
-------

[MIT](https://github.com/cscart/server-ansible-playbooks/blob/master/COPYING)
