Usage
=====

.. _install:

Installation
------------

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
   | Demo for QA multiple records in a directory can be accessed `here <https://github.com/aid4mh/QPrism/blob/main/tests/Sensor/multi_record_Demo.ipynb>`_.
   | We have also provided demos that can validate the integrity of our DQM metrics, those demos can be accessed in the test folder at 
     `here <https://github.com/aid4mh/QPrism/blob/main/tests/Sensor/>`_, any notebook with the name <DQM_name>_testing.ipynb is the validation demo.
   | We have a `code template <https://github.com/aid4mh/QPrism/blob/main/tests/Sensor/demo_sensor.py>`_ that the user can use with minor modifications 
     to the input data.
Video
^^^^^
   | Demo for QA video(s) can be accessed `here <https://github.com/aid4mh/QPrism/blob/main/tests/Video/video_demo.ipynb>`_.
Audio
^^^^^
   | Demo for QA audio(s) can be accessed `here <https://github.com/aid4mh/QPrism/blob/main/tests/Audio/audio_demo.ipynb>`_.


