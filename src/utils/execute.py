import subprocess
import threading
import time
from model.service import Service

from persistence import writer


class Executor(threading.Thread):
    def __init__(self,config,output_file):
        threading.Thread.__init__(self)
        self.config = config
        self.output_file = output_file

    def run(self):
        threads = list()
        for i in range(self.config.iterations):
            for j in range(self.config.thread):
                thread = Executor(self.config,self.output_file)
                threads.append(thread)
                thread.start()
        for index, thread in enumerate(threads):
            thread.join()

class Execute(threading.Thread):
    def __init__(self,config,output_file):
        threading.Thread.__init__(self)
        self.config = config
        self.output_file = output_file

    def run(self):
        start = time.time()
        if self.config.extension == 'java':
            cmd = ['java', '-cp', self.config.path, self.config.filename, self.config.args]
        elif self.config.extension == 'c':
            cmd = [self.config.path, '/',self.config.filename, self.config.args]
        else:
            raise ValueError('Wrong extenstion')
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate(self.stdin.encode())
        print(stdout.decode())
        end = time.time() - start
        service = Service(self.config.version,self.config.name,self.config.args,self.config.threads,self.config.stdin,end)
        writer.write_service(self.output_file,service)


def exec(configs,service_file):
    threads = list()
    output_file = writer.get_service_file(service_file)
    for config in configs:
        thread = Executor(config,output_file)
        threads.append(thread)
        thread.start()
    for index, thread in enumerate(threads):
        thread.join()
    output_file.close()

