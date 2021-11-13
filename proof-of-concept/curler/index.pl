#!/usr/bin/perl
use LWP::Simple;
use CGI;

print("Access-Control-Allow-Origin: *\n\r");
print("Content-type: text/html\n\r\n\r");


$secretkey = "#igj2iqjQ_g-Yghj";



my $url = CGI::param('url');
my $key = CGI::param('key');
if ($key eq $secretkey) {
    if ($url ne "") {
        $content = get($url);
        print $content;
    }
} else {
    print "\n";
}
