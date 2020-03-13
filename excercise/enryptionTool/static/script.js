function changeOffsetVisibility() {
    /**
     * Change the visibility on f.ex. encryption page.
     * If Cesar is choosen it shows the offset box else not.
     * Doesn't work if page is reloaded after mono is selected
     */
    if (document.getElementById("encryptiontype-0").checked){
        document.getElementById("offset").style.display = 'block';
    } else {
        document.getElementById("offset").style.display = 'none';
    }
}

function checkIfCesarWasUsedForEncryption() {
    /**
     * Check Status of Encryption Type f. ex. Result page
     * If status contains a number it sows the offset Factor box
     */
    var meta_elements = document.getElementsByTagName("META");
    var status = "";
    for (var i = 0; i < meta_elements.length; i++) {
      if (meta_elements[i].name == "offsetStatus") {
        status = meta_elements[i].content;
      }
    }
    if (status == "") {
      document.getElementById("offsetResult").style.display = 'none';
    } else {
      document.getElementById("offsetResult").style.display = "block";
    }
  }

