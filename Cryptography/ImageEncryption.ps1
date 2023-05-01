function Encrypt-Image {
    param(
        [string]$InputImagePath,
        [string]$OutputImagePath,
        [string]$Key
    )

    # Convert the provided key to a byte array
    $keyBytes = [System.Text.Encoding]::UTF8.GetBytes($Key)

    # Create an instance of AesCryptoServiceProvider to perform AES encryption
    $aesCryptoServiceProvider = New-Object System.Security.Cryptography.AesCryptoServiceProvider
    # Set the cipher mode to ECB (Electronic Code Book)
    $aesCryptoServiceProvider.Mode = [System.Security.Cryptography.CipherMode]::ECB
    # Set the padding mode to PKCS7
    $aesCryptoServiceProvider.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
    # Set the key for AES encryption
    $aesCryptoServiceProvider.Key = $keyBytes

    # Read all bytes of the input image
    $inputBytes = [System.IO.File]::ReadAllBytes($InputImagePath)

    # Create a MemoryStream to store the encrypted data
    $memoryStream = New-Object System.IO.MemoryStream
    # Create a CryptoStream to perform encryption using the AesCryptoServiceProvider
    $cryptoStream = New-Object System.Security.Cryptography.CryptoStream -ArgumentList @($memoryStream, $aesCryptoServiceProvider.CreateEncryptor(), [System.Security.Cryptography.CryptoStreamMode]::Write)

    # Write the input bytes to the CryptoStream, encrypting them in the process
    $cryptoStream.Write($inputBytes, 0, $inputBytes.Length)
    # Flush the final block of encrypted data to the MemoryStream
    $cryptoStream.FlushFinalBlock()

    # Get the encrypted bytes from the MemoryStream
    $encryptedBytes = $memoryStream.ToArray()

    # Dispose of the CryptoStream and MemoryStream
    $cryptoStream.Dispose()
    $memoryStream.Dispose()

    # Write the encrypted bytes to the output image file
    [System.IO.File]::WriteAllBytes($OutputImagePath, $encryptedBytes)
}

$inputImagePath = "D:\Pictures\immagine.jpg"
$outputImagePath = "D:\Pictures\encrypte_immagine.jpg"
$Key = "ABCDEFGHIJKLMNOP" # AES key of 16 characters (128 bits)

Encrypt-Image -InputImagePath $inputImagePath -OutputImagePath $outputImagePath -Key $Key
