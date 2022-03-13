#!/bin/python
from rdkit import Chem
from rdkit.Chem import AllChem
import csv
import os




def ECFP(ifile,ofile,diam,bits):
    """
    Generates circular fingerprints ECFP4 hashed into n bits length vectors
    """
    reader=csv.reader(open(ifile,'rb'),delimiter=',',quotechar='"')
    print "Now reading data from file: {}".format(ifile)
    writer=csv.writer(open(ofile,'wb'),delimiter=',')
    count=0
    headers=reader.next()
    print "Headers: {}".format(headers)
    ECFP=[]
    for j in range(1024):
	ECFP.append("ECFP4_"+str(j+1))
    writer.writerow(headers+ECFP)
    for row in reader:
        count+=1
	if count%1000==0:
            print count
        try:
            mol=Chem.MolFromSmiles(str(row[1]))
            Chem.SanitizeMol(mol)
            fp=AllChem.GetMorganFingerprintAsBitVect(mol,int(diam),nBits=int(bits))
            temp=[]
            for j in range(len(fp)):
                temp.append(fp[j])
            writer.writerow([row[0],row[1],row[2]]+temp)
        except:
            print row[0],row[1]
            pass

    return



if __name__ == '__main__':
    ECFP("CHEMBL218_cl.csv",
         "CHEMBL218_cl_ecfp_1024.csv",2,1024)
