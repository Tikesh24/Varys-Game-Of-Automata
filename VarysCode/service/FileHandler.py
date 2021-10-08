import json
import os

from numpy import load

validation_count = 0

# Check if data folder exists or not
def initial_setup():
    if not os.path.exists('app_data'):
        os.makedirs('app_data')
        os.makedirs('app_data/event')
        os.makedirs('app_data/validataion')
        os.makedirs('app_data/automata')
        os.makedirs('app_data/configuration')
        os.makedirs('app_data/log')
        with open('app_data/configuration/varys_configuration.json', 'w') as f:
            config = {'wait_time':1}
            config = json.dumps(config)
            f.write(config)
            f.close()


def write_file(case, data: any):
    if 'write_event' == case:
        print("Writing events")
        # with open('app_data/event/events.txt', 'w') as f:
        #     f.write(str(data))
        data = json.dumps(data)
        with open("app_data/event/events.json", 'w') as f:
            f.write(data)


def read_file(case, seq: any):
    if 'read_event' == case:
        print('Reading events')
        with open('app_data/automata/{0}'.format(seq)) as f:
            events = json.load(f)
            return events

    elif 'read_validation' == case:
        print('Reading Validation {0}'.format(seq))
        arr = load('app_data/validataion/validate{0}.npy'.format(seq))
        return arr

    elif 'read_config' == case:
        print('Reading config')
        with open('app_data/configuration/varys_configuration.json') as f:
            config = json.load(f)
            return config
