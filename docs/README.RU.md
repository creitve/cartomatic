О проекте
---------

[![Build Status](https://jenkins.gongled.me/buildStatus/icon?job=cartomatic)](https://jenkins.gongled.me/job/cartomatic)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/cscart/server-ansible-playbooks/blob/master/COPYING)

Сценарии автонастройки сервера для [CS-Cart или Multi-Vendor](https://cs-cart.com/). Текущая версия 2.0.

[![Cartomatic](https://raw.githubusercontent.com/cscart/server-ansible-playbooks/develop/cartomatic.png)](https://cs-cart.com)

Возможности
-----------

- [x] Поддержка HTTP/2
- [x] Конфигурации для высоконагруженных проектов
- [x] Deflate/GZIP сжатие
- [x] Кастомные ошибки
- [ ] Поддержка Varnish
- [x] Шифрование SSL/TLS в Let's Encrypt
- [x] Оптимизация производительности SSL (A+ по оценке SSL Labs)
- [x] Окружение разработчика в [Vagrant](https://vagrantup.com)
- [x] Инструментарий для создания образов с [Packer](https://packer.io)

Быстрая установка
-----------------

Подключитесь к серверу по SSH под суперпользователя (root) и выполните команду:

```
export CARTOMATIC_AUTO=true; curl -sL https://raw.githubusercontent.com/cscart/server-ansible-playbooks/master/provision/shell/cartomatic-installer | bash -s -- yourdomain.tld
```

Готово.

Ручная установка
----------------

1. Подключитесь к серверу по SSH под суперпользователем (root) и выполните команду:

    ```
    curl -sL https://raw.githubusercontent.com/cscart/server-ansible-playbooks/master/provision/shell/cartomatic-installer | bash -s
    ```

2. Склонируйте репозиторий

   ```
   git clone https://github.com/cscart/server-ansible-playbooks
   ```

3. Перейдите в каталог `provision/ansible`.

    ```
    cd cartomatic/provision/ansible/
    ```

4. Укажите настройки во внешнем JSON файле

    ```
    vim config/manual.json
    ```

5. Запустите настройку

    ```
    ansible-playbook lamp.yml -c local -e @config/manual.json
    ```

    Автосгенерированные пароли будут сохранены в каталоге `credentials`.

Компоненты
----------

Сценарии установят следующее ПО:

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

Поддерживаемые ОС
-----------------

* CentOS 6 x86_64
* CentOS 7 x86_64

Ограничения
-----------

* Несовместимо с панелями управления ISPManager, cPanel, Plesk и др.
* Работает только на «чистых» инсталляциях

Благодарности
-------------

* [@UlyanovskUI](https://twitter.com/UlyanovskUI) за дизайн логотипа.
* Татьяне Дурновой за помощь с переводом.

Лицензия
--------

[MIT](https://github.com/cscart/server-ansible-playbooks/blob/master/COPYING)
