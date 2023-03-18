Пример простого REST в проекте Pyramid
======================================

Установка:
1. Клонироание репозитория.
2. Создание виртуальной среды Python 

В папке проекта
---------------

https://cornice.readthedocs.io/en/latest/quickstart.html

3. pip install -U pip
4. pip install -r requirements.txt
5. pip install -e .
6. настроить соеднинение с mongodb (если мой, то надо ставить vpn).
7. провести тестирование, будет создан экземпляр Group в mongo-БД.
8. pserve development.ini --reload

открыть браузер на http://localhost:6543/api/group/<groupid экземпляра>


Credits
-------

- `Distribute`_
- `modern-package-template`_

.. _Distribute: http://code.activestate.com/pypm/distribute/
.. _`modern-package-template`: http://code.activestate.com/pypm/modern-package-template/
