# AdvanceGeospatial_Lab3
 Requirements my Project is fulfilling:
## 1. Map
    Requirement:
    “When a user visits the site, they should be taken to a page where they can see a map of the City of Calgary.”

    Implementation:
    I initialized a Leaflet map centered on [51.0447,−114.0719][51.0447, -114.0719][51.0447,−114.0719], which is the heart of Calgary, and I used an OpenStreetMap tile layer. This way, as soon as the page loads, the user immediately sees the map of Calgary without needing to do anything else.

## 2. Search with Date Range Picker
    Requirement:
    “Users should be able to search for building permits by date range with a date range picker.”

    Implementation:
    I included the daterangepicker library and provided a date input alongside a “Search” button. When the user clicks “Search,” my code constructs a SoQL query using the chosen start and end dates, then fetches the matching permits from the City of Calgary’s open data API. The resulting permits are displayed on the map as markers.

## 3. Identify (Marker Popups)
    Requirement:
    “When the user clicks on a marker, a pop-up box should appear showing issueddate, workclassgroup, contractorname, communityname, and originaladdress.”

    Implementation:
    Every permit marker is bound to a Leaflet popup that contains exactly those five fields:

                marker.bindPopup(`
                <strong>Issued Date:</strong> ${props.issueddate}<br/>
                <strong>Work Class:</strong> ${props.workclassgroup}<br/>
                <strong>Contractor:</strong> ${props.contractorname}<br/>
                <strong>Address:</strong> ${props.originaladdress}<br/>
                <strong>Community:</strong> ${props.communityname}<br/>
                `);

    So, when the user clicks a marker, they can see all the relevant details about that building permit at a glance.

## 4. Overlapping Markers
    Requirement:
    “Sometimes multiple building permits are located at the same spot. You need an intuitive way for the user to see them (e.g., OverlappingMarkerSpiderfier).”

    Implementation:
    I integrated OverlappingMarkerSpiderfier by adding each marker to an oms instance:

                oms.addMarker(marker);

    If two or more permits share identical coordinates, OverlappingMarkerSpiderfier “spiderfies” them on click, fanning them out so the user can easily select each permit without them being stacked on top of each other.

## 5. Marker Clustering
    Requirement:
    “At certain zoom levels, markers can be very close. You must use a clustering plug-in like Leaflet.markercluster.”

    Implementation:
    I also added Leaflet.markercluster to group nearby markers at lower zoom levels. My code creates a markerCluster object:

                let markerCluster = L.markerClusterGroup({
                spiderfyOnEveryZoom: false,
                spiderfyOnClick: false,
                disableClusteringAtZoom: 14
                });
                map.addLayer(markerCluster);

    Then, each marker is added via:

                markerCluster.addLayer(marker);

    This way, when markers are simply close (but not identical), they cluster together until the user zooms in, this will keep the map visually clean.

## 6. Refresh on New Search
    Requirement:
    “When a user searches for a new date range, the map should refresh and display the new results.”

    Implementation:
    In my “Search” button handler, I call:

                markerCluster.clearLayers();

before fetching the new permits. This removes any old markers, and then I add the newly fetched markers to the map. That way, each time the user picks a different date range, the map is updated with the most current results only.