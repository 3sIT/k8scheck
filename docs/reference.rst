.. _reference:

API Reference
=============

This page contains the full API reference for k8scheck.

.. contents::
    :depth: 3
    :local:


.. _k8scheck_client:

Client
------

.. automodule:: k8scheck.client


TestClient
~~~~~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.client.TestClient
   :members:
   :noindex:


.. _k8scheck_objects:

Objects
-------

.. automodule:: k8scheck.objects


ApiObject
~~~~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.ApiObject
   :members:


ClusterRoleBinding
~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.ClusterRoleBinding
   :members:


ConfigMap
~~~~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.ConfigMap
   :members:


Container
~~~~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.Container
   :members:


Deployment
~~~~~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.Deployment
   :members:


Namespace
~~~~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.Namespace
   :members:


Node
~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.Node
   :members:


Pod
~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.Pod
   :members:


RoleBinding
~~~~~~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.RoleBinding
   :members:


Secret
~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.Secret
   :members:


Service
~~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.objects.Service
   :members:


.. _k8scheck_conditions:

Conditions
----------

.. automodule:: k8scheck.condition


Policy
~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.condition.Policy
   :members:


Condition
~~~~~~~~~

.. versionadded:: 0.0.1

.. autoclass:: k8scheck.condition.Condition
   :members:


Helpers
~~~~~~~

.. autofunction:: k8scheck.condition.check_all

.. autofunction:: k8scheck.condition.check_and_sort
