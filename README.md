# hackerlab
mitmproxy with backdoor forwarding

#mitmproxy ile beraber backdoor iletme python 
:://::Gereksinimler:://::

sudo apt install python-pip
sudo apt install python2-pip
sudo apt install python3-pip

Gereksinim olan yüklemeler mitmf saldırılarının etkin olarak çalışması içindir .


Python kodunu mitmproxy ile beraber çalıştırmak için ./mitmdump -s /root/mitmproxy.py --mode transparent

iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080
yönlendirme yapılmalıdır.
