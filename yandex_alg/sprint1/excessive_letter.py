from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
        
	for i in range(len(longer)):

		x = longer[i]

		if x in shorter:
			shorter = shorter.replace(x, '', 1)
		else:
			return x
              

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
