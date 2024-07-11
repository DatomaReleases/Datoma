.. _using_datomaworkflow:

Submitting an official Workflow
=====================================

This section shows the usage of the ``DatomaWorkflow`` module, exemplifying how to submit official workflows to Datoma's infrastructure.

In this example, we submit an official workflow that executes ``RMSI`` and ``peakmatannotation``:

* We first create the ``DatomaWorkflow`` object, specifying the ``official_name``.
* Next, we set the parameters of the job that we want to modify from the standard ``rmsi2`` model (which is the key identifying our ``RMSI`` task). 
* Then, we set local files as the global input. 
* Finally, we submit the workflow to Datoma's infrastructure and download the output files.

.. literalinclude:: ../../code_examples/official_workflow_example.py
    :language: python

To see how to create unofficial ``DatomaWorkflow`` instances, refer to :ref:`creating_unofficial_workflows`.

If you want to see a more complex usage of ``DatomaWorkflow``, refer to :ref:`using_complexexample`.