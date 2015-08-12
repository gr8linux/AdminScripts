from netaddr import *
import sys
DEBUG = False
def debugger(msg):
	if DEBUG:
		print msg
	
if len(sys.argv) < 2:
	print "Use "+sys.argv[0]+" IP_LIST.TXT\n"
	print " IP list file format should be \n"
	print " a.b.c.d\n"
	print " or\n"
	print " a.b.c.d/w.x.y.z"
	exit()
filename = sys.argv[1]
debugger ("Opening "+filename )
iplist = []
with open(filename,'r') as ipfile:
	
	mylist = ipfile.read().splitlines()
	debugger(mylist)
	for rl in mylist:
	#	rl = ipfile.readline()
		if(rl):
			#rl.strip()
			#rl = rl[:-1]
			debugger(rl) 
			debugger(repr(rl))
			try: 
				iplist.append(IPNetwork(rl))
			except AddrFormatError:
				print "Address format is not defined"
			
		else:
			break
if(ipfile):
	debugger(iplist)
	cidrs = cidr_merge(iplist)
	for cid in cidrs:
		print cid
	ipfile.close()

