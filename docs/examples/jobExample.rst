.. _using_datomajob:

Submitting a job
===========================

This section shows the usage of the ``DatomaJob`` module, exemplifying how to submit jobs to Datoma's infrastructure.

In this example, we submit a job that executes ``RMSI``:

* We first create the ``DatomaJob`` object.
* Then, we set local files as input. 
* Next, we set the parameters of the job that we want to modify from the standard model. 
* After that, we submit the job to Datoma's infrastructure and download the output files.
* Then, we export the job to a ``JSON`` file. To see how to import a ``Datoma object`` from a ``JSON`` file, refer to :ref:`using_importjob`.
* Finally, we print the running time of the job.

.. literalinclude:: ../../code_examples/job_example.py
    :language: python

To see a more complex usage of ``DatomaJob``, refer to :ref:`using_complexexample`.