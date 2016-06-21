## About

Open-source scenarios which helps you setup server for [CS-Cart and Multi-Vendor](https://cs-cart.com/). Current version is 1.0.0.

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

#### Running in production 

If you already have your VPS/VDS and you want to try `cartomatic` in action, you should do following things:

###### Quick start

Log in to your server as superuser (root) via SSH and execute this command:

```
export CARTOMATIC_AUTO=true; curl -sL https://raw.githubusercontent.com/simtechdev/cartomatic/master/provision/shell/cartomatic-installer | bash -s -- yourdomain.tld
```

Done. It works.

###### Advanced 

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

#### Running on virtual machine

Cartomatic well-works not only on production – you can use it for development or
testing purposes using virtual machines which managed by [Vagrant](https://vagrantup.com).

1. Switch to the `dev/` directory.

2. Specify parameters into the 'config.yml' settings file:

    ```
    vms:
      centos6:
        box: centos6
        box_url: https://vagrant.smtk.us/centos/6/centos6.box
        ip: 10.0.0.10

    provision:
      ansible:
        playbook: "../provision/ansible/lamp.yml"
        extra_vars: "../provision/ansible/config/manual.json"
    ```

    You should specify amount of VMs which you want to launch for provisioning.
    Please read [the instruction for building images](../build/README.md) if you want to
    create your own image instead of using self-hosted images.

3. Run vagrant:

    ```
    vagrant up
    ```

    Please wait. It may takes from 5 to 15 minutes.

#### Building your own image

We use [Packer](https://packer.io) configurations for building Vagrant images.

1. Switch to `build/` directory.

2. Execute this command to build your own image:

    CentOS 6 x86_64
    ```
    packer build centos6.json
    ```

    Please wait. It takes from 15 to 30 minutes. Done.

3. Add the resulting image into Vagrant using following command:

    ```
    vagrant box add NAME images/IMAGE_NAME.box
    ```

    In some cases you need to know root-password. Here it is: `test123!`

#### Supported platforms

* CentOS / RedHat / Scientific Linux 6 x86_64

#### Restrictions

* Not compatible with ISPManager, cPanel, Plesk etc.
* Works well only for clean installations.

#### License

MIT
