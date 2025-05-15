from token_aggregator import aggregate

distributor = "CvgM6wSDXWCZeCmZnKRQdnh4CSga3UuTXwrCXy9Ju6PC"
wallet = "9dPHyjTpBQSTjnfh2vSCYjbHWgnR37k6mPTeRyZrMz4Q"
mint =  "Ddm4DTxNZxABUYm2A87TFLY6GDG2ktM2eJhGZS3EbzHM"

def main():
    aggregate(distributor, mint, wallet)

main()