import masking

FILENAME = "vault.txt"

def save_credential(site, username, password):
    masked_pw = masking.mask_password(password)
    with open(FILENAME, "a") as f:
        f.write(f"{site},{username},{masked_pw}\n")
    print("-> Credential saved successfully!")

def view_credentials():
    try:
        with open(FILENAME, "r") as f:
            lines = f.readlines()
            
        if not lines:
            print("Vault is empty.")
            return

        print("\n--- Saved Credentials ---")
        for line in lines:
            site, username, masked_pw = line.strip().split(",")
            original_pw = masking.unmask_password(masked_pw)
            print(f"Site: {site} | Username: {username} | Password: {original_pw}")
        print("-------------------------\n")
        
    except FileNotFoundError:
        print("No vault file found. Add some credentials first.")