

 var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 8
    });
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


function getLocation(){
    if ($('#isRuning').is(":checked"))
    {
        fxhr_('http://localhost:8080/location', function(resp){
            parseLocation(resp)
        }, function (err)
        {
            //alert(err)
        });
    }
}

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

    map.setCenter(new google.maps.LatLng(lat, lon));
    console.log('location updated: lat:' + lat + ", lon:" + lon)
    if ($('.linkindicator').hasClass('linkon')){
            $('.linkindicator').removeClass('linkon');
        }
        else{
            $('.linkindicator').addClass('linkon');
        }

}
setInterval(getLocation
, 5000);


