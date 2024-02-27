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

const getLocation = (locationPermission) => {

    const successCallback = (position) => {
        console.log(position);
        userLocation = { lat: position.coords.latitude, lng: position.coords.longitude };
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

  // The map, centered at Uluru
  let map = new Map(document.getElementById("map"), {
    zoom: 15,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Uluru",
  });
}