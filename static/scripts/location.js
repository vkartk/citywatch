document.addEventListener('DOMContentLoaded', function() {    
    setupLocationPermission();
});

const setupLocationPermission = () => {
    let locationPermission = document.querySelector('#locationPermission');
    locationPermission.checked =false;
    locationPermission.addEventListener('click', () => {
        if (locationPermission.checked) getLocation(locationPermission);
    });
};

const checkGeolocationPermission = () => {
    
    navigator.permissions.query({ name: "geolocation" }).then((result) => {
        if (result.state === "prompt") locationPermission.checked =false;
    });
};

const showUserLocation = userLocation => {
    document.querySelector('#map').classList.toggle('hidden');
    document.querySelector('#defaultMap').classList.toggle('hidden');
    initMap(userLocation);
}

const setUserLocation = userLocation => {
    document.querySelector('#id_latitude').value = userLocation.lat;
    document.querySelector('#id_longitude').value = userLocation.lng;
}

const getLocation = (locationPermission) => {

    const successCallback = (position) => {
        console.log(position);
        let userLocation = { lat: position.coords.latitude, lng: position.coords.longitude };
        setUserLocation(userLocation);
        showUserLocation(userLocation);
    };
    
    const errorCallback = (error) => {
        locationPermission.checked = false;
        if (error.code === error.PERMISSION_DENIED) {
            alert('You denied location permission');
        }
        console.log(error);
    };
    
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
};

async function initMap(position) {
  
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  let map = new Map(document.getElementById("map"), {
    zoom: 15,
    center: position,
    mapId: "7fd910e2ccd9585d",
  });

  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Uluru",
  });
}