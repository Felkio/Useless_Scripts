function Encrypt-Text {
    param(
        [string]$InputText,
        [string]$Key,
        [string]$IV
    )

    $encoding = [System.Text.Encoding]::UTF8
    $inputBytes = $encoding.GetBytes($InputText)
    $keyBytes = $encoding.GetBytes($Key)
    $ivBytes = $encoding.GetBytes($IV)

    $desCryptoServiceProvider = New-Object System.Security.Cryptography.DESCryptoServiceProvider
    $desCryptoServiceProvider.Mode = [System.Security.Cryptography.CipherMode]::CBC
    $desCryptoServiceProvider.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7

    $memoryStream = New-Object System.IO.MemoryStream
    $cryptoStream = New-Object System.Security.Cryptography.CryptoStream -ArgumentList @($memoryStream, $desCryptoServiceProvider.CreateEncryptor($keyBytes, $ivBytes), [System.Security.Cryptography.CryptoStreamMode]::Write)

    $cryptoStream.Write($inputBytes, 0, $inputBytes.Length)
    $cryptoStream.FlushFinalBlock()

    $encryptedBytes = $memoryStream.ToArray()
    $encryptedText = [Convert]::ToBase64String($encryptedBytes)

    $cryptoStream.Dispose()
    $memoryStream.Dispose()

    return $encryptedText
}

$inputText = "Hello, World!"
$key = "ABCDEFGA" # Chiave DES di 8 caratteri (64 bit)
$iv = "12345678" # Vettore di inizializzazione di 8 caratteri (64 bit)

$encryptedText = Encrypt-Text -InputText $inputText -Key $key -IV $iv
Write-Host "Testo cifrato: $encryptedText"
