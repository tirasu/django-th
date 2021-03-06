Pocket
======

Service Description:
--------------------

a "Read it Later" service

modifications of settings.py
----------------------------

1) INSTALLED_APPS :

.. code-block:: python

    INSTALLED_APPS = (
        'th_pocket',
    )

2) Cache :

After the default cache add :

.. code-block:: python

    CACHES = {
        'default':
        {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': BASE_DIR + '/cache/',
            'TIMEOUT': 600,
            'OPTIONS': {
                'MAX_ENTRIES': 1000
            }
        },
        # Pocket Cache
        'th_pocket':
        {
            'TIMEOUT': 500,
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/5",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        },

3) TH_SERVICES

add this line to the TH_SERVICES setting

.. code-block:: python

    TH_SERVICES = (
        'th_pocket.my_pocket.ServicePocket',
    )



4) The service keys

I strongly recommend that your put the following in a local_settings.py, to avoid to accidentally push this to a public repository


.. code-block:: python

    TH_POCKET = {
        # get your credential by subscribing to http://getpocket.com/developer/
        'consumer_key': '<your pocket key>',
    }


creation of the table of the services
-------------------------------------

enter the following command

.. code-block:: bash

    python manage.py migrate


from the admin panel, activation of the service
-----------------------------------------------

from http://yourdomain.com/admin/django_th/servicesactivated/add/

* Select "Pocket",
* Set the Status to "Enabled"
* Check Auth Required: this will permit to redirect the user (or you) to Pocket website to confirm the access of the Pocket account
* Fill a description

