#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gearman
import wave
import os
import signal
import subprocess
def wav2mp3(gearman_worker, gearman_job):
    print 'JOB:'+gearman_job.data+"\n\n"
    #gearman_worker.send_job_data(gearman_job, str(character))
    #gearman_worker.send_job_status(gearman_job, idx + 1, total_chars)
    cmd = '/usr/bin/lame /var/www/upload.ural.im/wav/'+gearman_job.data+'.wav /var/www/upload.ural.im/mp3/'+gearman_job.data+'.mp3'
    print cmd
    proc = subprocess.Popen(cmd, shell=True)
    proc.wait()
    return "OK"

def simple(gearman_worker, gearman_job):
    print 'JOB:'+gearman_jod.data+"\n\n"
    return "OK"
def handler_end(signum, frame):
    onend()

def main():
    signal.signal(signal.SIGINT, handler_end)
    signal.signal(signal.SIGQUIT, handler_end)
    gm_worker = gearman.GearmanWorker(['localhost:4730'])
    gm_worker.set_client_id('wav2mp3')
    print 'started encmp3 main'+"\n";
    gm_worker.register_task('wav2mp3', wav2mp3)
    gm_worker.register_task('simple', simple)
    try:
	gm_worker.work()
    finally:
	onend()

def onend():
    try:
	os.remove('pids/'+os.path.basename(__file__)+'.pid')
    finally:
	pass

if __name__ == "__main__":
    pid = os.getpid()
    print 'started encmp3'+"\n";
    #fpid = open('pids/'+os.path.basename(__file__)+'.pid','w')
    #fpid.write(str(pid))
    main()
