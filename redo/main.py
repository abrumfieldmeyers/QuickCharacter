from ClassDef2 import Character

if __name__ == "__main__":
    p_name = input("Player Name: \n") or "Player A"
    c_name = input("Character Name: \n") or "My Character"
    cls = input("Class: \n") or "Fighter"
    spec = input("Species: \n") or "Human"
    bck = input("Back: \n") or "Soldier"
    rdm = input('random stats: ') or False    
    print("--------------------------------------------------")
    char = Character(p_name,c_name,cls,bck,spec,rdm)
    # print(char)