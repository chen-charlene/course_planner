let text = document.getElementById('text');
let path = document.querySelector('path');
let pathLength = path.getTotalLength();
let pathHeight = path.getBoundingClientRect().height + 5;
const yearButtons = document.getElementsByClassName('year-button');
var incomingYear = 0;
var selectedConcentration = "";


path.style.strokeDasharray = pathLength + ' ' + pathLength;
path.style.strokeDashoffset = pathLength;


function handleScroll() {
    let value = window.scrollY;
    // scroll line animation
    var scrollPercentage = (document.documentElement.scrollTop) 
    / (document.documentElement.scrollHeight - document.documentElement.clientHeight);

    var drawLength = pathLength * scrollPercentage * 3;
    
    path.style.strokeDashoffset = pathLength - drawLength;
    
}

window.addEventListener('scroll', () => {
    let value = window.scrollY;
    text.style.marginTop = value * -0.2 + 'px';

    // Check if the animation has completed
    // if (value >= pathHeight) {
    //     window.removeEventListener('scroll', handleScroll);
    //    }
    // else handleScroll();
    handleScroll();
});

//prevent button-press from jumping back to top
for (let i = 0; i < yearButtons.length; i++) {
    yearButtons[i].addEventListener('click', function(e) {
        e.preventDefault();
        incomingYear = i + 1;
    });
}


const wrapper = document.querySelector('.dropdown-wrapper');
const concentrationContainer = document.querySelector('.selected-concentration-container');
concBtn = concentrationContainer.querySelector('.conc-btn');
searchInput = wrapper.querySelector('input');
options = wrapper.querySelector('.options');

let courses = [
    "AFRI Africana Studies - AB" ,"AMST American Studies - AB" ,"ANTH Anthropology - AB (Anthropological Archaeology)" ,"ANTH Anthropology - AB (Biological Anthropology)" ,"ANTH Anthropology - AB (General Anthropology)" ,"ANTH Anthropology - AB (Linguistic Anthropology)" ,"ANTH Anthropology - AB (Medical Anthropology)" ,"ANTH Anthropology - AB (Socio-cultural Anthropology)" ,"APMA Applied Mathematics - AB" ,"APMA Applied Mathematics - SCB" ,"APMB Applied Mathematics-Biology - SCB" ,"APMC Applied Mathematics-Computer Science - SCB" ,"APME Applied Mathematics-Economics - AB (Advanced Economics)" ,"APME Applied Mathematics-Economics - AB (Mathematical Finance)" ,"APME Applied Mathematics-Economics - SCB (Advanced Economics)" ,"APME Applied Mathematics-Economics - SCB (Mathematical Finance)" ,"ARAN Archaeology & Ancient World - AB" ,"ARCT Architecture - AB" ,"ASTR Astronomy - AB" ,"BDS Behavioral Decision Sciences - AB" ,"BCHM Biochemistry & Molecular Biology - SCB" ,"BIOL Biology - AB" ,"BIOL Biology - SCB" ,"ENBI Biomedical Engineering - SCB" ,"BIOP Biophysics - SCB" ,"BEO Business, Entrepreneurship and Organizations - AB (Business Economics)" ,"BEO Business, Entrepreneurship and Organizations - AB (Entrepreneurship & Tech Mgmt)" ,"BEO Business, Entrepreneurship and Organizations - AB (Organizational Studies)" ,"CHPH Chemical Physics - SCB" ,"CHEM Chemistry - AB" ,"CHEM Chemistry - SCB" ,"CHEM Chemistry - SCB (Chemical Biology)" ,"CHEM Chemistry - SCB (Materials)" ,"CLAS Classics - AB" ,"CLAS Classics - AB (Greek and Latin)" ,"CLAS Classics - AB (Greek and Sanskrit)" ,"CLAS Classics - AB (Greek)" ,"CLAS Classics - AB (Latin and Sanskrit)" ,"CLAS Classics - AB (Latin)" ,"CLAS Classics - AB (Sanskrit)" ,"CLAS Classics - AB (South Asian Classics)" ,"COGN Cognitive Neuroscience - AB" ,"COGN Cognitive Neuroscience - SCB" ,"COGS Cognitive Science - AB" ,"COGS Cognitive Science - SCB" ,"COLT Comparative Literature - AB (Literary Translation)" ,"COLT Comparative Literature - AB (Literary in Three Languages)" ,"COLT Comparative Literature - AB (Literary in Two Languages)" ,"CSBI Computational Biology - AB" ,"CSBI Computational Biology - SCB" ,"CSCI Computer Science - AB" ,"CSCI Computer Science - SCB" ,"CSEC Computer Science - Economics - AB" ,"CSEC Computer Science - Economics - SCB" ,"CTMP Contemplative Studies - AB (Humanities)" ,"CTMP Contemplative Studies - AB (Sciences)" ,"NAIS Critical Native American and Indigenous Studies - AB" ,"DEVL Development Studies - AB" ,"EMOW Early Modern World - AB" ,"EAST East Asian Studies - AB" ,"ECON Economics - AB" ,"ECON Economics - AB (Business Economics)" ,"ECON Economics - AB (Public Policy)" ,"EDUC Education Studies - AB" ,"EGYA Egyptology & Assyriology - AB (Assyriology)" ,"EGYA Egyptology & Assyriology - AB (Egyptology)" ,"ENGN Engineering - AB" ,"ENGN Engineering - SCB (Chemical)" ,"ENGN Engineering - SCB (Computer)" ,"ENGN Engineering - SCB (Electrical)" ,"ENGN Engineering - SCB (Environmental)" ,"ENGN Engineering - SCB (Materials)" ,"ENGN Engineering - SCB (Mechanical)" ,"ENPH Engineering and Physics - SCB" ,"ENGL English - AB" ,"EVST Environmental Studies - SCB" ,"EVST Environmental Studies - AB" ,"ETHS Ethnic Studies - AB" ,"FFS French & Francophone Studies - AB" ,"GNSS Gender & Sexuality Studies - AB" ,"GEOL Geological Sciences - AB" ,"GEOL Geological Sciences - SCB" ,"GEOB Geology - Biology - AB" ,"GEOB Geology - Biology - SCB" ,"GEOC Geology - Chemistry - AB" ,"GEOC Geology - Chemistry - SCB" ,"GEOP Geology - Physics/Mathematics - AB" ,"GEOP Geology - Physics/Mathematics - SCB" ,"GMST German Studies - AB" ,"HHBI Health and Human Biology - AB" ,"HSLC Hispanic Literatures and Cultures - AB" ,"HIST History - AB" ,"HIAA History of Art and Architecture - AB" ,"INTL International Relations - AB (Political Economy and Society)" ,"INTL International Relations - AB (Security and Society)" ,"IAPA International and Public Affairs - AB" ,"ITAL Italian Studies - AB" ,"JUDS Judaic Studies - AB" ,"LACS Latin American & Caribbean Studies - AB" ,"LING Linguistics - AB" ,"LING Linguistics - SCB" ,"LITA Literary Arts - AB" ,"MATH Mathematics - AB" ,"MATH Mathematics - SCB" ,"MACS Mathematics-Computer Science - SCB" ,"MTEC Mathematics-Economics - AB" ,"MDVC Medieval Cultures - AB" ,"MDVC Medieval Cultures - AB (Late Antique Cultures)" ,"MIDE Middle Eastern Studies - AB" ,"MCMD Modern Culture and Media - AB (Practice based)" ,"MCMD Modern Culture and Media - AB (Theory based)" ,"MUSC Music - AB" ,"NEUR Neuroscience - SCB" ,"PHIL Philosophy - AB" ,"PHYS Physics - AB" ,"PHYS Physics - AB (Mathematical)" ,"PHYS Physics - SCB" ,"PHYS Physics - SCB (Astrophysics)" ,"PHYS Physics - SCB (Biological)" ,"PHYS Physics - SCB (Mathematical)" ,"PHPH Physics and Philosophy - AB" ,"POLI Political Science - AB" ,"POBR Portuguese and Brazilian Studies - AB" ,"PSYC Psychology - AB" ,"PSYC Psychology - SCB" ,"PHP Public Health - AB" ,"PLCY Public Policy - AB" ,"RELS Religious Studies - AB" ,"STS Science, Technology, and Society - AB" ,"SLAV Slavic Studies - AB" ,"SAR Social Analysis and Research - SCB" ,"SAR Social Analysis and Research - SCB (Organizational Studies)" ,"SOC Sociology - AB" ,"SOC Sociology - AB (Organizational Studies)" ,"SAST South Asian Studies - AB" ,"STAT Statistics - SCB" ,"TAPS Theatre Arts & Performance Studies - AB (Dance)" ,"TAPS Theatre Arts & Performance Studies - AB (Performance Studies)" ,"TAPS Theatre Arts & Performance Studies - AB (Theatre Arts)" ,"URBN Urban Studies - AB" ,"VISA Visual Arts - AB"
]

