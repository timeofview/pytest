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
        for i in range(int(self.config.iterations)):
            for j in range(int(self.config.threads)):
                thread = Execute(self.config,self.output_file)
                threads.append(thread)
                thread.start()
        if (self.config.join=='1'):
            for index, thread in enumerate(threads):
                thread.join()

class Execute(threading.Thread):
    def __init__(self,config,output_file):
        threading.Thread.__init__(self)
        self.config = config
        self.output_file = output_file

    def run(self):
        args = self.config.args.split()
        start = time.time()
        if self.config.extension == 'java':
            cmd = ['java', '-cp', self.config.path, self.config.filename]
        elif self.config.extension == 'c':
            cmd = [self.config.path, '/',self.config.filename]
        else:
            raise ValueError('Wrong extenstion')
        cmd.extend(args)
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate(self.config.stdin.encode())
        print(stdout.decode())
        end = time.time() - start
        if self.config.s_timestapm=='1':
            service = Service(self.config.version,self.config.name,self.config.args,self.config.threads,self.config.stdin,end,self.config.iterations)
            writer.write_service(self.output_file,service)


def exec(configs,output_file):
    threads = list()
    for config in configs:
        thread = Executor(config,output_file)
        threads.append(thread)
        thread.start()
    for index, thread in enumerate(threads):
        thread.join()

