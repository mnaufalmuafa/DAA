DEBUG = True
string = "acffecdefeffdea"
string = input("Teks : ")

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return "%s_%s" % (self.left, self.right)


## Mencari kode untuk setiap daun
def huffmanCodeTree(node, left=True, binString=""):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffmanCodeTree(l, True, binString + "0"))
    d.update(huffmanCodeTree(r, False, binString + "1"))
    return d

freq = {}
for c in string: #Mencari frekuensi dari setiap karakter
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

#Mengurutkan freq
#Mengubahnya menjadi tuple
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

#Membuat Tree
while len(nodes) > 1:
    key1, c1 = nodes[-1]
    key2, c2 = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffmanCodeTree(nodes[0][0])

tabel = []
print("")
print("Teks : ", string)
print()
print (" Char | Freq  | Huffman code ")
print ("-----------------------------")
for char, frequency in freq:
    tabel.append((char,frequency,huffmanCode[char]))

arrChar = list(string)
i = 0
while i < len(tabel) : #Menampilkan frekuensi dan kode Huffman
    char, frequency, kode = tabel[i]
    print(" %-4r | %5d | %12s" % (char, frequency, huffmanCode[char]))
    i = i + 1

kodeHuffman = ""
i = 0
while i < len(arrChar) : #Membuat hasil Encoding untuk string input
    j = 0
    while j < len(tabel) :
        char = tabel[j][0]
        if char == arrChar[i] :
            break
        j = j + 1
    kodeHuffman = kodeHuffman + tabel[j][2]
    i = i + 1

print()
print("Seteleh Encoding : ", kodeHuffman)
