from requests_racer.core import SynchronizedSession
from time import sleep


url = 'http://localhost:5000/'
s = SynchronizedSession()

resp1 = s.get(url)
resp2 = s.get(url)

# at this point, the requests have been started but not finished.
# resp1 and resp2 should *not* be used.

s.finish_all()

sleep(3)
print(resp1.text)
print(resp2.text)
