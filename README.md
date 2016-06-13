## About

Scenarious which helps you setup server for [CS-Cart and Multi-Vendor](https://cs-cart.com/). Current version is 1.0.0 beta.

* [Features](#features)
* [Quick install](#quick-install)
* [Manual install](#manual-install)
* [Components](#components)
* [Supported platforms](#supported-platforms)
* [Restrictions](#restrictions)
* [License](#license)

#### Features

- [x] HTTP/2 support
- [x] Performance tuning for highload
- [x] Deflate/GZIP compression
- [x] Google Pagespeed filters support
- [x] Well-looking error pages
- [x] Full-page Varnish cache
- [x] Strong SSL preferencies (A+ by default on SSL Labs)
- [x] Development environment based on [Vagrant](https://vagrantup.com)
- [x] Configurations for creating your own images based on [Packer](https://packer.io)

#### Quick install

Log in to your server as superuser (root) via SSH and execute this command:

```
export CARTOMATIC_AUTO=true; curl -sL https://raw.githubusercontent.com/simtechdev/cartomatic/master/provision/shell/cartomatic-installer | bash -s -- yourdomain.tld
```

Done. It works.

#### Manual install

1. Log in to your server as superuser (root) via SSH and execute this command.

    ```
    curl -sL https://raw.githubusercontent.com/simtechdev/cartomatic/master/provision/shell/cartomatic-installer | bash -s
    ```

2. Clone repository into the workspace.

   ```
   git clone https://github.com/simtechdev/cartomatic
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

#### Components

Cartomatic will install for you the latest versions of following software:

- [x] [Apache](http://httpd.apache.org) + mod_php
- [x] [WEBKAOS](http://github.com/essentialkaos/webkaos)
- [x] [PHP](https://secure.php.net)
  - [x] 5.4.x
  - [x] 5.5.x
  - [x] 5.6.x
  - [x] 7.0.x
- [x] [MariaDB](https://mariadb.com)
- [x] [Redis](http://redis.io)
- [x] [Postfix](http://www.postfix.org)
- [x] [vsFTPd](https://security.appspot.com/vsftpd.html)
- [x] [Varnish](https://www.varnish-cache.org)
- [x] [phpMyAdmin](https://www.phpmyadmin.net)

Please keep in mind that apps are still subject to change.

#### Supported platforms

* CentOS/RedHat/Scientific Linux 6 x86_64

#### Restrictions

* Not compatible with ISPManager, cPanel, Plesk etc.
* Works well only for clean installations.

#### License

MIT
