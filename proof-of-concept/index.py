#!/usr/bin/python

print("Access-Control-Allow-Origin: *\r\n"),
print("Referrer-Policy: unsafe-url\r\n"),
#print("Access-Control-Allow-Methods: GET, POST, HEAD, PUT\r\n"),
#print("Access-Control-Allow-Headers: Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token\r\n"),
print("Content-type: text/html\r\n\r\n"),


print '''
<html>
<head>
<title>GoProxyYourself Proof Of Concept</title>
<script type="text/javascript">
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    function doMainLoop() {
        setInterval(getFromQueue, 5000);
        setInterval(scrollToBottom, 250);
    } 
    function scrollToBottom() {
        var elem = document.getElementById('status');
        elem.scrollTop = elem.scrollHeight;
    }
    function getFromQueue() {
        var xmlHttp = new XMLHttpRequest();
        token = Math.round(Date.now() / 1000);
        xmlHttp.open( "GET", "http://192.168.1.167/poc/q?" + token, true  );
        xmlHttp.onload = function (e) {
            if (xmlHttp.readyState === 4) {
                if (xmlHttp.status === 200) {
                    urlToFetch = xmlHttp.responseText.trim();

                    // Update status log
                    if (document.getElementById("status").innerHTML != "") {
                        document.getElementById("status").innerHTML += "<br>\\n";
                    }
                    document.getElementById("status").innerHTML += urlToFetch;
                    // Fetch the page
                    var fetcher = new XMLHttpRequest();
                    fetcher.open( "GET", "https://twu.net/curler/?key=" + encodeURIComponent("#igj2iqjQ_g-Yghj") + "&url=" + encodeURIComponent(urlToFetch), true  );
                    fetcher.onload = function (e) {
                        if (fetcher.readyState === 4) {
                            if (fetcher.status === 200) {
                                document.getElementById("status").innerHTML = fetcher.responseText;
                            }
                        }
                    }
                    fetcher.send( null ); // Complete request

                } else {
                    console.error(xmlHttp.statusText)
                }
            }
        }
        xmlHttp.send( null );
    }
</script>

</head>
<body onload="javascript:doMainLoop()">
<div style="width: 90%; height: 90%; overflow-y:auto; align: center; vertical-align: center; background-color: #EEEEEE; font-size: 64pt;" id="status">
o hai, starting poc
</div>
</body>
</html>
''';
