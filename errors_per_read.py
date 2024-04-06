import matplotlib.pyplot as plt

def parse_sam_file(filename):
    values = []

    with open(filename, 'r') as sam_file:
        for line in sam_file:
            if line.startswith('@'):
                # Skip header lines
                continue
            fields = line.strip().split('\t')
            if len(fields) < 12:
                # Skip invalid lines
                continue
            # Extract the NM value from the SAM fields
            seqlen = int(fields[0].split("_")[-1])
            if fields[1] != '0' and fields[1] != '16':
                continue
            for field in fields:
                if field.startswith("NM"):
                    nm = int(field.split(":")[-1])
                    values.append(nm/seqlen)
    return values

parse_sam_file("Anneal_Splint_1/splint_1.sam")

# main functionality
splints = 8
splint_data = [list() for x in range(splints)]

for i in range(splints):
    filepath = f"Anneal_Splint_{i+1}/splint_{i+1}.sam"
    splint_data[i] = parse_sam_file(filepath)
    # plt.ylim(0, )
    plt.xlim(0.0, 0.3)  # Set x-axis limits from 0.0 to 1.0
    plt.hist(splint_data[i], bins=[x/100 for x in range(11)], color='#34abff')
    plt.title(f"Splint {i+1} Errors Per Read")
    plt.xlabel("NM Value")
    plt.savefig(f"hists_err/splint_{i+1}.png")
    plt.clf()
