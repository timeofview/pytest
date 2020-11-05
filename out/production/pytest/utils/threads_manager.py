import subprocess
import threading
import time
from model.outcome import Outcome

from persistence import writer


class Threader(threading.Thread):
    def __init__(self,config,output_file):
        threading.Thread.__init__(self)
        self.setting = config
        self.output_file = output_file

    def run(self):
        threads = list()
        for i in range(int(self.setting.iterations)):
            for j in range(int(self.setting.threads)):
                thread = Starter(self.setting, self.output_file)
                threads.append(thread)
                thread.start()
        if (self.setting.join):
            for index, thread in enumerate(threads):
                thread.join()

class Starter(threading.Thread):
    def __init__(self, setting, output_file):
        threading.Thread.__init__(self)
        self.setting = setting
        self.output_file = output_file

    def run(self):
        args = self.setting.args.split()
        start = time.time()
        if self.setting.extension == 'java':
            cmd = ['java', '-cp', self.setting.path, self.setting.filename]
        elif self.setting.extension == 'c':
            cmd = [self.setting.path, '/', self.setting.filename]
        else:
            raise ValueError('Wrong extenstion')
        cmd.extend(args)
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate(self.setting.stdin.encode())
        print(stdout.decode())
        end = time.time() - start
        if self.setting.s_timestapm== '1':
            service = Outcome(self.setting.version, self.setting.name, self.setting.args, self.setting.threads, self.setting.stdin, end, self.setting.iterations)
            writer.write_service(self.output_file,service)


def exec(settings, output_file):
    threads = list()
    for config in settings:
        thread = Threader(config, output_file)
        threads.append(thread)
        thread.start()
    for index, thread in enumerate(threads):
        thread.join()

