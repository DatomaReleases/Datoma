.. _using_complexexample:

Leveraging Datoma's potential
==============================

This section delves in a more complex example executed on the ``datoma`` library, showing an advanced usage of this tool.

As we show on the example, a great way of leveraging ``datoma``'s potential is to link inputs with other execution outputs.

In this example, we first submit a job to Datoma's infrastructure. Then we use its output as input for a workflow.

* We first create the ``DatomaJob`` and ``DatomaWorkflow`` objects.
* Then we create set the job's inputs with *local files*, we also modify the parameters we wish.
* We submit the job to Datoma's infrastructure.
* Instead of just listing the outputs, we will store them in the ``output_files`` variable.
* Next, we will set the workflow's global input with our job's output.
* After that, we submit the workflow and download the output files.
* Finally, we export a ``JSON`` file containing the information of our workflow.

.. literalinclude:: ../../code_examples/complex_example.py
    :language: python

To see an example on how to import a saved ``JSON`` file, refer to :ref:`using_importjob`.