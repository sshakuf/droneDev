

 var map, droneMarker;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 18
});
    droneMarker = new google.maps.Marker({
            position: map.getCenter(),
            icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 10
            },
            draggable: true,
            map: map
        });

    droneMarker.setMap(map);
        
}


//Usually, you put script-tags into the head
function myFunction(url) {
    //This performs a POST-Request.
    //Use "$.get();" in order to perform a GET-Request (you have to take a look in the rest-API-documentation, if you're unsure what you need)
    //The Browser downloads the webpage from the given url, and returns the data.
    $.post( url, function( data ) {
            //As soon as the browser finished downloading, this function is called.
            $('#demo').html(data);
    });
}

function fxhr_(url, _func, _err){
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == xhr.DONE) {           
            var resptxt = xhr.responseText;

            if (resptxt) {
                _func(resptxt);
            } else {
                _err(resptxt);                        
            }
        }
    }

    xhr.open("GET", url, true);
    xhr.send();
}

function xhr_(url, elementId){
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == xhr.DONE) {           
            var resptxt = xhr.responseText;

            if (resptxt) {
                document.getElementById(elementId).innerHTML = resptxt;
            } else {
                document.getElementById(elementId).innerHTML = "no response";
            }
        }
    }

    xhr.open("GET", url, true);
    xhr.send();
}

function getMeters(){
    return document.getElementById("textMeters").value;
}
function getAlt(){
    return document.getElementById("textAlt").value;
}


function getLocation(){
    if ($('#isRuning').is(":checked"))
    {
        fxhr_('http://localhost:8080/location', function(resp){
            parseLocation(resp)
            // refreshRate = 1000;
        }, function (err)
        {
            // refreshRate = 5000;
            //alert(err)
        });
    }
}


var refreshRate = 1000;
var oldLocation  = [0,0];

function parseLocation(loc){
    all = loc.substring(loc.indexOf(':') + 1);
    all = all.substring(0, all.indexOf('<'));
    params = all.split(',')
    lat =params[0].split('=')[1]
    lon =params[1].split('=')[1]
    alt =params[2].split('=')[1]
    $('#txtLAT').val(lat);
    $('#txtLON').val(lon);
    $('#txtALT').val(alt);

    console.log('location updated: lat:' + lat + ", lon:" + lon)
    if ($('.linkindicator').hasClass('linkon')){
            $('.linkindicator').removeClass('linkon');
        }
        else{
            $('.linkindicator').addClass('linkon');
        }

    droneMarker.setPosition( new google.maps.LatLng(lat, lon));
    map.panTo(new google.maps.LatLng(lat, lon));

    if (oldLocation[0] == 0) {
        oldLocation = [parseFloat(lat), parseFloat(lon)];
    }

    if ((oldLocation[0] - lat) > 0.0000001 || (oldLocation[1] - lon) > 0.0000001){

        var line = new google.maps.Polyline({
            path: [
                new google.maps.LatLng(oldLocation[0],oldLocation[1]), 
                new google.maps.LatLng(parseFloat(lat), parseFloat(lon))
            ],
            strokeColor: "#FF0000",
            strokeOpacity: 1.0,
            strokeWeight: 10,
            map: map
        });
    oldLocation = [parseFloat(lat), parseFloat(lon)];
    }





}

function updateJoystick(id, val)
{
    //$('#'+o)
    // s = 'http://localhost:8080/joystick/' + id[3] + '/' + val;
    // console.debug(s);
    xhr_('http://localhost:8080/joystick/' + id[3] + '/' + val, 'texthtm')
}

setInterval(getLocation
, refreshRate);


