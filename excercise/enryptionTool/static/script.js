function changeOffsetVisibilty() {
    // checks if cesar is checked
    if (document.getElementById("encryptiontype-0").checked){
        document.getElementById("offset").style.display = 'block';
    } else {
        document.getElementById("offset").style.display = 'none';
    }
}

function checkIfCesarWasUsedForEncryption() {
    document.getElementByTagName('meta')
}

