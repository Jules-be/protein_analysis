import requests
from Bio import SeqIO
from io import StringIO

# https://www.uniprot.org/uniprot/P01308.fasta

def fetch_and_parse_fasta(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        fasta_data = StringIO(response.text)

        for seq_record in SeqIO.parse(fasta_data, "fasta"):
            print(f"ID: {seq_record.id}")
            print(f"Sequence: {seq_record.seq}")
            print(f"Length: {len(seq_record)}\n")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Please, enter the URL of the protein:")
url = input().strip()

fetch_and_parse_fasta(url)
