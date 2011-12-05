from os import listdir, stat
from stat import ST_SIZE
from os.path import splitext
from subprocess import Popen, PIPE
from time import clock

exts = ('.mov', '.3gp')
#qs = xrange(1, 8)
qs = xrange(1, 2)
#runme = 'ffmpeg -y -i {0} -ar 22050 -ab 64k -ac 1 -s 640x360 -g 150 -q {2} -vb 100k {1}_q{2}.flv'
runme = 'mencoder {0} -o {1}.flv -ovc vfw -xvfwopts codec=vp6vfw.dll:compdata=settings.vps -oac mp3lame -lameopts cbr:br=64 -af lavcresample=22050 -vf yadif,scale=640:360,flip -of lavf'

def encode(f, path, q):
    cmd = runme.format(f, path, q)
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    start = clock()
    p.communicate()
    end = clock() - start
    #out = '{0}_q{1}.flv'.format(path, q)
    out = '{0}.flv'.format(path)
    print '{0},{1},{2}'.format(out, end, stat(out)[ST_SIZE])    

for f in listdir('.'):
    path, ext = splitext(f)
    if ext in exts:
        for q in qs:            
            encode(f, path, q)