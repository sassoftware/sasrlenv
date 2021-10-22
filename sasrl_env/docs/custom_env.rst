Creating Custom Python Environment of Reinforcement Learning
===============================================================

In this document, we explain how you can create a custom environment to be used in reinforcement learning (RL) algorithms. The method explained here follows the standard openAI Gym design.



Adding a new environment can be summarized in the following steps:

1. Create an environment file
------------------------------

The environment implementation inherits from `gym.Env <https://github.com/openai/gym/blob/8da6224b7263f9541a55d541d8268f68ece7d99e/gym/core.py>`_ and we need to define ``__init__()``, ``reset()`` and ``step()`` function as follows:

**__init__()**: This function is the function that is called from the entry point when creating the environment instance. It sets parameters and it also defines self.observation_space and self.action_space. These two spaces are defined in spaces of gym package.

**reset()**: This function resets the state of environment to the state at time zero.

**step()**: this function gets the action and simulates dynamics of the environment as a result of action. It will return the next state, reward, termination indicator, and info.

**seed()**: (optional) sets seed of the random number generator.



**EXAMPLE**: implementation of Linear Quadratic Regulator environment in ``lqr_env.py``:

.. code-block:: python

  class LqrEnv(gym.Env):

    def __init__(self, size, init_state, state_bound=np.inf):
      self.init_state = init_state
      self.size = size
      self.observation_space = spaces.Box(low=-state_bound, high=state_bound, shape=(size,))
      self.action_space = spaces.Box(low=-state_bound, high=state_bound, shape=(size,))
      self.seed()

    def seed(self, seed=None):
      self.np_random, seed = seeding.np_random(seed)
      return [seed]

    def reset(self):
      high = self.init_state*np.ones((self.size,))
      self.state = self.np_random.uniform(low=-high, high=high)
      self.last_u = None
      return self.state

    def step(self,u):
      costs = np.sum(u**2) + np.sum(self.state**2)
      self.state = np.clip(self.state + u, self.observation_space.low, self.observation_space.high)
      return self.state, -costs, False, {}

2. Create a pip package
------------------------

Your need to have the following folder structure for your files:


.. toctree::
   :maxdepth: 3
   :caption: Folder Structure
    gym-lqr/
      README.md
      setup.py
      gym_lqr/
        __init__.py
        envs/
          __init__.py
          lqr_env.py

The ``__init__.py`` inside the folder envs imports the environment:

.. code-block:: python

  from gym_lqr.envs.lqr_env import LqrEnv

and the ``__init__.py`` inside folder gym_lqr is responsible for registering environment with default parameters using the function `register() <https://github.com/openai/gym/blob/8da6224b7263f9541a55d541d8268f68ece7d99e/gym/envs/registration.py>`_ defined in openAI Gym:

.. code-block:: python

  register(
     id='Lqr-v0',
     entry_point='gym_lqr.envs:LqrEnv',
     max_episode_steps=150,
     kwargs={'size' : 1, 'init_state' : 10.},
  )

Other environments can be added similarly to this package or in another package.

**Recommendation**: In order to integrate the user-written environments with the remote connection to CAS server, it is required that the package name starts/ends with string "gym". In this case, sasrlenv will identify user written package automatically and expose the environment to the environment server. If you package name follows a different convention, you need to modify ``runServer.py`` and ``serverSingle.py`` to import the custom environment package.


3. Install custom environment
------------------------------
Install the custom environment package by running the pip installation:

.. code-block:: console

  cd gym-lqr
  pip install -e .


Now, the environment is ready to be called from python:

.. code-block:: python

  import gym
  import gym_lqr
  env = gym.make('Lqr-v0')

Other Examples
---------------

https://github.com/hubbs5/or-gym

https://github.com/openai/gym-soccer

https://github.com/openai/gym-wikinav

https://github.com/alibaba/gym-starcraft

https://github.com/endgameinc/gym-malware

https://github.com/hackthemarket/gym-trading

https://github.com/tambetm/gym-minecraft

https://github.com/ppaquette/gym-doom

https://github.com/ppaquette/gym-super-mario

https://github.com/tuzzer/gym-maze

