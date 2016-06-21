About
-----

Cartomatic well-works not only on production – you can use it for development or
testing purposes using virtual machines which managed by [Vagrant](https://vagrantup.com).

How to use
----------

1. Specify parameters into the 'config.yml' settings file:

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

2. Run vagrant:

    ```
    vagrant up
    ```

    Please wait. It may takes from 5 to 15 minutes.
