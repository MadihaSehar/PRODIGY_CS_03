####################### TASK 3: Pixel Manipulation for Image Encryption  #################
import subprocess

def install_package(package):
    try:
        subprocess.check_call(["python", '-m', 'pip', 'install', package])
    except Exception as e:
        print(f"Error installing {package}: {str(e)}")

# Check if NumPy is installed
try:
    import numpy as np
except ImportError:
    print("NumPy library not found. Installing...")
    install_package('numpy')
    import numpy as np

# Check if Pillow is installed
try:
    from PIL import Image
except ImportError:
    print("Pillow library not found. Installing...")
    install_package('Pillow')
    from PIL import Image

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        
        # Perform XOR operation with the key
        encrypted_array = img_array ^ key
        
        # Create encrypted image from the encrypted array
        encrypted_img = Image.fromarray(encrypted_array)
        
        # Save encrypted image
        encrypted_img.save("encrypted_image.png")
        print("Image encrypted successfully.")
    except Exception as e:
        print("Error encrypting image:", str(e))

def decrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        
        # Perform XOR operation with the key to decrypt
        decrypted_array = img_array ^ key
        
        # Create decrypted image from the decrypted array
        decrypted_img = Image.fromarray(decrypted_array)
        
        # Show decrypted image
        decrypted_img.show()
    except Exception as e:
        print("Error decrypting image:", str(e))

def main():
    try:
        image_path = input("Enter the path to the image: ")
        key = int(input("Enter the encryption/decryption key: "))
        option = input("Encrypt or Decrypt? (e/d): ")

        if option == 'e':
            encrypt_image(image_path, key)
        elif option == 'd':
            decrypt_image(image_path, key)
        else:
            print("Invalid option.")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
