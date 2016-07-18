import pexpect
import sys

key = sys.argv[1]
pw = sys.argv[2]

cmd = "openssl rsa -in %s -out %s" % (key, key)

bash = pexpect.spawn('bash', echo=True)
bash.sendline(cmd)
bash.expect('Enter pass phrase')
bash.sendline(pw)
bash.sendline('echo COMPLETE')
bash.expect_exact('COMPLETE')
bash.sendline('exit')
bash.expect_exact(pexpect.EOF)
