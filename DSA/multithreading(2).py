import threading

class x(threading.Thread):
    def run(self):
        for p in range(1,101):
            print(p)

class y(threading.Thread):
    def run(self):
        for q in range(101,201):
            print(q)

x1=x()
x1.start()
y1=y()
y1.start()
for r in range(201,301):
    print(r)
for i in range(301,401):
    print(i)
