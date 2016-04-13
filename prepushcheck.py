import sh
import os 
import glob 

if os.system("g++ main.cpp -o prog")==256: #denotes failed compile
	print "compile error!"
	exit(1)
else:
	print "compile successful!"

tests = glob.glob('test*.cpp')
numberPassed = 0
numberFailed = 0
for test in tests:
	# first, compile test case
	cmd1 = "g++ " + test + " -o prog"
	if os.system(cmd1)==256: # failed compile
		print test + " compile error"
		exit(1)
	# now, run test case
	var = os.system("./prog")
	if var==0: #denotes successful return 0
		print test + " successful"
		numberPassed += 1
	else:
		print test + " failed"
		numberFailed += 1
print str(numberPassed) + " test cases passed"
print str(numberFailed) + " test cases failed"
if numberFailed>0:
	# stop push
	exit(1)
else:
	exit(0)