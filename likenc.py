import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ''
target = ''
upload_destination = ''
port = 0


def usage():
    print 'BHP Net Tool'
    print
    print "Usage: likenc.py -t target_host -p port"
    print "-l --listen          - listen on[host]:[port] for incoming connections"
    print "-e --execute=file_to_run    - execute the give file upon" \
          "                             receiving a connection"
    print "-c --command             - initialize a command shell"
    print "-u --upload=destination  - upon receiving connection upload a" \
          "                             file and write to [destination]"
    print
    print
    print "Examples: "
    print "likenc.py -t 192.168.0.1 -p 5555 -l -c"
    print "likenc.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "likenc.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./likenc.py -t 192.168.11.12 -p 135"
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hle:t:p:cu:',
                                   ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as e:
        print str(e)
        usage()
