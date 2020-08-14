#  HTTP header response with Puppet.

exec { 'add Header':
command => 'sudo apt-get -y install haproxy;
echo "ENABLED=1" >> /etc/default/haproxy;
printf %s "frontend load_balancer
    bind *:80
    mode http
    default_backend holb
    
backend holb
    balance roundrobin
    server 1432-web-01 35.190.159.176:80 check
    server 1432-web-02 35.229.61.48:80 check" >> /etc/haproxy/haproxy.cfg;
service haproxy restart;',
sudo service haproxy restart;
',
provider   => 'shell',
}
