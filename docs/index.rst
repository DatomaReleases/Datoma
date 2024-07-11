.. datoma documentation master file, created by
   sphinx-quickstart on Mon Jan 22 16:14:38 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

datoma's documentation
=======================

**datoma** is a library intended to allow users to programatically submit jobs to Datoma's infrastructure. It is also intended to allow users to create their own workflows and submit them.

This library expands the possibilities offered by our `webpage <https://datoma.cloud/>`_, allowing users to automate their executions.

Main modules:
==============

.. toctree::
   :maxdepth: 7
   :caption: Main modules:
   :hidden:

   datomaJob
   datomaWorkflow

:doc:`datomaJob`
   The module intended to set inputs and parameters to any offered tool and submitting it to Datoma's infrastructure.
:doc:`datomaWorkflow`
   The module that allows you to set and submit your own workflow or choose a provided one.

.. toctree::
   :maxdepth: 7
   :caption: Usage examples:

   examples/jobExample
   examples/importJob
   examples/ephemeralWorkflowExample
   examples/complexExample
   examples/officialWorkflowExample
   


Installation Guide
==================

The following steps will guide you through the installation process:

* Prerequisites:
    * Python 3.11 or higher
    * pip

1. Install datoma:

.. code-block:: bash

    $ pip install datoma

2. Log in to datoma:

This is the step where you can specify if you have developer access. If you don't, please refrain from using the ``--dev`` flag. 

.. code-block:: bash

    $ python3 -m datoma login [--email <email>] [--password <password>] [--dev]

3. Obtain credentials:

.. code-block:: bash

    $ python3 -m datoma aws-creds