import os
import subprocess
import threading
import time

SERVICES_FILE = 'services.csv'

output_data = None


class ExcThread(threading.Thread):

    def __init__(self, java_path, java_class, args, stdin):
        threading.Thread.__init__(self)
        self.java_path = java_path
        self.java_class = java_class
        self.args = args
        self.stdin = stdin

    def run(self):
        start = time.time()
        cmd = ['java', '-cp', self.java_path, 'Client', self.args]
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate(self.stdin.encode())
        print(stdout.decode())
        end = time.time() - start
        out = ', '.join([self.java_class, self.args, self.stdin, "%.20f" % end])
        output_data.write(str(out) + '\n')


def exec_client(java_path, java_class, args, stdin, n, num_iterate):
    for j in range(num_iterate):
        threads = list()
        for i in range(n):
            thread = ExcThread(java_path, java_class, args, stdin)
            threads.append(thread)
            thread.start()
        for index, thread in enumerate(threads):
            thread.join()
    output_data.close()


def write_configs(configs_file, configs):
    file = open(configs_file, "w")
    for config in configs:
        file.write(config.to_string())
    file.close()

def write_services(services_file, services):
    file = open(services_file, "a")
    for service in services:
        file.write(service.to_string())
    file.close()

def write_service(services_file,service):
    services_file.write(service.to_string())

def get_service_file(services_file=SERVICES_FILE):
    return open(services_file, "a")

def write_groups(groups_file, groups):
    file = open(groups_file, "w")
    for group in groups:
        file.write(group.to_string())
    file.close()