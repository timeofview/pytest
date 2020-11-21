import subprocess
import threading
import time
from model.outcome import Outcome

from persistence import writer


class Threader(threading.Thread):
    def __init__(self, setting, output_file):
        threading.Thread.__init__(self)
        self.setting = setting
        self.output_file = output_file

    def run(self):
        threads = list()
        for i in range(int(self.setting.iterations)):
            for j in range(int(self.setting.threads)):
                thread = Starter(self.setting, self.output_file)
                threads.append(thread)
                thread.start()
        if (self.setting.concurrency):
            for index, thread in enumerate(threads):
                thread.join()


class Starter(threading.Thread):
    def __init__(self, setting, output_file):
        threading.Thread.__init__(self)
        self.setting = setting
        self.output_file = output_file

    def run(self):
        args = self.setting.args.split()
        stdin = '\n'.join(self.setting.stdin.split("@@@"))

        if self.setting.extension == 'class':
            cmd = ['java', '-cp', self.setting.path, self.setting.filename]
        elif self.setting.extension == '' or self.setting.extension == 'exe':
            cmd = [self.setting.path, '/', self.setting.filename]
        else:
            raise ValueError('Wrong extenstion')
        cmd.extend(args)
        start = time.time()
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = proc.communicate(stdin.encode())
        print(stdout.decode())
        end = time.time() - start
        if self.setting.s_timestamp:
            outcome = Outcome(self.setting.id, end)
            writer.write_outcome(self.output_file, outcome)


def exec(settings, output_file):
    threads = list()
    for setting in settings:
        thread = Threader(setting, output_file)
        threads.append(thread)
        thread.start()
    for index, thread in enumerate(threads):
        thread.join()
