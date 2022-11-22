package mailauth;
use nginx;

our $auth_ok;
our $mail_server_ip={};
our $protocol_ports={};
$mail_server_ip->{'mailhost01'}="192.168.1.22";
$protocol_ports->{'smtp'}=25;

sub handler {
  my $r = shift;
  $auth_ok=1;

  if ($auth_ok==1){
    $r->header_out("Auth-Status", "OK") ;
    $r->header_out("Auth-Server", $mail_server_ip->{$hash->{'mail_server'}});
    $r->header_out("Auth-Port", $protocol_ports->{$r->header_in("Auth-Protocol")});
  } else {
    $r->header_out("Auth-Status", "Invalid login or password") ;
  }

  $r->send_http_header("text/html");

  return OK;
}

1;
__END__
