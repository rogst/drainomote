function DisableRS(ip) {
    request = new XMLHttpRequest();
    request.open('GET', '/status/disable/' + ip, true);

    request.onload = function() {
      if (this.status >= 200 && this.status < 400){
        // Success!
        data = JSON.parse(this.response);
      } else {
        // We reached our target server, but it returned an error

      }
    };

    request.onerror = function() {
      // There was a connection error of some sort
    };

    request.send();
}