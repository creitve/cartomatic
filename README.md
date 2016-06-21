## About

Open-source scenarios to help you setup [CS-Cart and Multi-Vendor](https://cs-cart.com/) servers. Current version is 1.0.0.

  * [About](#about)
      * [Features](#features)
      * [Components](#components)
      * [Running in production](#running-in-production)
      * [Running on virtual machine](#running-on-virtual-machine)
      * [Building your own image](#building-your-own-image)
      * [Supported platforms](#supported-platforms)
      * [Restrictions](#restrictions)
      * [Status](#status)
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

Cartomatic will install the latest versions of the following software for you:

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

If you already have your VPS/VDS and you want to try `cartomatic` in action, follow these steps:

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

Cartomatic not only covers your production needs, but can also ease your development and
testing workflow with virtual machines and [Vagrant](https://vagrantup.com).

1. Switch to the `dev/` directory.

2. Specify parameters in the 'config.yml' settings file:

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

    Define as much VMs as you need to create and provision here.
    Take a look at [the instruction for building images](../build/README.md) if you want to
    create your own image instead of using self-hosted ones.

3. Run vagrant:

    ```
    vagrant up
    ```

    Provisioning can take from 5 to 15 minutes per machine.

#### Building your own image

We use [Packer](https://packer.io) configurations to build Vagrant images.

1. Switch to `build/` directory.

2. Execute this command to build your own image:

    CentOS 6 x86_64
    ```
    packer build centos6.json
    ```

    Wait until it is over. It normally takes 15 to 30 minutes to finish.

3. Add the resulting image into Vagrant using the following command:

    ```
    vagrant box add NAME images/IMAGE_NAME.box
    ```

    In some cases you might require the root password, which is `test123!`.

#### Supported platforms

* CentOS / RedHat / Scientific Linux 6 x86_64

#### Restrictions

* Not compatible with ISPManager, cPanel, Plesk etc.
* Works well only for clean installations.

#### Status

| Repository | Status |
|------------|--------|
| Stable | [![Build Status](https://travis-ci.org/simtechdev/cartomatic.svg?branch=master)](https://travis-ci.org/simtechdev/cartomatic) |
| Unstable | [![Build Status](https://travis-ci.org/simtechdev/cartomatic.svg?branch=develop)](https://travis-ci.org/simtechdev/cartomatic) |

#### License

MIT
