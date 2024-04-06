import matplotlib.pyplot as plt
import mappy

splints = 8
splint_data = [list() for x in range(splints)]
num_reads = [0 for x in range(splints)]

for i in range(splints):
    filepath = f"Anneal_Splint_{i+1}/R2C2_Consensus.fasta"
    for name, seq, qual in mappy.fastx_read(filepath): 
        splint_data[i].append(len(seq))
        num_reads[i] += 1
    plt.hist(splint_data[i], bins=range(0, 20001, 200), color='#F96419')
    plt.title(f"Splint {i+1} Histogram")
    plt.xlabel("Sequence Length (bp)")
    plt.ylabel("Frequency")

    plt.savefig(f"hists/hist_splint_{i+1}.png")

    plt.clf()
print(num_reads)
