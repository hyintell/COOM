# Continual Learning Module

This module provides popular continual learning baseline implementations on top of the Soft-Actor-Critic (SAC) algorithm.
The implementation is based on Tensorflow.

## Installation
To install the continual learning module, run the following command from the root directory of the repository:
```bash 
$ pip install COOM[cl]
```

## Running Experiments
You can run single task or continual learning experiments with `run_single.py` and `run_cl.py` scripts, respectively.
To see available script arguments, run with `--help` option, e.g. `python run_single.py --help`

### Single task
```
python run_single.py --scenario pitfall
```

### Continual learning
```
python run_cl.py --sequence CO4 --cl_method packnet
```

## Reproducing Experimental Results
We have also listed all the commands for running the experiments in our paper in 
[cl.sh](scripts/cl.sh) and [single.sh](scripts/single.sh).
We used seeds [0, 1, ..., 9] for all experiments in the paper.

### Average Performance, Forgetting, Forward Transfer and Action Distributions
We evaluate the continual learning methods on the COOM benchmark based on Average Performance, Forgetting, and Forward Transfer.
We use the following CL methods:
```
python CL/run_cl.py --sequence [SEQUENCE] --seed [SEED] --cl_method packnet --packnet_retrain_steps 10000 --clipnorm 2e-05
python CL/run_cl.py --sequence [SEQUENCE] --seed [SEED] --cl_method mas --cl_reg_coef=10000
python CL/run_cl.py --sequence [SEQUENCE] --seed [SEED] --cl_method agem --regularize_critic --episodic_mem_per_task 10000 --episodic_batch_size 128
python CL/run_cl.py --sequence [SEQUENCE] --seed [SEED] --cl_method l2 --cl_reg_coef=100000
python CL/run_cl.py --sequence [SEQUENCE] --seed [SEED] --cl_method ewc --cl_reg_coef=250
python CL/run_cl.py --sequence [SEQUENCE] --seed [SEED] --cl_method vcl --cl_reg_coef=1 --vcl_first_task_kl False
python CL/run_cl.py --sequence [SEQUENCE] --seed [SEED] --cl_method clonex --exploration_kind 'best_return' --cl_reg_coef=100 --episodic_mem_per_task 10000 --episodic_batch_size 128
python CL/run_cl.py --sequence [SEQUENCE] --seed [SEED] --batch_size 512 --buffer_type reservoir --reset_buffer_on_task_change False --replay_size 8e5  # Perfect Memory
python CL/run_cl.py --sequence [SEQUENCE] --seed [SEED]  # Fine-tuning
```

We ran the COC sequence with sparse reward and only with PackNet:
```
python CL/run_cl.py --sequence COC --seed [SEED] --sparse_rewards --cl_method packnet --packnet_retrain_steps 10000 --clipnorm 2e-05
```

Measuring Forward Transfer also requires running SAC on each task in isolation:
```
python CL/run_single.py --scenario [SCENARIO] --envs [ENVS] --seed [SEED] --no_test
```

### Network plasticity
To reproduce our network plasticity experiments from the paper, run the following command:
```
python CL/run_continual.py --sequence CO8 --seed [SEED] --repeat_sequence 10 --no_test --steps_per_env 100000
```

### Method Variations
To reproduce our method variations experiments from the paper, run the following command:
#### Image Augmentations
1. Random Convolution
2. Random Shift
3. Random Noise
```
python CL/run_continual.py --sequence CO8 --cl_method [METHOD] --seed [SEED] --augment --augmentation conv
python CL/run_continual.py --sequence CO8 --cl_method [METHOD] --seed [SEED] --augment --augmentation shift
python CL/run_continual.py --sequence CO8 --cl_method [METHOD] --seed [SEED] --augment --augmentation noise
```
#### Prioritized Experience Replay (PER)
```
python CL/run_continual.py --sequence CO8 --cl_method [METHOD] --seed [SEED] --buffer_type prioritized
```
#### LSTM
```
python CL/run_continual.py --sequence CO8 --cl_method [METHOD] --seed [SEED] --use_lstm
```
#### Critic Regularization
```
python CL/run_continual.py --sequence CO8 --cl_method [METHOD] --seed [SEED] --regularize_critic
```