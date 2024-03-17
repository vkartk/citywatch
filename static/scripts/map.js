const  initMap = async mapData => {
    // Request needed libraries.
    const { Map, InfoWindow } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement, PinElement } = await google.maps.importLibrary(
      "marker",
    );
    const map = new Map(document.getElementById("map"), {
      zoom: 3,
      center: { lat: 21.7679, lng: 78.8718 },
      mapId: "7fd910e2ccd9585d",
    });
    const infoWindow = new InfoWindow({
      content: "",
      disableAutoPan: true,
    });

    // Add markers to the map.
    const markers = mapData.map( issue  => {
      const label = issue.label;
      const pinGlyph = new PinElement({
        glyph: label,
        glyphColor: "white",
      });
      const marker = new AdvancedMarkerElement({
        position: issue,
        content: pinGlyph.element,
      });

      // markers can only be keyboard focusable when they have click listeners
      // open info window when marker is clicked
      marker.addListener("click", () => {
        infoWindow.setContent(issue.title);
        infoWindow.open(map, marker);
      });
      return marker;
    });

    // Add a marker clusterer to manage the markers.
    new markerClusterer.MarkerClusterer({ markers, map });
}
  
 

const fetchIssues = async () => {
  try {
    const response = await fetch("/api/issues");
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
};

window.addEventListener("load", async () => {
  const issues = await fetchIssues();

  const mapData = issues.map(issue => {
    const label = issue['category'].charAt(0).toUpperCase();
    return {
      title: issue.title, 
      lat: issue.latitude, 
      lng: issue.longitude,
      label: label
    };
  });

  initMap(mapData);

});