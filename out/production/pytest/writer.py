import os
import subprocess
import threading
import time

FILE_NAME = 'version.txt'

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


def write():
    global output_data
    file = open(FILE_NAME)
    lines = file.read().splitlines()
    if len(lines) != 3:
        print('Caro utente, il programma si aspettava 3 righe')

    server = lines[0].split(':')
    server_path = server[1]
    server_args = server[2]
    server_instances = int(server[3])

    client = lines[1].split(':')
    client_path = client[1]
    client_args = client[2]
    client_instances = int(client[3])
    client_stdin = client[4]

    run_config = lines[2].split(':')
    version = run_config[1]
    num_iterate = int(run_config[2])

    output_data = open(version + '_' + str(client_instances) + '.csv', 'a+')
    # output_data.write(', '.join(['java_class','args','stdin','time'])+'\n')

    file.close()

    java_path = os.path.dirname(server_path)
    java_class = os.path.splitext(os.path.basename(server_path))[0]
    exec_server(java_path, java_class, server_args, '', server_instances)

    # server starts
    time.sleep(0.1)

    java_path = os.path.dirname(client_path)
    java_class = os.path.splitext(os.path.basename(client_path))[0]
    exec_client(java_path, java_class, client_args, client_stdin, client_instances, num_iterate)


def exec_client(java_path, java_class, args, stdin, n, num_iterate):
    for j in range(num_iterate):
        threads = list()
        for i in range(n):
            thread = ExcThread(java_path, java_class, args, stdin)
            threads.append(thread)
            thread.start()
        for index, thread in enumerate(threads):
            thread.join()

#FIXME
def exec_server(java_path, java_class, args, stdin, n):
    for i in range(n):
        ExcThread(java_path, java_class, args, stdin).start()