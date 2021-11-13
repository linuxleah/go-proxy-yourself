This WILL NOT WORK unless you ensure the CORS headers are being sent.
Ensure the .htaccess file here is taking effect, as well as the one in 'q',
and the one in 'curler' running on your remote server.

INSTALLATION INSTRUCTIONS:
1) Install index.py, the 'q' directory (including its .htaccess file), and
   the top-level .htaccess into a local Apache documents dir; e.g. on a Mac:

   sudo mkdir "/Library/WebServer/Documents/poc" && sudo cp -pRv index.py .htaccess q "/Library/WebServer/Documents/poc"

2) Ensure Apache is started; e.g. on a Mac:
   apachectl start

3) Install curler on a remote Web host. HIGHLY RECOMMENDED: SERVE IT UP VIA
   HTTPS!

   Ensure the .htaccess file is being respected on the remote host! You may
   need to add an AllowOverrides directive in Apache (or the equivalent for
   other Web servers).

4) Change the secret key in curler to something else. This is pure
   'security through obscurity', but it's better than nothing.

5) Likewise, change the "key=" parameter in index.py.




