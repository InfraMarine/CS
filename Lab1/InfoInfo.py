#this program calculates probabilities of chars, entropy and information quantity
#in text files (except whitespace chars)
import math,os
#this returns string with info about file
def analiz(filename):
    alpha = {}
    with open(filename,'r', encoding="utf8") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if not c.isspace():
                if c.isupper():
                    c = c.lower()
                alpha[c] = alpha.get(c, 0) + 1
    count = sum(alpha.values())
    entropy = 0
    res_str = filename + "\n"    
    for key in alpha:
        p = alpha[key] / count
        entropy += p * math.log2(p)
        res_str += "{}\t{:.3f}\n".format(key, p)
    entropy *= -1
    infoQ = entropy * count / 8     #converting to bytes
    filesize = os.path.getsize(filename)
    res_str += (f"{'entropy':<8} {'info':<12} {'size':<9} {'relation':<9}\n" +
    "{:<8.3f} {:<12.2f} {:<9d} {:<9.2f}\n".format(entropy, infoQ, filesize, infoQ * 100 / filesize))
    return res_str

#loading task (waht files to analize from txt file)
task_file = "task.txt"
writefile = "output.txt"
files = []
try:
    with open(task_file, 'r', encoding="utf8") as f:
        files = f.read().split("\n")
except IOError as e:
    print(e.strerror)

#executing algo
stringe = '-' * 30 + '\n'
for filename in files:
    stringe += analiz(filename)

#writing result
with open(writefile, 'a', encoding="utf8") as wf:
    wf.write(stringe)
