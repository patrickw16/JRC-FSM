from multiprocessing.pool import ThreadPool
import subprocess
import sys
import os.path
import itertools

# globals
launched = 0
done = 0
n_runs = 0

def print_status():
    print('Launched: {}/{} Done: {}'.format(launched, n_runs, done), end='\r', flush=True)

def launch_scenario(index):
    global launched
    global done
    launched += 1
    print_status()
    p = subprocess.run(
        ['python', 'safety_check_runner.py'] + ['one_case'] + ['cut_in'] + ['model=CC_human_driver'] + ['initial_speed=108'] + [f'obstacle_speed={str(108-combinations[index][0])}'] + [f'front_distance={combinations[index][1]}'] + ['lateral_speed=-2'] + ['save_to_csv=True'] + ['headless=True'],
        stdout=subprocess.DEVNULL
    )
    done += 1
    print_status()


if __name__ == '__main__':

    v_delta_values = range(10, 42, 2)
    s_delta_values = range(10, 62, 2)

    # Generate all possible combinations
    combinations = list(itertools.product(v_delta_values, s_delta_values))

    n_runs = len(combinations)
    print_status()

    with ThreadPool() as p:
        p. map(launch_scenario, range(n_runs))

    print()
