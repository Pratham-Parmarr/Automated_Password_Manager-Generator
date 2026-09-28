import generator
import vault
import evaluator

MASTER_PASSWORD = "admin"  

def main():
    print("=== SECURITY TERMINAL ===")
    user_pass = input("Enter Master Password to unlock: ")
    
    if user_pass != MASTER_PASSWORD:
        print("Access Denied! Incorrect Master Password.")
        return

    print("Access Granted!")
    
    while True:
        print("\n--- MENU ---")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Save Credential to Vault")
        print("4. View Saved Credentials")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            length = int(input("Enter length (default 12): ") or 12)
            use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
            use_num = input("Include numbers? (y/n): ").lower() == 'y'
            use_spec = input("Include special chars? (y/n): ").lower() == 'y'
            
            pwd = generator.generate_password(length, use_upper, use_num, use_spec)
            print(f"Generated Password: {pwd}")
            
        elif choice == "2":
            pwd = input("Enter password to evaluate: ")
            strength = evaluator.check_strength(pwd)
            print(f"Password Strength: {strength}")
            
        elif choice == "3":
            site = input("Enter Site Name: ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            vault.save_credential(site, username, password)
            
        elif choice == "4":
            vault.view_credentials()
            
        elif choice == "5":
            print("Exiting Security Terminal. Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()