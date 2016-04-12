About
-----

[Packer](https://packer.io) configurations for building images.

How to use
----------

1. Execute this command to build your own image:

    CentOS 6 x86_64
    ```
    packer build centos6.json
    ```

    CentOS 7 x86_64
    ```
    packer build centos7.json
    ```

    Please wait. It takes from 15 to 30 minutes. Done.

2. Add the resulting image into Vagrant using following command:

    ```
    vagrant box add NAME images/IMAGE_NAME.box
    ```

    In some cases you need to know root-password. Here it is: `test123!`
