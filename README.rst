Fleming Custom Taxi Environment Based on OpenAI Gym
***************************************************

Installation
============

Install in your working directory with:

.. code-block::

    git clone https://github.com/FlemingDL/gym_fleming.git
    cd gym_fleming
    pip install -e .

If using Google Colab or Jupyter Notebook, enter this at the top of your workbook:

.. code-block::

    !pip install gym
    !git clone https://github.com/FlemingDL/gym_fleming.git
    !pip install -e gym_fleming

(For Google Colab, you will need to restart your notebook after the step above (Runtime -> Restart all).

In your python file enter:

.. code-block::

    import gym
    import gym_fleming

To set the environment for the 5x10 map enter:

.. code-block::

    env = gym.make('taxi_fleming-5x10')

To set the environment for the 10x10 map enter:

.. code-block::

    env = gym.make('taxi_fleming-10x10')

To set the environment for the 20x20 map enter:

.. code-block::

    env = gym.make('taxi_fleming-20x20')