from Bio.Seq import Seq

single_seq = input("请输入你的核酸序列：")
dna = Seq(single_seq)
protein = dna.translate()
print(protein)