function addCourse() {
    options.innerHTML = "";
    courses.forEach(course => {
        //adding each course inside li and inserting all li inside 
        let li = '<li onclick="updateName(this)">' + course + '</li>';
        options.insertAdjacentHTML("beforeend", li);
    });
}

addCourse();

// function updateName(selectedLi) {
//     wrapper.classList.remove("active");
//     selectBtn.firstElementChild.innerText = selectedLi.innerText;
// }

searchInput.addEventListener('keyup', () => {
    let arr = [];
    let searchedVal = searchInput.value;
    arr = courses.filter(data => {
        return data.toLowerCase().includes(searchedVal);
    }).map(data => '<li onclick="updateName(this)">'+data+'</li>').join("");
    // ? arr : '<p>Course not found</p>'
    options.innerHTML = arr;
});

function updateName(selectedLi) {
    searchInput.value = "";
    addCourse();
    concentrationContainer.classList.remove("active");
    concBtn.firstElementChild.innerText = selectedLi.innerText;
    selectedConcentration = selectedLi.innerText;
}

let confBtnContainer = document.querySelector('.confirmation-btn-container');
let confBtn = confBtnContainer.querySelector('.confirmation-btn');

function checkForError() {
    errorMessage = [];
    var hasError = false;
    
    if (selectedConcentration == "") {
        errorMessage.push("no concentration selected");
        hasError = true;
    }
    if (incomingYear == 0) {
        errorMessage.push("no incoming year selected");
        hasError = true;
    }

    if (hasError == false) {
        document.getElementById("confirmation-btn").href = "course_display.html"
    } else {
        displayErrorMsg(errorMessage);
    }
}

function displayErrorMsg(errorMessage) {
    // var errorMessageElement = document.getElementById('error-message');
    // errorMessageElement.textContent = errorMessage;

    // var modal = new bootstrap.Modal(document.getElementById('error-modal'));
    // modal.show();
    var popupWindow = window.open('', 'ErrorPopup', 'width=400, height=300');
    popupWindow.document.write('<html><head><title>Error Message</title></head><body>');
    popupWindow.document.write('<h1>Error Message</h1>');
    popupWindow.document.write('<p>' + errorMessage + '</p>');
    popupWindow.document.write('</body></html>');

}


