f=open('dna.txt','r')
fileData=f.read().strip().replace(" ","")
dnaMapping={
    "00":"A",
    "01":"G",
    "10":"C",
    "11":"T"
}
tripletMapping = {
        'AAA':'a','AAC':'b','AAG':'c','AAT':'d','ACA':'e','ACC':'f', 'ACG':'g','ACT':'h','AGA':'i','AGC':'j','AGG':'k','AGT':'l','ATA':'m','ATC':'n','ATG':'o','ATT':'p','CAA':'q','CAC':'r','CAG':'s','CAT':'t','CCA':'u','CCC':'v','CCG':'w','CCT':'x','CGA':'y','CGC':'z','CGG':'A','CGT':'B','CTA':'C','CTC':'D','CTG':'E','CTT':'F','GAA':'G','GAC':'H','GAG':'I','GAT':'J','GCA':'K','GCC':'L','GCG':'M','GCT':'N','GGA':'O','GGC':'P','GGG':'Q','GGT':'R','GTA':'S','GTC':'T','GTG':'U','GTT':'V','TAA':'W','TAC':'X','TAG':'Y','TAT':'Z','TCA':'1','TCC':'2','TCG':'3','TCT':'4','TGA':'5','TGC':'6','TGG':'7','TGT':'8','TTA':'9','TTC':'0','TTG':' ','TTT':'.'}
flagPart=""
finalFlagPart=""

#Convert binary to DNA using the binary and dna A,G,C,T mapping
for item in range(0,len(fileData),2):
    newData = fileData[item:item+2]
    flagPart += dnaMapping[newData]
print(flagPart)

#convert DNA A,G,C,T strands to Ascii using triplet mapping codon
for items in range(0,len(flagPart),3):
    newCodonData = flagPart[items:items+3]
    finalFlagPart += tripletMapping[newCodonData]
print(finalFlagPart)

#https://raw.githubusercontent.com/JohnHammond/ctf-katana/master/img/dna_codes.png
#https://raw.githubusercontent.com/JohnHammond/ctf-katana/master/img/genome-coding.jpg

