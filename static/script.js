function showSection(sectionId) {
    // Cacher le menu
    document.getElementById("menu").style.display = "none";

    // Cacher toutes les sections et retirer les anciennes classes de couleur
    let sections = document.querySelectorAll(".content");
    sections.forEach(section => {
        section.style.display = "none";
        section.classList.remove("bg-consultation", "bg-insertion", "bg-suppression", "bg-mise_a_jour");
    });

    // Afficher la section sélectionnée
    const section = document.getElementById(sectionId);
    section.style.display = "block";

    // Ajouter la classe de couleur correspondante
    section.classList.add("bg-" + sectionId);

}

function showMenu() {
    // Afficher le menu
    document.getElementById("menu").style.display = "grid";

    // Cacher toutes les sections
    let sections = document.querySelectorAll(".content");
    sections.forEach(section => section.style.display = "none");
}


function showFormInsertion() {
    const type = document.getElementById("Insertion-type").value;

    const forms = {
        "Agences_Spatiales": document.getElementById("Agences_SpatialesFormInsertion"),
        "Satellites": document.getElementById("SatellitesFormInsertion"),
        "Instrument_Embarqués": document.getElementById("Instrument_EmbarquésFormInsertion"),
        "Anomalie": document.getElementById("AnomalieFormInsertion"),
        "Missions": document.getElementById("MissionsFormInsertion"),
        "Données_Satellites": document.getElementById("Données_SatellitesFormInsertion"),
        "Zones": document.getElementById("ZonesFormInsertion"),
        "Observation": document.getElementById("ObservationFormInsertion"),
        "Stations_terrestres": document.getElementById("Stations_terrestresFormInsertion"),
        "Communication": document.getElementById("CommunicationFormInsertion"),
        "Sat_Telecom_Navigation": document.getElementById("Sat_Telecom_NavigationFormInsertion"),
        "Observation_De_Donnees": document.getElementById("Observation_De_DonneesFormInsertion"),
        "Sat_Recherche": document.getElementById("Sat_RechercheFormInsertion"),
        "Sat_Militaire": document.getElementById("Sat_MilitaireFormInsertion")
    };

    for (const key in forms) {
        if (forms.hasOwnProperty(key)) {
            forms[key].style.display = (key === type) ? "block" : "none";
        }
    }
}





function showFormmise_a_jour() {
    const type = document.getElementById("mise_a_jour_type").value;

    const forms = {
        "Agences_Spatiales": document.getElementById("Agences_SpatialesFormModification"),
        "Satellites": document.getElementById("SatellitesFormModification"),
        "Instrument_Embarqués": document.getElementById("Instrument_EmbarquésFormModification"),
        "Anomalie": document.getElementById("AnomalieFormModification"),
        "Missions": document.getElementById("MissionsFormModification"),
        "Données_Satellites": document.getElementById("Données_SatellitesFormModification"),
        "Zones": document.getElementById("ZonesFormModification"),
        "Stations_terrestres": document.getElementById("Stations_terrestresFormModification"),
        "Sat_Telecom_Navigation": document.getElementById("Sat_Telecom_NavigationFormModification"),
        "Observation_De_Donnees": document.getElementById("Observation_De_DonneesFormModification"),
        "Sat_Recherche": document.getElementById("Sat_RechercheFormModification"),
        "Sat_Militaire": document.getElementById("Sat_MilitaireFormModification")
    };

    for (const key in forms) {
        if (forms.hasOwnProperty(key)) {
            forms[key].style.display = (key === type) ? "block" : "none";
        }
    }
}






function confirmerModification() {
    return confirm("Êtes-vous sûr de vouloir modifier ces données ?");
}

function closePopup() {
    document.getElementById("alert-popup").style.display = "none";
}