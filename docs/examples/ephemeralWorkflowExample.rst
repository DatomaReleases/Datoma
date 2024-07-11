.. _creating_unofficial_workflows:

Submitting an unofficial workflow
=====================================

This section shows the usage of the ``DatomaWorkflow`` module, exemplifying how to submit unofficial (ephemeral) workflows to Datoma's infrastructure.

First of all, you should have prepared a workflow file with ``YAML`` extension (e.g. ``my_workflow.yml``) and a layout file with ``JSON`` extension (e.g. ``my_layout.json``).

**my_workflow.yml**: This file contains the workflow definition. It defines:

* The different jobs that will be executed.
* If a job input depends on the output of another job (``depends_on``). You can filter the files that are passed to the dependant job using ``regex``.
* Which inputs are considered global (``input_mapping``).
* Which parameters are considered global (``paremeter_mapping``).

.. literalinclude:: ../../code_examples/my_workflow.yml
    :language: yaml

**my_layout.json**: This file contains the layout of the workflow. It defines:

* The global inputs that will be used by the workflow (``globalInputs``).
* The global parameters that will be used by the workflow (``globalParameters``).
* The parameters that will be overriden for a specific job (``parameterOverrides``).

.. literalinclude:: ../../code_examples/my_layout.json
    :language: json


In this example, we submit an **unofficial** workflow that executes ``TIMSCONVERT``, ``RMSI`` and ``XCMSPEAKPICKING``:

* We first create the ``DatomaWorkflow`` object, specifying the paths to the necessary files mentioned above (``path_yaml`` and ``path_json``).
* We set the global input. In this example, it is only used as input for the first job. You can modify the ``YAML`` file to use it for additional jobs.
* Then, we set the input for the third job, which is executed independently (unlike ``my_second_step``, which depends from another job's output). 
* We modify the global parameter's value, which will change the value for all parameters depending on it.
* Next, we set the parameters of the job that we want to modify from the standard ``my_third_step`` model (which is the key identifying our ``xcmspeakpicking`` task). 
* After that, we submit the workflow to Datoma's infrastructure and download the output files.
* Finally, we print the running time of the workflow.

.. literalinclude:: ../../code_examples/ephemeral_workflow_example.py
    :language: python

To see a more complex usage of ``DatomaWorkflow``, refer to :ref:`using_complexexample`.