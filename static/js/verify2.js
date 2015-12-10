function makeid()
{
    var text = "";
    var possible = "0123456789";

    for( var i=0; i < 4; i++ )
        text += possible.charAt(Math.floor(Math.random() * possible.length));

    return text;
}

function send_sms(number,id){
	var message = "http://api.mVaayoo.com/mvaayooapi/MessageCompose?user=gks@swifttote.com:gotoHell&senderID=TEST SMS&receipientno="+number+"&msgtxt=Hi your verification code for thefoodjoint account is"+id+"&state=4";
	var xmlHttp  = new XMLHttpRequest();

	xmlHttp.open("GET",message,true);
	
	xmlHttp.send(null);
	return xmlHttp.responseText;
}

function verifyNumber(number){
	var verificationCode = makeid();
	send_sms(number,verificationCode);
	var confirmationCode = prompt("verification code sent to"+number+"Please enter the code received");
	if(confirmationCode == verificationCode){
		return true;
	}
	else{
	return false;
	}	
}
