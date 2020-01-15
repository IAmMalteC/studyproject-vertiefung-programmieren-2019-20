/**
 * Change the visibility on f.ex. encryption page.
 * If Cesar is choosen it shows the offset box else not.
 */
function changeOffsetVisibility() {
    // checks if cesar is checked
    if (document.getElementById("encryptiontype-0").checked){
        document.getElementById("offset").style.display = 'block';
    } else {
        document.getElementById("offset").style.display = 'none';
    }
}
/**
 * Check Status of Encryption Type f. ex. Result page
 * If status contains a number it sows the offset Factor box
 */
function checkIfCesarWasUsedForEncryption() {
    var status = getMetaContent(offsetStatus);
    if (status == ''){
        document.getElementById("offsetResult").style.display = 'none';
    }else{
        document.getElementById("offsetResult").style.display = 'block';
    }
}
/**
 * Get Meta Tag Content
 *
 * @param {string} metaName The meta tag name.
 * @return {string} The meta tag content value, or empty string if not found.
 */
function getMetaContent(metaName) {
    var metas = document.getElementsByTagName('meta');
    var re = new RegExp('\\b' + metaName + '\\b', 'i');
    var i = 0;
    var mLength = metas.length;
 
    for (i; i < mLength; i++) {
        if (re.test(metas[i].getAttribute('name'))) {
            return metas[i].getAttribute('content');
        }
    }
 
    return '';
}

