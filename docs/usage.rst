Usage
=====

.. _install:

Installation
------------
For installation of the QPrism package, please first install and create a virtual environment using the following commands.

.. code-block:: console

   $ python3 -m pip install --user virtualenv

.. code-block:: console

   $ python3 -m venv QPrism

.. code-block:: console

   $ source QPrism/bin/activate
   
To use QPrism, the installation can be done with pip.
Since pip does not resolve the dependencies' version efficiently, please install QPrism with the following steps.

.. code-block:: console

   $ python3 -m pip install --upgrade pip

.. code-block:: console

   $ pip install -r https://raw.githubusercontent.com/aid4mh/QPrism/main/requirements.txt

.. code-block:: console

   $ pip install --no-deps QPrism

Examples
--------

We have provided detailed demo notebooks for each submodule.

Sensor
^^^^^^
   | Demo for QA a single record can be accessed `here <https://github.com/aid4mh/QPrism/blob/main/tests/Sensor/single_record_Demo.ipynb>`_.
   |
   | Demo for QA multiple records in a directory can be accessed `here <https://github.com/aid4mh/QPrism/blob/main/tests/Sensor/multi_record_Demo.ipynb>`_.
   |
   | We have also provided demos that can validate the integrity of our DQM metrics, those demos can be accessed in the test folder at
     `here <https://github.com/aid4mh/QPrism/blob/main/tests/Sensor/>`_, any notebook with the name <DQM_name>_testing.ipynb is the validation demo.
   |
   | We have a `code template <https://github.com/aid4mh/QPrism/blob/main/tests/Sensor/demo_sensor.py>`_ that the user can use with minor modifications
     to the input data.
   |
   | Note that the input dataframe should only contains numerical values. If there are non-numerical values, either a timestamp or a text entry,
     please refer `here <https://github.com/aid4mh/QPrism/blob/main/tests/Sensor/Non_numerical_record.ipynb>`_ for an example of solution.
Video
^^^^^
   | Demo for QA video(s) can be accessed `here <https://github.com/aid4mh/QPrism/blob/main/tests/Video/video_demo.ipynb>`_.
Audio
^^^^^
   | Demo for QA audio(s) can be accessed `here <https://github.com/aid4mh/QPrism/blob/main/tests/Audio/audio_demo.ipynb>`_.


