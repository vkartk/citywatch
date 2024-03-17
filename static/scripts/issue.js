async function initMap(location) {
  
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
  
    let map = new Map(document.getElementById("map"), {
      zoom: 15,
      center: location,
      mapId: "7fd910e2ccd9585d",
    });
  
    const marker = new AdvancedMarkerElement({
      map: map,
      position: location,
      title: "Issue Location",
    });

    const content = `<h3 class='font-bold'>${location.title}</h3>
    <p>Latitude: ${location.lat}</p>
    <p>Longitude: ${location.lng}</p>
    <a href="https://www.google.com/maps/search/?api=1&query=${location.lat},${location.lng}" class='text-blue-500'>View on Google Maps</a>
    `;
    const infoWindow = new google.maps.InfoWindow({
      content: content,
    });
    marker.addListener("click", () => {
      infoWindow.open(map, marker);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const url = window.location.pathname;
    const issueId = url.split('/').filter(Boolean).pop();

    fetch(`/api/issue/${issueId}`)
      .then(response => response.json())
      .then(data => {
        const location = {
            title: data.title, 
            lat: data.latitude, 
            lng: data.longitude 
        };
        if(!location.lat || !location.lng) return;
        initMap(location);
      });
});