import subprocess
import threading
import time


class Service(threading.Thread):
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
        #output_data.write(str(out) + '\n')