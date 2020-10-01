import random
import sys


print(f"Ich werfe {sys.argv[2]} Würfel mit {sys.argv[1]} Seiten:")

for i in range(int(sys.argv[2])):
    wurf_ergebnis = random.randint(1, int(sys.argv[1]) )
    print(f"Würfel Nr.{i+1}: {wurf_ergebnis}")

