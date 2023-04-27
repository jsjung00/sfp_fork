import h5py 
import os
import os.path as osp 
import numpy as np 
import sys

import gym
import d4rl


if __name__ == "__main__":
    env_name = sys.argv[1]
    dataset = gym.make(env_name).get_dataset()
    new_dataset = {k: dataset[k] for k in dataset if 'infos' not in k or 'observations' not in k or 'rewards' not in k}
    new_dataset['states'] = dataset['observations']
    new_dataset['goals'] = dataset['infos/goal']
    np.save(osp.join(osp.abspath(osp.expanduser("~")), f'.d4rl/datasets/{env_name}_primitive_distilled.npy'), new_dataset)
    # h5path = osp.join(osp.abspath(osp.expanduser("~")), f'.d4rl/datasets/Ant_maze_medium_noisy_multistart_True_multigoal_True_sparse.hdf5')
    # with h5py.File(h5path, "r") as f:
    #     # Print all root level object names (aka keys) 
    #     # these can be group or dataset names 
    #     print("Keys: %s" % f.keys())
    #     for key in f.keys():
    #         print(f'key: {key}')
        
    #     all_trajs = {'actions': [], 'states': [], 'goals': [], 'terminals': [], 'timeouts': []}
        
    #     actions_dataset = f['actions']
    #     actions = np.array(actions_dataset)


    #     infos_group = f['infos']
    #     goals = np.array(infos_group['goal'])


    #     observations_dataset = f['observations']
    #     states = np.array(observations_dataset)


    #     terminals_dataset = f['terminals']
    #     terminals = np.array(terminals_dataset)


    #     timeouts_dataset = f['timeouts']
    #     timeouts = np.array(timeouts_dataset)

    #     all_trajs['actions'] = actions
    #     all_trajs['states'] = states 
    #     all_trajs['goals'] = goals 
    #     all_trajs['terminals'] = terminals 
    #     all_trajs['timeouts'] = timeouts 